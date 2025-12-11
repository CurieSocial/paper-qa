#!/usr/bin/env python
"""
Document search script using PaperQA's vector search with cross-encoder re-ranking.
Fully LLM-free - only embedding and cross-encoder models are used.

Pipeline:
1. Tantivy keyword search → find relevant papers
2. Vector similarity + MMR → retrieve diverse candidates
3. Cross-encoder re-ranking → score candidates precisely against query
4. Return top-k results sorted by cross-encoder score

Interactive mode loads models once for fast repeated queries.
"""

import asyncio
from dataclasses import dataclass
from pathlib import Path

from paperqa import Docs, Settings
from paperqa.agents.search import SearchIndex
from paperqa.types import Text

# Default settings
DEFAULT_INDEX_DIR = Path.home() / ".pqa" / "indexes"
DEFAULT_WORKS_DIR = Path("./works")
DEFAULT_CROSS_ENCODER = "cross-encoder/ms-marco-MiniLM-L-6-v2"
DEFAULT_SNIPPET_RERANKER = "mixedbread-ai/mxbai-rerank-xsmall-v1"
DEFAULT_SNIPPET_SENTENCES = 3


def get_settings(works_dir: Path) -> Settings:
    """Settings optimized for search-only (no LLM calls)."""
    return Settings(
        # Local sentence-transformers embedding (free, no API key needed)
        embedding="st-sentence-transformers/all-mpnet-base-v2",
        parsing=dict(
            use_doc_details=False,  # Skip DOI/title LLM parsing
            multimodal=0,  # Skip media enrichment
        ),
        agent=dict(
            index=dict(
                paper_directory=str(works_dir),
            ),
        ),
    )


def get_index_name(works_dir: Path) -> str:
    """Generate a unique index name based on the works directory."""
    from hashlib import md5

    return f"search_index_{md5(str(works_dir.resolve()).encode()).hexdigest()[:16]}"


class CrossEncoderReranker:
    """Cross-encoder model for precise query-document relevance scoring."""

    def __init__(self, model_name: str = DEFAULT_CROSS_ENCODER):
        self.model_name = model_name
        self.model = None

    def load(self):
        """Load the cross-encoder model."""
        from sentence_transformers import CrossEncoder

        print(f"Loading cross-encoder: {self.model_name}...")
        self.model = CrossEncoder(self.model_name)
        print("Cross-encoder loaded.\n")

    def rerank(
        self, query: str, texts: list[Text], top_k: int | None = None
    ) -> list[tuple[Text, float]]:
        """
        Re-rank texts using cross-encoder scores.

        Args:
            query: The search query
            texts: List of Text objects to re-rank
            top_k: Return only top-k results (None = return all, sorted)

        Returns:
            List of (Text, score) tuples sorted by score descending
        """
        if self.model is None:
            raise RuntimeError("CrossEncoder not loaded. Call load() first.")

        if not texts:
            return []

        # Create query-text pairs for scoring
        pairs = [[query, t.text] for t in texts]

        # Get cross-encoder scores
        scores = self.model.predict(pairs)

        # Pair texts with scores and sort
        scored_texts = list(zip(texts, scores))
        scored_texts.sort(key=lambda x: x[1], reverse=True)

        if top_k is not None:
            scored_texts = scored_texts[:top_k]

        return scored_texts


