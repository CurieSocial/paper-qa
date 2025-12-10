# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

PaperQA2 is a high-accuracy retrieval augmented generation (RAG) system for scientific literature and documents. It combines document indexing, vector search, LLM-based summarization, and agentic workflows to answer questions from PDFs, text files, and other document formats.

## Development Commands

### Setup
```bash
# Install dependencies using uv (recommended)
uv sync

# Alternative: install with pip
pip install -e ".[dev]"
```

### Testing
```bash
# Run all tests (requires OPENAI_API_KEY)
pytest

# Run tests in parallel
pytest -n auto

# Run a single test file
pytest tests/test_specific.py

# Run a single test
pytest tests/test_specific.py::test_function_name

# Record new VCR cassettes for HTTP mocking
uv run pytest --record-mode=once tests/desired_test_module.py
```

### Code Quality
```bash
# Run pre-commit checks (formatting, linting, type checking)
pre-commit run --all-files

# Individual tools
mypy paperqa
refurb paperqa
pylint paperqa
```

### CLI Usage
```bash
# Basic question answering (in a directory with PDFs)
pqa ask 'What is PaperQA2?'

# Use a specific settings profile
pqa -s fast ask 'Your question here'
pqa -s high_quality ask 'Your question here'

# Search the answer index
pqa -i answers search 'ranking and contextual summarization'

# Index a directory of papers
pqa -i my_index_name index

# View current settings
pqa view
pqa -s fast view

# Save custom settings
pqa -s my_settings --temperature 0.5 --llm gpt-4o-mini save
```

## Architecture

### Core Components

**1. Document Processing Pipeline** (`src/paperqa/docs.py`, `src/paperqa/readers.py`)
- `Docs` class: Main collection managing documents, texts, and vector indices
- Workflow: PDF/text → `read_doc()` → parsed text + media → chunking → `Text` objects → embedding → vector index
- Supports multimodal parsing (text + images/tables) with optional LLM enrichment of media
- Document metadata is enhanced via `DocMetadataClient` querying Crossref, Semantic Scholar, Unpaywall

**2. Settings System** (`src/paperqa/settings.py`)
- Hierarchical Pydantic models: `Settings` → `AnswerSettings`, `ParsingSettings`, `PromptSettings`, `AgentSettings` → `IndexSettings`
- Bundled configurations in `src/paperqa/configs/` (high_quality, fast, wikicrow, contracrow, debug, tier*_limits)
- Settings are hashed to create index names, ensuring parsing consistency
- Key LLM roles:
  - `llm`: General use, metadata inference, answer generation
  - `summary_llm`: Creating contextual summaries (RCS = re-ranking and contextual summarization)
  - `agent.agent_llm`: Agent tool selection
  - `parsing.enrichment_llm`: Media enrichment (generating descriptions for images/tables)

**3. Agent System** (`src/paperqa/agents/`)
- `PaperQAEnvironment` (`env.py`): Aviary-based environment providing tools to agents
- Tools (`tools.py`):
  - `PaperSearch`: Search local index for relevant papers
  - `GatherEvidence`: Retrieve and summarize relevant text chunks
  - `GenerateAnswer`: Create final answer from evidence
  - `Complete`: Mark task completion with success/failure
- Agent types (`main.py`):
  - `"fake"`: Deterministic hard-coded tool sequence (search → gather → answer → complete)
  - `"ToolSelector"`: Aviary's LLM-based tool selector (default)
  - LDP agents: `ReActAgent`, `MemoryAgent`, `SimpleAgent`, `HTTPAgentClient`
- Paper indexing (`search.py`): Tantivy-based full-text search with `SearchIndex` and `SearchDocumentStorage`

**4. Type System** (`src/paperqa/types.py`)
- `Doc` / `DocDetails`: Document metadata (citation, DOI, authors, etc.)
- `Text`: Chunked text with embeddings, linked to a `Doc`, optionally with `ParsedMedia`
- `Context`: LLM-generated summary of a `Text` chunk for a specific question, with relevance score
- `PQASession`: Complete Q&A session (question, contexts, answer, token counts, tool history)
- `ParsedMedia`: Images/tables extracted from documents with optional enriched descriptions

**5. Metadata Clients** (`src/paperqa/clients/`)
- `DocMetadataClient`: Orchestrates queries to multiple providers
- Providers: `CrossrefProvider`, `SemanticScholarProvider`, `UnpaywallProvider`, `OpenAlexProvider`
- `JournalQualityPostProcessor`: Adds journal quality ratings
- `RetractionDataPostProcessor`: Checks retraction status

### Document Reading Flow

1. **Initial Read** (`Docs.aadd()` → `read_doc()` in `readers.py`)
   - Peek first pages to infer citation using `parsing.citation_prompt`
   - LLM extracts title, DOI, authors via `parsing.structured_citation_prompt`

2. **Metadata Enhancement**
   - `DocMetadataClient.upgrade_doc_to_doc_details()` queries providers
   - Merges data from Crossref, Semantic Scholar, Unpaywall
   - Generates/validates BibTeX, adds citation counts, journal quality

3. **Full Parsing**
   - Parse PDF with `parsing.parse_pdf` (defaults: pypdf or pymupdf)
   - If `parsing.multimodal` is enabled: extract images/tables
   - Optional: enrich media with `parsing.enrichment_llm` using surrounding text
   - Chunk text based on `parsing.reader_config['chunk_chars']` and `overlap`

4. **Embedding & Indexing**
   - Embed chunks (text + optional enriched media descriptions)
   - Add to `texts_index` (NumpyVectorStore or QdrantVectorStore)
   - Store in Tantivy index for keyword search

### Question Answering Flow

**Agent Mode** (default via `ask()` → `agent_query()`)
1. Build search index from `settings.agent.index.paper_directory`
2. Agent selects tools iteratively:
   - `PaperSearch`: Find papers via keyword → chunk → embed → add to Docs
   - `GatherEvidence`: MMR search → top-k chunks → contextual summarization → re-ranking
   - `GenerateAnswer`: Format contexts → LLM generates answer
   - `Complete`: Mark success/failure
3. Store answer in answers index

**Manual Mode** (via `Docs.aquery()`)
1. `aget_evidence()`: Retrieve k relevant chunks, create `Context` objects with summaries
2. `context_serializer()`: Format contexts for prompt
3. LLM call with `prompts.qa` template
4. Parse citations, format bibliography

### Evidence Gathering (RCS)

From `Docs.aget_evidence()`:
1. **Retrieval**: MMR search for top `answer.evidence_k` chunks
2. **Contextual Summarization**: For each chunk:
   - Prompt: `prompts.summary_json` or `prompts.summary`
   - LLM generates: summary + relevance score (0-10)
   - Creates `Context` with score-based filtering
3. **Re-ranking**: Sort by score, keep top `answer.answer_max_sources`
4. Filter contexts with `score >= answer.evidence_relevance_score_cutoff`

## Key Patterns

### Async/Sync Duality
All main operations have both sync and async versions. Sync methods wrap async with `get_loop().run_until_complete()`:
- `Docs.add()` → `Docs.aadd()`
- `Docs.query()` → `Docs.aquery()`
- `Docs.get_evidence()` → `Docs.aget_evidence()`

### Embedding Models
Configured via `settings.embedding`:
- OpenAI: `"text-embedding-3-small"` (default)
- Hybrid: `"hybrid-text-embedding-3-small"` (dense + sparse keyword)
- Sparse only: `"sparse"`
- Sentence Transformers: `"st-model-name"` (requires `pip install paper-qa[local]`)
- Custom via `embedding_model_factory()`

### LLM Integration
Uses `lmi` (LiteLLM Model Interface) for provider-agnostic LLM calls:
- All LLM names support LiteLLM format (e.g., `"gpt-4o"`, `"claude-3-5-sonnet-20240620"`, `"gemini/gemini-2.0-flash"`)
- Configure via `*_llm_config` settings (model_list, rate limits)
- Temperature defaults to 0.0 (deterministic), forced to 1.0 for o1/gpt-5 models

### Index Management
- Index name auto-generated from settings hash (paper_directory, embedding, chunk_size, etc.)
- Located in `~/.pqa/indexes/` by default (configurable via `PQA_HOME` or `agent.index.index_directory`)
- Rebuilt when settings change affecting parsing/embedding
- Set `agent.rebuild_index=True` to sync with paper_directory on load

### Multimodal Support
Enable with `parsing.multimodal`:
- `OFF` (0): Text only
- `ON_WITH_ENRICHMENT` (1): Parse media + LLM enrichment (default)
- `ON_WITHOUT_ENRICHMENT` (2): Parse media, no enrichment

Media enrichment (`Settings.make_media_enricher()`):
- For each image/table: prompt LLM with surrounding text (±`enrichment_page_radius` pages)
- Store description in `ParsedMedia.info['enriched_description']`
- Used to shift embeddings without polluting source text

## Package Structure

This is a monorepo with workspace packages in `packages/`:
- `paper-qa-pypdf`: PyPDF-based PDF parser
- `paper-qa-pymupdf`: PyMuPDF-based PDF parser (better for some PDFs)
- `paper-qa-docling`: Docling PDF parser (experimental)
- `paper-qa-nemotron`: NVIDIA Nemotron-based reader

## Testing Notes

- VCR cassettes in `tests/cassettes/` cache HTTP requests
- Cassettes filter sensitive headers (OPENAI_API_KEY, etc.) via `tests/conftest.py`
- Keep cassettes < 1 MB
- Tests use `typeguard` for runtime type checking (via pytest plugin)
- Test timeout: 300 seconds (configurable in `pyproject.toml`)

## Configuration Files

- `pyproject.toml`: Dependencies, tool configs (ruff, mypy, pytest, etc.)
- `.pre-commit-config.yaml`: Pre-commit hooks
- `src/paperqa/configs/*.json`: Bundled settings profiles
- `uv.lock`: Lockfile for reproducible builds

## Common Pitfalls

1. **Index not updating**: Ensure `agent.rebuild_index=True` or manually rebuild index
2. **Different results than papers**: Internal FutureHouse version has citation traversal and broader paper access
3. **Embedding mismatch**: Changing embedding model requires new index (different hash)
4. **Media too large**: LLM providers reject images > 5 MB; enrichment skips these automatically
5. **Rate limits**: Use tier*_limits configs or manual rate_limit settings to throttle LLM calls