class SnippetExtractor:
    """Extract the most relevant snippet from a text chunk using cross-encoder scoring."""

    def __init__(
        self,
        model_name: str = DEFAULT_SNIPPET_RERANKER,
        num_sentences: int = DEFAULT_SNIPPET_SENTENCES,
    ):
        self.model_name = model_name
        self.num_sentences = num_sentences
        self.model = None
        self.segmenter = None

    def load(self):
        """Load the cross-encoder model and sentence segmenter."""
        import warnings
        from sentence_transformers import CrossEncoder

        print(f"Loading snippet reranker: {self.model_name}...")
        self.model = CrossEncoder(self.model_name)

        # Suppress pysbd's SyntaxWarnings about escape sequences
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=SyntaxWarning)
            import pysbd
            self.segmenter = pysbd.Segmenter(language="en", clean=False)

        print("Snippet reranker loaded.\n")

    def extract_snippet(self, query: str, text: str) -> tuple[str, float]:
        """
        Extract the most relevant snippet from text.

        Args:
            query: The search query
            text: The full text to extract snippet from

        Returns:
            Tuple of (snippet text, score)
        """
        if self.model is None or self.segmenter is None:
            raise RuntimeError("SnippetExtractor not loaded. Call load() first.")

        # Split into sentences
        sentences = self.segmenter.segment(text)

        if not sentences:
            return text, 0.0

        # If fewer sentences than window size, return full text
        if len(sentences) <= self.num_sentences:
            score = float(self.model.predict([[query, text]])[0])
            return text, score

        # Create sliding windows of sentences
        windows = []
        for i in range(len(sentences) - self.num_sentences + 1):
            window_text = " ".join(sentences[i : i + self.num_sentences])
            windows.append(window_text)

        # Score all windows
        pairs = [[query, w] for w in windows]
        scores = self.model.predict(pairs)

        # Find best window
        best_idx = int(scores.argmax())
        return windows[best_idx], float(scores[best_idx])

    def extract_snippets_batch(
        self, query: str, texts: list[str]
    ) -> list[tuple[str, float]]:
        """
        Extract snippets from multiple texts efficiently.

        Args:
            query: The search query
            texts: List of text strings

        Returns:
            List of (snippet, score) tuples
        """
        if self.model is None or self.segmenter is None:
            raise RuntimeError("SnippetExtractor not loaded. Call load() first.")

        results = []
        all_pairs = []
        window_info = []  # Track which windows belong to which text

        for text_idx, text in enumerate(texts):
            sentences = self.segmenter.segment(text)

            if not sentences:
                window_info.append((text_idx, [(text, 0, 1)]))
                all_pairs.append([query, text])
                continue

            if len(sentences) <= self.num_sentences:
                window_info.append((text_idx, [(text, 0, 1)]))
                all_pairs.append([query, text])
                continue

            # Create windows for this text
            text_windows = []
            for i in range(len(sentences) - self.num_sentences + 1):
                window_text = " ".join(sentences[i : i + self.num_sentences])
                text_windows.append((window_text, len(all_pairs), 0))
                all_pairs.append([query, window_text])

            # Update last entry with count
            text_windows = [
                (w, start, len(text_windows)) for w, start, _ in text_windows
            ]
            window_info.append((text_idx, text_windows))

        # Score all pairs in one batch
        if all_pairs:
            all_scores = self.model.predict(all_pairs)
        else:
            all_scores = []

        # Extract best snippet for each text
        score_idx = 0
        for text_idx, windows in window_info:
            if len(windows) == 1:
                # Single window (short text)
                snippet, _, _ = windows[0]
                results.append((snippet, float(all_scores[score_idx])))
                score_idx += 1
            else:
                # Multiple windows - find best
                num_windows = len(windows)
                window_scores = all_scores[score_idx : score_idx + num_windows]
                best_local_idx = int(window_scores.argmax())
                best_snippet = windows[best_local_idx][0]
                best_score = float(window_scores[best_local_idx])
                results.append((best_snippet, best_score))
                score_idx += num_windows

        return results


@dataclass
class SearchResult:
    """Search result with relevance score and extracted snippet."""

    text: Text
    score: float
    snippet: str | None = None
    snippet_score: float | None = None

    @property
    def docname(self) -> str:
        return self.text.doc.docname

    @property
    def content(self) -> str:
        return self.text.text


async def build_index(
    works_dir: Path, settings: Settings, index_dir: Path | None = None
) -> SearchIndex:
    """Build search index from documents in works_dir."""
    if not works_dir.exists():
        raise FileNotFoundError(f"Directory not found: {works_dir}")

    supported_extensions = {".pdf", ".txt", ".html", ".md"}
    files = [
        f for f in works_dir.iterdir() if f.suffix.lower() in supported_extensions
    ]

    if not files:
        raise ValueError(f"No supported documents found in {works_dir}")

    index_name = get_index_name(works_dir)
    index_dir = index_dir or DEFAULT_INDEX_DIR

    search_index = SearchIndex(
        fields=["file_location", "body", "title", "year"],
        index_name=index_name,
        index_directory=index_dir,
    )

    print(f"Indexing {len(files)} documents from {works_dir}...")
    print(f"Index location: {index_dir / index_name}")

    for file_path in files:
        file_location = str(file_path.resolve())

        # Check if already indexed
        if await search_index.filecheck(file_location):
            print(f"  Skipping (cached): {file_path.name}")
            continue

        print(f"  Indexing: {file_path.name}")

        # Create Docs and add document with manual citation (no LLM call)
        tmp_docs = Docs()
        try:
            await tmp_docs.aadd(
                path=file_path,
                citation=file_path.stem,
                docname=file_path.stem,
                title=file_path.stem,
                settings=settings,
            )
        except Exception as e:
            print(f"    Warning: Failed to parse {file_path.name}: {e}")
            await search_index.mark_failed_document(file_location)
            continue

        # Add to search index
        await search_index.add_document(
            {
                "title": file_path.stem,
                "year": "Unknown",
                "file_location": file_location,
                "body": "".join(t.text for t in tmp_docs.texts),
            },
            document=tmp_docs,
        )

    await search_index.save_index()
    print("Index saved.\n")
    return search_index


async def load_index(works_dir: Path, index_dir: Path | None = None) -> SearchIndex:
    """Load existing search index."""
    index_name = get_index_name(works_dir)
    index_dir = index_dir or DEFAULT_INDEX_DIR

    search_index = SearchIndex(
        fields=["file_location", "body", "title", "year"],
        index_name=index_name,
        index_directory=index_dir,
    )
    return search_index


class SearchEngine:
    """Search engine with cross-encoder re-ranking and snippet extraction."""

    def __init__(
        self,
        works_dir: Path,
        settings: Settings,
        use_reranker: bool = True,
        reranker_model: str = DEFAULT_CROSS_ENCODER,
        use_snippets: bool = True,
        snippet_model: str = DEFAULT_SNIPPET_RERANKER,
        snippet_sentences: int = DEFAULT_SNIPPET_SENTENCES,
    ):
        self.works_dir = works_dir
        self.settings = settings
        self.use_reranker = use_reranker
        self.use_snippets = use_snippets
        self.index: SearchIndex | None = None
        self.embedding_model = None
        self.reranker: CrossEncoderReranker | None = None
        self.snippet_extractor: SnippetExtractor | None = None

        if use_reranker:
            self.reranker = CrossEncoderReranker(reranker_model)

        if use_snippets:
            self.snippet_extractor = SnippetExtractor(snippet_model, snippet_sentences)

    async def initialize(self, rebuild: bool = False):
        """Initialize index and load models."""
        # Load embedding model
        print("Loading embedding model...")
        self.embedding_model = self.settings.get_embedding_model()
        print("Embedding model loaded.\n")

        # Load cross-encoder if enabled
        if self.reranker is not None:
            self.reranker.load()

        # Load snippet extractor if enabled
        if self.snippet_extractor is not None:
            self.snippet_extractor.load()

        # Load or build index
        self.index = await load_index(self.works_dir)

        try:
            index_files = await self.index.index_files
            has_content = bool(index_files) and not rebuild
        except Exception:
            has_content = False

        if not has_content or rebuild:
            self.index = await build_index(self.works_dir, self.settings)

    async def search(self, query: str, k: int = 5) -> list[SearchResult]:
        """
        Search for relevant text chunks with optional cross-encoder re-ranking.

        Pipeline:
        1. Tantivy keyword search → find relevant papers
        2. Vector + MMR → retrieve candidates (3x k if reranking)
        3. Cross-encoder → precise re-ranking (if enabled)
        4. Return top-k results
        """
        if self.index is None or self.embedding_model is None:
            raise RuntimeError("SearchEngine not initialized. Call initialize() first.")

        # Keyword search to find relevant papers
        paper_results: list[Docs] = await self.index.query(
            query,
            top_n=50,
            field_subset=[f for f in self.index.fields if f != "year"],
        )

        if not paper_results:
            return []

        # Combine all texts from found papers
        combined_docs = Docs()

        for paper_docs in paper_results:
            doc = next(iter(paper_docs.docs.values()))
            await combined_docs.aadd_texts(
                texts=paper_docs.texts,
                doc=doc,
                settings=self.settings,
                embedding_model=self.embedding_model,
            )

        # Retrieve more candidates if re-ranking (to have good pool for reranker)
        retrieve_k = k * 3 if self.reranker else k

        # Vector search (MMR) for initial candidates
        candidates = await combined_docs.retrieve_texts(
            query=query,
            k=retrieve_k,
            settings=self.settings,
            embedding_model=self.embedding_model,
        )

        if not candidates:
            return []

        # Re-rank with cross-encoder if enabled
        if self.reranker:
            scored = self.reranker.rerank(query, candidates, top_k=k)
            results = [SearchResult(text=t, score=s) for t, s in scored]
        else:
            # No reranking - return with placeholder scores
            results = [SearchResult(text=t, score=0.0) for t in candidates[:k]]

        # Extract snippets if enabled
        if self.snippet_extractor and results:
            texts = [r.content for r in results]
            snippets = self.snippet_extractor.extract_snippets_batch(query, texts)
            for result, (snippet, snippet_score) in zip(results, snippets):
                result.snippet = snippet
                result.snippet_score = snippet_score

        return results


def print_results(results: list[SearchResult], query: str, show_scores: bool = True) -> None:
    """Print search results with snippets highlighted."""
    print(f"\nQuery: {query}")
    print(f"Found {len(results)} results:\n")
    print("=" * 80)

    for i, result in enumerate(results, 1):
        score_str = f" (score: {result.score:.3f})" if show_scores and result.score != 0.0 else ""
        print(f"\n[{i}] {result.docname}{score_str}")
        print("-" * 80)

        # Show snippet if available
        if result.snippet:
            snippet_score_str = f" (snippet score: {result.snippet_score:.3f})" if result.snippet_score else ""
            print(f">>> SNIPPET{snippet_score_str}:")
            print(result.snippet)
            print()
            print("--- Full chunk ---")

        print(result.content)
        print()

    print("=" * 80)


async def interactive_mode(engine: SearchEngine, k: int = 5):
    """Interactive search loop."""
    print("Enter search queries (Ctrl+C or 'quit' to exit):\n")

    while True:
        try:
            query = input("Search: ").strip()
            if not query:
                continue
            if query.lower() in ("quit", "exit", "q"):
                print("Exiting.")
                break

            results = await engine.search(query, k=k)
            if results:
                print_results(results, query, show_scores=engine.use_reranker)
            else:
                print(f"\nNo results found for: {query}\n")

        except KeyboardInterrupt:
            print("\nExiting.")
            break
        except Exception as e:
            print(f"Error: {e}\n")


async def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Document search with cross-encoder re-ranking (LLM-free)"
    )
    parser.add_argument("query", nargs="?", help="Search query (omit for interactive mode)")
    parser.add_argument(
        "--dir", "-d",
        default=str(DEFAULT_WORKS_DIR),
        help=f"Directory containing documents (default: {DEFAULT_WORKS_DIR})",
    )
    parser.add_argument(
        "--k", "-k",
        type=int,
        default=5,
        help="Number of results (default: 5)",
    )
    parser.add_argument(
        "--no-rerank",
        action="store_true",
        help="Disable cross-encoder re-ranking (faster, less precise)",
    )
    parser.add_argument(
        "--reranker-model",
        default=DEFAULT_CROSS_ENCODER,
        help=f"Cross-encoder model (default: {DEFAULT_CROSS_ENCODER})",
    )
    parser.add_argument(
        "--no-snippets",
        action="store_true",
        help="Disable snippet extraction",
    )
    parser.add_argument(
        "--snippet-model",
        default=DEFAULT_SNIPPET_RERANKER,
        help=f"Snippet reranker model (default: {DEFAULT_SNIPPET_RERANKER})",
    )
    parser.add_argument(
        "--snippet-sentences",
        type=int,
        default=DEFAULT_SNIPPET_SENTENCES,
        help=f"Number of sentences per snippet (default: {DEFAULT_SNIPPET_SENTENCES})",
    )
    parser.add_argument(
        "--rebuild", "-r",
        action="store_true",
        help="Force rebuild index",
    )
    parser.add_argument(
        "--index-only",
        action="store_true",
        help="Only build index, don't search",
    )
    args = parser.parse_args()

    works_dir = Path(args.dir).resolve()
    if not works_dir.exists():
        print(f"Error: Directory not found: {works_dir}")
        return

    settings = get_settings(works_dir)

    # Index-only mode
    if args.index_only:
        await build_index(works_dir, settings)
        return

    # Initialize search engine
    engine = SearchEngine(
        works_dir,
        settings,
        use_reranker=not args.no_rerank,
        reranker_model=args.reranker_model,
        use_snippets=not args.no_snippets,
        snippet_model=args.snippet_model,
        snippet_sentences=args.snippet_sentences,
    )
    await engine.initialize(rebuild=args.rebuild)

    if args.query:
        # Single query mode
        results = await engine.search(args.query, k=args.k)
        if results:
            print_results(results, args.query, show_scores=engine.use_reranker)
        else:
            print(f"No results found for: {args.query}")
    else:
        # Interactive mode (default)
        await interactive_mode(engine, k=args.k)


if __name__ == "__main__":
    asyncio.run(main())
