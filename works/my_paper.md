
Electron. Commun. Probab. 23 (2018), no. 66, 1–11. ELECTRONIC
https://doi.org/10.1214/18-ECP165 COMMUNICATIONS
ISSN: 1083-589X in PROBABILITY

Random walks in doubly random scenery*

Łukasz Treszczotko†

### Abstract

We provide a random walk in random scenery representation of a new class of stable self-similar processes with stationary increments introduced recently by Jung, Owada and Samorodnitsky. In the functional limit theorem they provided only a single instance of this class arose as a limit. We construct a model in which a significant portion of processes in this new class is obtained as a limit.

**Keywords**: local times; Lévy processes; stable self-similar processes; random walks in random scenery.
**AMS MSC 2010**: Primary 60G18, Secondary 60F17.
Submitted to ECP on February 14, 2018, final version accepted on August 17, 2018.

# 1 Introduction

## 1.1 Random walks in random scenery

Our model is based in the framework of random walks in random scenery models. They were first considered in [4], where a number of limit theorems regarding the scaling limits of these models were proved. The more specific context in which we will be working was presented in [1]. The model considered therein can be briefly sketched as follows. Assume that there is a *user* moving randomly on the *network* (in this paper the network is just Z) which earns random rewards (governed by the random scenery) associated to the points in the network that they visit. The quantity of interest is then the total amount of rewards collected. To be more precise, assume that that the movement of the user is a random walk on Z which after suitable scaling converges to the $\beta$-stable Lévy process with $\beta \in (1, 2]$. Furthermore, let the random scenery be given by i.i.d. random variables $(\xi_j)_{j \in Z}$ which belong to the normal domain of attraction of a symmetric strictly stable distribution with index of stability $\alpha \in (0, 2]$. Then the random walk in random scenery is given by

$$
Z_n = \sum_{k=1}^{n} \xi_{S_k}, \quad (1.1)
$$

where $S_k = \sum_{j=1}^{k} X_j$ is the random walk determining the movement of the user. If we consider a large number of independent *random walkers* moving in independent random sceneries, then the scaling limit in the corresponding functional limit theorem

*Supported NCN research grant PRELUDIUM NUM 2017/25/N/ST1/00368.
†University of Warsaw, Poland. E-mail: lukasz.treszczotko@gmail.com


---


Random walks in doubly random scenery

(see Theorem 1.2 in [1]) leads to the process which has the integral representation given by
$$
X = \left(\int_{\mathbb{R} \times \Omega'} L_t(x, \omega')M_\alpha(dx, d\omega')\right)_{t \ge 0} \quad (1.2)
$$
where $(L_t(x, \omega'))_{t \ge 0, x \in \mathbb{R}}$ is a jointly continuous version of the local time of the symmetric $\beta$-stable Lévy motion (defined on some probability space $(\Omega', \mathcal{F}', \mathbb{P}')$) and $M_\alpha$ is a symmetric $\alpha$-stable random measure on $\mathbb{R} \times \Omega'$ with control measure $\lambda_1 \otimes \mathbb{P}'$, which is itself defined on some other probability space $(\Omega, \mathcal{F}, \mathbb{P})$. The process (1.2) was also obtained in [6] where it arose as a limit of partial sums of a stationary and infinitely divisible process.

## 1.2 The limit process
Very recently Jung, Owada and Samorodnitsky in their paper [3], which was an extension of the model considered in [6], introduced a new class of self-similar stable processes whose members have an integral representation given by
$$
Y_{\alpha, \tilde{\beta}, \gamma}(t) := \int_{\Omega' \times [0, \infty)} S_\gamma(M_{\tilde{\beta}}((t-x)_+, \omega'), \omega') dZ_{\alpha, \tilde{\beta}}(\omega', x), \quad t \ge 0, \quad (1.3)
$$
where
$$
0 < \alpha < \gamma \le 2, 0 \le \tilde{\beta} < 1,
$$
$(S_\gamma(t, \omega'))_{t \ge 0}$ is a symmetric $\gamma$-stable Lévy motion and $(M_{\tilde{\beta}}(t, \omega'))_{t \ge 0}$ is an independent $\tilde{\beta}$-Mittag-Leffler process (see section 3 in [6] for more on the latter). Both of these processes are defined on a probability space $(\Omega', \mathcal{F}', \mathbb{P}')$. Finally $Z_{\alpha, \tilde{\beta}}$ is a symmetric $\alpha$-stable random measure on $\Omega' \times [0, \infty)$ with control measure $\mathbb{P}' \otimes \nu_{\tilde{\beta}}$, where $\nu_{\tilde{\beta}}(dx) = (1-\tilde{\beta})x^{-\tilde{\beta}} \mathbf{1}_{x \ge 0} dx$. By Proposition 3.2 in [3] the process $Y_{\alpha, \tilde{\beta}, \gamma}$ is $H$-sssi (self-similar with stationary increments) with Hurst coefficient $H = \tilde{\beta}/\gamma + (1-\tilde{\beta})/\alpha$. Here we use $\tilde{\beta}$ instead of $\beta$ so as not to confuse it with the notation we have adopted for this paper. Similarly as in the proof of (3.10) in [6] we can show that for $\tilde{\beta} \in (0, \frac{1}{2})$
$$
(Y_{\alpha, \tilde{\beta}, \gamma}(t))_{t \ge 0} \stackrel{d}{=} c_{\tilde{\beta}} \left(\int_{\Omega' \times \mathbb{R}} S_\gamma(L_t(x, \omega'), \omega') dZ_\alpha(\omega', x)\right)_{t \ge 0}, \quad (1.4)
$$
where $c_{\tilde{\beta}}$ is a constant depending only on $\tilde{\beta}$, $(L_t(x))_{t \ge 0}$ is the local time of a symmetric $\beta$-stable Lévy motion defined independent of the process $S_\gamma$ (both defined on $(\Omega', \mathcal{F}', \mathbb{P}')$), $\beta = (1-\tilde{\beta})^{-1}$ and $Z_\alpha$ is a symmetric $\alpha$-stable random measure on $(\Omega', \mathbb{R})$ with control measure $\mathbb{P}' \otimes \lambda_1$.
The limit process obtained in [3] corresponds to $\gamma = 2$ in (1.3) it is our purpose to provide a model in which the scaling limit is given by processes of the form (1.4) for any allowable choice of parameters $\alpha, \beta$ and $\gamma$.

## 2 Description of the model and the result
Imagine that each $x \in \mathbb{Z}$ is associated with a reward (or punishment) given by $\xi_x$ which takes integer values. Now imagine a *random walker* moving on $\mathbb{Z}$ independently of the rewards and starting at 0. Before the movement the walker generates a strategy $Y_1, Y_2, \dots$ of i.i.d. random variables which are independent of the $\xi_x$'s and his movement. Now, any time the walker visits a point $x$ he gets a reward (or receives punishment) given by $Y_k \times \xi_x$, where $k$ is number of times that the walker has already stayed at $x$ (including the current visit). Thus the amount by which a potential reward is being

ECP 23 (2018), paper 66. http://www.imstat.org/ecp/
Page 2/11


---


Random walks in doubly random scenery

multiplied depends only on the number of the visits. The total reward/punishment at time $n$ in this scheme is given by

$$\sum_{x \in \mathbb{Z}} \left( \sum_{k=1}^{N_n(x)} Y_k \right) \xi_x, \quad (2.1)$$

where

$$N_n(x) := \sum_{k=1}^{n} \mathbf{1}_{\{S_k=x\}} \quad (2.2)$$

denotes the number of visits to the point $x \in \mathbb{Z}$ up to time $n \in \mathbb{N}$ and $S_k = X_1 + \dots X_k$ is the random walk performed.
The specific context in which our model is investigated is an extension of the one presented in Section 1.2 of [1] and goes as follows. Let $(S_n)_{n \ge 0}$ be a random walk on $\mathbb{Z}$ such that

$$\frac{1}{a_n} S_n \Rightarrow Z_\beta, \quad (2.3)$$

where $Z_\beta$ has symmetric $\beta$-stable distribution $1 < \beta < 2$. In particular, we assume that the random walk is recurrent. In the most general setting $(a_n)_{n \ge 1}$ is regularly varying at infinity with exponent $\beta$. We will assume more, i.e., that $(S_n)$ is in the normal domain of attraction of $Z_\beta$ and take $a_n = n^{1/\beta}$. Let $\xi = (\xi_x)_{x \in \mathbb{Z}}$ be a family of i.i.d. random variable such that

$$\frac{1}{n^{1/\alpha}} \sum_{x=0}^{n} \xi_x \Rightarrow Z_\alpha, \quad (2.4)$$

where $Z_\alpha$ is a symmetric $\alpha$-stable random variable with $\alpha \in (0, 2)$. What is different from the model considered in [1] is that we introduce more randomness to the model with an i.i.d. sequence $(Y_n)_{n \ge 1}$ such that

$$\frac{1}{n^\gamma} \sum_{j=1}^{n} Y_j \Rightarrow Z_\gamma, \quad (2.5)$$

where $Z_\gamma$ has a symmetric $\gamma$-stable distribution with $\alpha < \gamma \le 2$. In the original formulation of [1] all the $Y_n$'s are equal to one. For technical reasons we will also assume that

$$\sup_{k \in \mathbb{N}} E \left| \frac{Y_1 + \dots + Y_k}{k^{1/\gamma}} \right|^{\alpha\kappa} < \infty, \quad (2.6)$$

for some $\kappa > 1$. The above condition can be viewed as a restriction on the distribution of $Y_1$. A sufficient condition for (2.6) to hold is given in the lemma below. We denote the characteristic function of $Y_1$ by $\phi$.
**Lemma 2.1.** If $\alpha > 1$, then (2.6) is satisfied as long as

$$\int_r^\infty \frac{|\phi'(\theta)|}{\theta^{\alpha\kappa}} d\theta < \infty \quad (2.7)$$

for some $r > 0$ and there is a finite constant $K$ such that $|\phi'(\theta)| \le K |\theta|^{\gamma-1}$ for $\theta$ in some neighbourhood of zero.
The proof of Lemma 2.1 is given in the Appendix.

The base for our study is the behaviour of the process

$$\tilde{Z}(t) := \sum_{x \in \mathbb{Z}} \left( \sum_{k=1}^{N_{[t]}(x)} Y_k \right) \xi_x, \quad t \ge 0. \quad (2.8)$$

ECP **23** (2018), paper 66. http://www.imstat.org/ecp/
Page 3/11


---

# Random walks in doubly random scenery

We also define the rescaled version of (2.8) by
$$D_n(t) := r_n^{-1} \tilde{Z}(nt), \quad n \ge 1, i \ge 1, t \ge 0, \quad (2.9)$$
with $r_n = n^{1/\gamma+1/(\alpha\beta)-1/(\gamma\beta)}$.
We are interested in the scaling limit in which we consider the aggregate behaviour of a large number of independent walkers with independent strategies and having independent environments from which they collect the rewards. More precisely, consider an i.i.d. sequence of processes $((D_n^{(i)}(t))_{t \ge 0})_{i=1}^\infty$, $n \ge 1$ and define for $t \ge 0$
$$G_n(t) := \frac{1}{c_n^{1/\alpha}} \sum_{i=1}^{c_n} D_n^{(i)}(t), \quad n \ge 1, \quad (2.10)$$
where $c_n$ is any sequence of positive integers converging to $+\infty$. Now we may state our result concerning the scaling limit of the above process.
**Theorem 2.2.** For any $0 < \alpha < \gamma \le 2$ the process $(G_n(t))_{t \ge 0}$ defined by (2.10) converges (up to a multiplicative constant) as $n \to \infty$, in the sense of finite-dimensional distributions, to the process given by (1.4).

# 3 Proof of Theorem 2.2

For clarity we divided the proof of Theorem 2.2 into a number of lemmas. Basically, we prove the convergence of finite-dimensional distributions by showing the convergence of appropriate characteristic functions. First we will state them and then proceed to their proofs. In order to simplify the notation we put
$$\tilde{N}_n(x) := \sum_{j=1}^{N_n(x)} Y_j, \quad (3.1)$$
for $n \in \mathbb{N}$ and $x \in \mathbb{Z}$. Since we are going to work a lot with the characteristic function of $\xi_0$ we introduce the following notation. Let
$$\lambda(u) = E(\exp(iu\xi_0)), \quad u \in \mathbb{R} \quad (3.2)$$
and
$$\bar{\lambda}(u) = \exp(-|u|^\alpha), \quad u \in \mathbb{R}. \quad (3.3)$$
Assume that $\theta_1, \dots, \theta_k \in \mathbb{R}$, $t_1, \dots, t_k \in [0, \infty)$ for $k \ge 1$. We want to show the convergence of the characteristic function of $\sum_{j=1}^k \theta_j G_n(t_j)$ to the corresponding characteristic function of the process given by (1.3).
The first lemma in this section removes the first layer of randomness in our scheme and expresses the characteristic function in question solely in terms of the random walk and the sequence $(Y_k)_{k \ge 1}$.
**Lemma 3.1.** For the setting as in Section 2
$$E\left(\exp\left(i \sum_{j=1}^k \theta_j G_n(t_j)\right)\right) = \left(E\left(\prod_{x \in \mathbb{Z}} \lambda\left(c_n^{-1/\alpha} r_n^{-1} \sum_{j=1}^k \theta_j \sum_{m=1}^{N_{[nt_j]}(x)} Y_m\right)\right)\right)^{c_n}. \quad (3.4)$$
The second lemma says that, in the limit, only the asymptotic behaviour of $\lambda$ near zero matters.
**Lemma 3.2.**
$$E\left(c_n \left(\prod_{x \in \mathbb{Z}} \lambda\left(c_n^{-1} r_n^{-1} \sum_{j=1}^k \theta_j \tilde{N}_{[nt_j]}(x)\right) - \bar{\lambda}\left(c_n^{-1} r_n^{-1} \sum_{j=1}^k \theta_j \tilde{N}_{[nt_j]}(x)\right)\right)\right) \quad (3.5)$$
converges to 0 as $n \to \infty$.

ECP 23 (2018), paper 66. http://www.imstat.org/ecp/
Page 4/11


---


Random walks in doubly random scenery

The third lemma is the backbone of the whole proof.
**Lemma 3.3.** Let
$$
B_n := \sum_{x \in \mathbb{Z}} \left| r_n^{-1} \sum_{j=1}^k \theta_j \sum_{m=1}^{N_{[nt_j]}(x)} Y_m \right|^\alpha, \quad n \ge 1. \quad (3.6)
$$

Then,
$$
\lim_{n \to \infty} E(B_n) = c(\alpha)E \left( \int_{\mathbb{R}} \left| \sum_{j=1}^k \theta_j Y(L_{t_j}(x)) \right|^\alpha dx \right), \quad (3.7)
$$

and
$$
E(\exp(-c_n^{-1}B_n)) = 1 - c_n^{-1}c(\alpha)E(B) + o(c_n^{-1}). \quad (3.8)
$$
Here $B = \int_{\mathbb{R}} |\sum_{j=1}^k \theta_j Y(L_t(x))|^\alpha dx$ and $c(\alpha)$ is a constant depending only on $\alpha$.
It is evident that given the lemmas above, Theorem 2.2 follows immediately (see the proof of Theorem 1.2 in [1]). First, however, we will show that the random variables $B_n$, $n \in \mathbb{N}$ introduced in the formulation of Lemma 3.3 are uniformly integrable. We do this by showing that $E|B_n|^\kappa$ is bounded uniformly in $n \in \mathbb{N}$ for some $\kappa > 1$.
**Lemma 3.4.** Assume that (2.6) holds for some $1 < \kappa < \gamma/(\gamma - \alpha)$. Then, for every $t > 0$ there is a constant $C$, independent of $n \in \mathbb{N}$ (possibly depending on $\kappa$), such that we have
$$
E(B_n^\kappa) \le C. \quad (3.9)
$$
**Proof of Lemma 3.4.** It is enough to prove the lemma with $k = 1$ and $\theta_1 = 1$. Fix $n \in \mathbb{N}$ and $t \ge 0$. Let $x_1, \dots, x_{s_n}$ be the points in the range of the random walk up to time $[nt]$ taken in the increasing order with respect to $N_{[nt]}(x_i)$. We can write
$$
B_n = \frac{1}{r_n^\alpha} \left( \left| Y_1 + \dots + Y_{N_{[nt]}(x_1)} \right|^\alpha + \dots + \left| Y_1 + \dots + Y_{N_{[nt]}(x_{s_n})} \right|^\alpha \right). \quad (3.10)
$$
Notice that by Jensen inequality, for any $\kappa > 1$ we have
$$
B_n^\kappa \le r_n^{-\kappa\alpha} R_{[nt]}^{\kappa-1} \left( \left| Y_1 + \dots + Y_{N_{[nt]}(x_1)} \right|^{\alpha\kappa} + \dots + \left| Y_1 + \dots + Y_{N_{[nt]}(x_{s_n})} \right|^{\alpha\kappa} \right), \quad (3.11)
$$
where $R_m = \sum_{x \in \mathbb{Z}} \mathbf{1}_{\{N_m(x)=0\}}$ for $m \in \mathbb{N}$. Since the sequence $(Y_n)_{n \in \mathbb{N}}$ and the random walk are independent, by conditioning on the random walk, we get
$$
E(B_n^\kappa) \le r_n^{-\kappa\alpha} \sup_{k \in \mathbb{N}} E \left| \frac{Y_1 + \dots + Y_k}{k^{1/\gamma}} \right|^{\alpha\kappa} E \left( R_{[nt]}^{\kappa-1} \left( N_{[nt]}(x_1)^{\frac{\alpha\kappa}{\gamma}} + \dots + N_{[nt]}(x_{s_n})^{\frac{\alpha\kappa}{\gamma}} \right) \right), \quad (3.12)
$$
We now claim that
$$
r_n^{-\kappa\alpha} E \left( R_{[nt]}^{\kappa-1} \sum_{k=1}^{R_{[nt]}} N_{[nt]}(x_k)^{\frac{\alpha\kappa}{\gamma}} \right) \quad (3.13)
$$
is bounded uniformly in $n \in \mathbb{N}$ for all $\kappa > 1$ sufficiently close to 0. Using Hölder inequality

ECP 23 (2018), paper 66. http://www.imstat.org/ecp/
Page 5/11


---


Random walks in doubly random scenery

with $p = \frac{\gamma}{\alpha\kappa}$ and $q = \frac{\gamma}{\gamma-\alpha\kappa}$ we see that (3.13) is no bigger than
$$
\begin{aligned}
& r_n^{-\kappa\alpha}\text{E}\left(R_{[nt]}^{\kappa-1} \left(\sum_{x \in \mathbb{Z}} \mathbf{1}_{\{N_{[nt]}(x) \neq 0\}}\right)^{\frac{\gamma-\alpha\kappa}{\gamma}}\right) [nt]^{\frac{\alpha\kappa}{\gamma}} \\
= & r_n^{-\kappa\alpha}\text{E}\left(R_{[nt]}^{\frac{(\gamma-\alpha)\kappa}{\gamma}}\right) [nt]^{\frac{\alpha\kappa}{\gamma}} \\
\leq & r_n^{-\kappa\alpha} \left(\text{E}(R_{[nt]})\right)^{\frac{(\gamma-\alpha)\kappa}{\gamma}} \left(\sum_{x \in \mathbb{Z}} N_{[nt]}(x)\right)^{\frac{\alpha\kappa}{\gamma}} \\
= & r_n^{-\kappa\alpha} \left(\text{E}(R_{[nt]})\right)^{\frac{(\gamma-\alpha)\kappa}{\gamma}} [nt]^{\frac{\alpha\kappa}{\gamma}}, \quad (3.14)
\end{aligned}
$$
where the inequality in (3.14) follows from Hölder inequality as long as $\kappa \leq \frac{\gamma}{\gamma-\alpha}$. By Lemma 1 in [4], $\text{E}(R_{[nt]}) \leq c_1[nt]^{1/\beta}$ for some constant $c_1$ depending only on $\beta$. We thus conclude that (3.13) can be bounded by
$$
\frac{c_1[nt]^{\frac{(\gamma-\alpha)\kappa}{\gamma\beta}} [nt]^{\frac{\alpha\kappa}{\gamma}}}{n^{\frac{\kappa\alpha}{\gamma} - \frac{\kappa}{\beta} + \frac{\kappa\alpha}{\gamma\beta}}}, \quad (3.15)
$$
which is bounded uniformly in $n \in \mathbb{N}$.

The proof of Lemma 3.1 is the same as the proof of Lemma 3.4 in [1] and, therefore, we skip it and proceed directly to the proof of Lemma 3.2.

### Proof of Lemma 3.2.
The proof presented here is very similar to the proof of Lemma 3.5 in [1]. Recall that, by assumption,
$$
\lambda(u) = \bar{\lambda}(u) + o(|u|^\alpha),
$$
as $u \to 0$. Let
$$
U_n(x) := r_n^{-1} \sum_{j=1}^k \theta_j \tilde{N}_{[nt_j]}(x), \quad n \in \mathbb{N}, x \in \mathbb{Z}. \quad (3.16)
$$
Using inequality (41) in [1]
$$
\left|\prod_{x \in \mathbb{Z}} \lambda(c_n^{-1/\alpha} U_n(x)) - \prod_{x \in \mathbb{Z}} \bar{\lambda}(c_n^{-1/\alpha} U_n(x))\right| \leq \sum_{x \in \mathbb{Z}} |\lambda(c_n^{-1/\alpha} U_n(x)) - \bar{\lambda}(c_n^{-1/\alpha} U_n(x))|. \quad (3.17)
$$
Therefore (3.5) can be bounded by
$$
c_n \text{E}\left(\sum_{x \in \mathbb{Z}} |\lambda(c_n^{-1/\alpha} U_n(x)) - \bar{\lambda}(c_n^{-1/\alpha} U_n(x))|\right). \quad (3.18)
$$
Define $g(v) = |v|^{-\alpha}|\lambda(v) - \bar{\lambda}(v)|$, for $v \neq 0$ and $g(0) = 0$. Then $g$ is bounded and continuous. With this notation (3.18) equals
$$
\text{E}\left(\sum_{x \in \mathbb{Z}} |U_n(x)|^\alpha g(c_n^{-1/\alpha} U_n(x))\right). \quad (3.19)
$$
Fix any $\epsilon > 0$ and choose $\delta > 0$ such that $|z| < \delta$ implies $|g(z)| < \epsilon$. Then, (3.19) can be bounded by
$$
\epsilon \text{E}\left(\sum_{x \in \mathbb{Z}} |U_n(x)|^\alpha\right) + \|g\|_\infty \text{E}\left(\sum_{x \in \mathbb{Z}} |U_n(x)|^\alpha \mathbf{1}_{\{c_n^{1/\alpha}|U_n(x)| \geq \delta\}}\right). \quad (3.20)
$$

ECP 23 (2018), paper 66.
Page 6/11
http://www.imstat.org/ecp/


---


Random walks in doubly random scenery

which in turn is bounded by
$$ \epsilon E\left(\sum_{x \in \mathbb{Z}} |U_n(x)|^\alpha\right) + \|g\|_\infty E\left(\sum_{x \in \mathbb{Z}} |U_n(x)|^\alpha \mathbf{1}_{\left\{\sum_{x \in \mathbb{Z}} |U_n(x)|^\alpha \geq c_n \delta^\alpha\right\}}\right). \quad (3.21) $$
Since, by Lemma 3.4 the sequence of random variables ($\sum_{x \in \mathbb{Z}} |U_n(x)|^\alpha$)$_{n \in \mathbb{N}}$ is uniformly integrable, the first sumand in (3.21) is bounded by $\epsilon$ times a constant independent of $n \in \mathbb{N}$ and the second converges to 0 as $n \to \infty$. The choice of $\epsilon$ was arbitrary and hence the proof is finished. $\square$

## Proof of Lemma 3.3.
First we are going to show that (3.7) holds. Without losing generality we may assume that $0 \leq t_1 \leq \dots \leq t_k$. For convenience we also put $t_0 = 0$. We can rewrite $E(B_n)$ as
$$ \int_{\mathbb{R}} \left| (\theta_1 + \dots + \theta_k) Z^{(1)}\left(N_{[nt_1]}([a_n x])\right) \left(\frac{N_{[nt_1]}([a_n x])}{n a_n^{-1}}\right)^{1/\gamma} \right. $$
$$ \left. \quad + (\theta_2 + \dots + \theta_k) Z^{(2)}\left(N_{[nt_2]}([a_n x]) - N_{[nt_1]}([a_n x])\right) \right. $$
$$ \left. \quad \quad \times \left(\frac{N_{[nt_2]}([a_n x]) - N_{[nt_1]}([a_n x])}{n a_n^{-1}}\right)^{1/\gamma} \right. $$
$$ \left. \quad + \dots + \right. $$
$$ \left. \quad + \theta_k Z^{(k)}\left(N_{[nt_k]}([a_n x]) - N_{[nt_{k-1}]}([a_n x])\right) \right. $$
$$ \left. \quad \quad \times \left(\frac{N_{[nt_k]}([a_n x]) - N_{[nt_{k-1}]}([a_n x])}{n a_n^{-1}}\right)^{1/\gamma} \right|^\alpha dx, $$
where $Z^{(1)}(\cdot), \dots, Z^{(k)}(\cdot)$ are i.i.d. copies of the sequence (we put $Z^{(j)}(0) = 0$ for convenience)
$$ Z^{(0)}(m) = \frac{1}{m^{1/\gamma}} (Y_1 + \dots + Y_m), \quad m \in \mathbb{N}, \quad (3.22) $$
which are independent of the random walk ($S_n$). By Skorochod representation theorem we may assume that for $j = 1, \dots, k$, $Z^{(j)}(m)$ converges almost surely to $Z^{(j)}$, which has symmetric $\gamma$-stable distribution and the random variables $Z^{(j)}$ are independent. Let
$$ C_n = \int_{\mathbb{R}} \left| (\theta_1 + \dots + \theta_k) Z^{(1)} \times \left(\frac{N_{[nt_1]}([a_n x])}{n a_n^{-1}}\right)^{1/\gamma} \right. $$
$$ \left. \quad + (\theta_2 + \dots + \theta_k) Z^{(2)} \times \left(\frac{N_{[nt_2]}([a_n x]) - N_{[nt_1]}([a_n x])}{n a_n^{-1}}\right)^{1/\gamma} \right. $$
$$ \left. \quad + \dots + \right. $$
$$ \left. \quad + \theta_k Z^{(k)} \times \left(\frac{N_{[nt_k]}([a_n x]) - N_{[nt_{k-1}]}([a_n x])}{n a_n^{-1}}\right)^{1/\gamma} \right|^\alpha . \quad (3.23) $$
We are going to show that $E(B_n) - E(C_n)$ converges to 0 as $n \to \infty$. For that we will need the inequalities:
$$ |a^\alpha - b^\alpha| \leq \alpha |a - b| (a^{\alpha-1} + b^{\alpha-1}), \quad \alpha > 1, \quad a, b \geq 0, \quad (3.24) $$
and
$$ |a^\alpha - b^\alpha| \leq |a - b|^\alpha, \quad 0 \leq \alpha \leq 1, \quad a, b \geq 0. \quad (3.25) $$

ECP 23 (2018), paper 66. http://www.imstat.org/ecp/ Page 7/11


---


Random walks in doubly random scenery

Assume first that $\alpha > 1$. Put
$$
A = \left| (\theta_1 + \dots + \theta_k) Z^{(1)} (N_{[nt_1]}([a_n x])) \left( \frac{N_{[nt_1]}([a_n x])}{na_n^{-1}} \right)^{1/\gamma} \right.
$$
$$
\quad + (\theta_2 + \dots + \theta_k) Z^{(2)} (N_{[nt_2]}([a_n x]) - N_{[nt_1]}([a_n x]))
$$
$$
\quad \times \left( \frac{N_{[nt_2]}([a_n x]) - N_{[nt_1]}([a_n x])}{na_n^{-1}} \right)^{1/\gamma}
$$
$$
\quad + \dots +
$$
$$
\quad + \theta_k Z^{(k)} (N_{[nt_k]}([a_n x]) - N_{[nt_{k-1}]}([a_n x]))
$$
$$
\quad \times \left. \left( \frac{N_{[nt_k]}([a_n x]) - N_{[nt_{k-1}]}([a_n x])}{na_n^{-1}} \right)^{1/\gamma} \right|,
$$
and
$$
B = \left| (\theta_1 + \dots + \theta_k) Z^{(1)} \times \left( \frac{N_{[nt_1]}([a_n x])}{na_n^{-1}} \right)^{1/\gamma} \right.
$$
$$
\quad + (\theta_2 + \dots + \theta_k) Z^{(2)} \times \left( \frac{N_{[nt_2]}([a_n x]) - N_{[nt_1]}([a_n x])}{na_n^{-1}} \right)^{1/\gamma}
$$
$$
\quad + \dots +
$$
$$
\quad + \theta_k Z^{(k)} \times \left. \left( \frac{N_{[nt_k]}([a_n x]) - N_{[nt_{k-1}]}([a_n x])}{na_n^{-1}} \right)^{1/\gamma} \right|.
$$
Then by (3.24) and Hölder inequality
$$
E|a^\alpha - b^\alpha| \le \alpha E(|A - B|(A^{\alpha-1} + B^{\alpha-1}))
$$
$$
\le \alpha (E|A - B|^\alpha)^{1/\alpha} ((EA^\alpha)^{(\alpha-1)/\alpha} + (EB^\alpha)^{(\alpha-1)/\alpha}).
$$
By triangle inequality
$$
|A - B| \le \sum_{j=1}^k |\theta_j + \dots + \theta_k| \left| Z^{(j)} \left( N_{[nt_j]}([a_n x]) - N_{[nt_{j-1}]}([a_n x]) \right) \right.
$$
$$
\quad - Z^{(j)} \left. \left( \frac{N_{[nt_j]}([a_n x]) - N_{[nt_{j-1}]}([a_n x])}{na_n^{-1}} \right)^{1/\gamma} \right|. \quad (3.26)
$$
Notice that by (2.6) the sequence of random variables
$$
\left( \left| \frac{Y_1 + \dots + Y_n}{n^{1/\gamma}} \right|^\alpha \right)_{n \ge 1} \quad (3.27)
$$
is uniformly integrable and hence, by conditioning on the random walk and using triangle inequality once again (now for the $\alpha$-norm of a random variable), we conclude that
$$
(E|A - B|^\alpha)^{1/\alpha} \le \sum_{j=1}^k |\theta_j + \dots + \theta_k|
$$
$$
\quad \times \left( E \left| f \left( N_{[nt_j]}([a_n x]) - N_{[nt_{j-1}]}([a_n x]) \right) \right. \right.
$$
$$
\quad \times \left. \left. \left( \frac{N_{[nt_j]}([a_n x]) - N_{[nt_{j-1}]}([a_n x])}{na_n^{-1}} \right)^{1/\gamma} \right|^\alpha \right)^{1/\alpha} \quad (3.28)
$$
where $f : \mathbb{N} \cup \{0\} \to \mathbb{R}_+$ is a bounded function such that $\lim_{m\to\infty} f(m) = 0$. Using (2.6) again one can easily notice that both $EA^\alpha$ and $EB^\alpha$ can be bounded by
$$
c_1 E \left( \frac{N_{[nt_k]}([a_n x])}{na_n^{-1}} \right)^{\alpha/\gamma} \quad (3.29)
$$

ECP **23** (2018), paper 66. http://www.imstat.org/ecp/
Page 8/11


---


Random walks in doubly random scenery

for some finite constant $c_1$ independent of $n$. Thus, to show that $|E(B_n) - E(C_n)|$ goes to zero as $n \to \infty$ it remains to prove that for any $j = 1, \dots, k$
$$
\int_{\mathbb{R}} \left( E\left(f\left(N_{[nt_j]}([a_n x]) - N_{[nt_{j-1}]}([a_n x])\right)^\alpha \right) \right. \\
\left. \times \left( \frac{N_{[nt_j]}([a_n x]) - N_{[nt_{j-1}]}([a_n x])}{na_n^{-1}} \right)^{\alpha/\gamma} \right)^{1/\alpha} \\
\left. \times E\left( \left( \frac{N_{[nt_k]}([a_n x])}{na_n^{-1}} \right)^{\alpha/\gamma} \right)^{(\alpha-1)/\alpha} dx \right. \quad (3.30)
$$
converges to 0 as $n \to \infty$. The integrand in (3.30) is bounded by the function
$$
x \mapsto c_2 E\left( \left( \frac{N_{[nt_k]}([a_n x])}{na_n^{-1}} \right)^{\alpha/\gamma} \right), \quad (3.31)
$$
for some constant $c_2$ independent of $n$. It follows from the proof of Lemma 6 in [4] that for any $K > 0$ and $t > 0$
$$
\int_{|x|>K} \left( \frac{N_{[nt]}([a_n x])}{na_n^{-1}} \right)^{\alpha/\gamma} dx \\
\text{converges in distribution to} \\
\int_{|x|>K} L_t(x)^{\alpha/\gamma} dx \quad (3.32)
$$
where $(L_t(x))_{t \ge 0, x \in \mathbb{R}}$ is a jointly continuous version of local time of a symmetric $\beta$-stable Lévy process. By Lemma 3.3 in [1] the convergence holds also in $L^1(\Omega)$. Since the expected value of (3.32) converges to 0 as $K \to \infty$ (see Lemma 2.1 in [1]), we see that by choosing $K$ large enough,
$$
\int_{|x|>K} E\left( \left( \frac{N_{[nt_k]}([a_n x])}{na_n^{-1}} \right)^{\alpha/\gamma} \right) dx \quad (3.33)
$$
can be made arbitrarily small for all $n$ large enough. Thus it remains to show that for any $K > 0$
$$
\int_{|x|\le K} \left( E\left(f\left(N_{[nt_j]}([a_n x]) - N_{[nt_{j-1}]}([a_n x])\right)^\alpha \right) \right. \\
\left. \times \left( \frac{N_{[nt_j]}([a_n x]) - N_{[nt_{j-1}]}([a_n x])}{na_n^{-1}} \right)^{\alpha/\gamma} \right)^{1/\alpha} \\
\left. \times E\left( \left( \frac{N_{[nt_k]}([a_n x])}{na_n^{-1}} \right)^{\alpha/\gamma} \right)^{(\alpha-1)/\alpha} dx \right. \quad (3.34)
$$
converges to zero as $n \to \infty$. This is relatively easy and we will only sketch the idea. Fix any $r > 0$ and $j = 1, \dots, k$. The integral in (3.34) can be written as a sum of two integrals $I_1, I_2$ depending on whether
$$
\frac{N_{[nt_j]}([a_n x]) - N_{[nt_{j-1}]}([a_n x])}{na_n^{-1}} \quad (3.35)
$$
is greater than $r$ or not. In the first case, taking $n$ sufficiently large, the integrand can be bounded by an arbitrarily small constant (in this case $N_{[nt_j]}([a_n x]) - N_{[nt_{j-1}]}([a_n x])$ must be large since $na_n^{-1} \to \infty$). In the second case we simply bound the integrand by
$$
r^{1/\gamma} \left( \frac{N_{[nt_k]}([a_n x])}{na_n^{-1}} \right)^{(\alpha-1)/\gamma} \quad (3.36)
$$

ECP 23 (2018), paper 66.                                               http://www.imstat.org/ecp/
Page 9/11


---


Random walks in doubly random scenery

and the corresponding integral (again by Lemma 3.3 in [1]) can be bounded from above by a constant independent of $n$ times $c^{1/\gamma}$. Choosing $r$ small in the first place gives us what was needed. The case $0 \leq \alpha \leq 1$ is very similar and we skip the proof.
Now, by the stability and independence of $Z^{(1)}, \dots, Z^{(k)}$, $E(C_n)$ is equal to

$$
\sum_{x \in \mathbb{Z}} r_n^{-\alpha} \left( \left| \theta_1 + \dots + \theta_k \right|^\gamma N_{[nt_1]}(x) \right. \\
\left. + \left| \theta_2 + \dots + \theta_k \right|^\gamma (N_{[nt_2]}(x) - N_{[nt_1]}(x)) \right. \\
\left. + \dots + \right. \\
\left. + \left| \theta_k \right|^\gamma (N_{[nt_k]}(x) - N_{[nt_{k-1}]}(x)) \right)^{\alpha/\gamma} E(|Y_1|^\alpha). \quad (3.37)
$$

By Lemmas 3.2 and 3.3 in [1], (3.37) converges as $n \to \infty$, to
$$
\int_{\mathbb{R}} E \left| \sum_{j=1}^k \left( |\theta_j + \dots + \theta_k|^\gamma - |\theta_{j+1} + \dots + \theta_k|^\gamma \right) L_{t_j}(x) \right|^\alpha dx, \quad (3.38)
$$
which finishes the proof of (3.7). Now let us turn to (3.8). Define $f_n(x) := c_n(1 - \exp(-c_n^{-1}(x)))$ for $x \in \mathbb{R}, n \in \mathbb{N}$. Then, (3.8) is equivalent to
$$
\lim_{n \to \infty} E f_n(B_n) = E B. \quad (3.39)
$$
We can write, for $\delta > 0$
$$
E f_n(B_n) = E \left( f_n(B_n) \mathbf{1}_{\{|B_n| > c_n^\delta\}} \right) + E \left( f_n(B_n) \mathbf{1}_{\{|B_n| \leq c_n^\delta\}} \right) \quad (3.40) \\
= I_1 + E \left( c_n \left( 1 - \left( 1 - B_n/c_n + O((B_n/c_n)^2) \right) \right) \mathbf{1}_{\{|B_n| \leq c_n^\delta\}} \right),
$$
where (using $|f_n(x)| \leq |x|$ for all $x \in \mathbb{R}$ and $n \in \mathbb{N}$)
$$
|I_2(x)| \leq E (|B_n| \mathbf{1}_{\{|B_n| > c_n^\delta\}}), \quad (3.41)
$$
which converges to 0 as $n \to \infty$ by the uniform integrability of $(B_n)_{n \geq 1}$. Using this, and taking $\delta < \frac{1}{2}$ we see that (again by the uniform integrability of $(B_n)_{n \geq 1}$) (3.39) holds. $\square$

# A Appendix
Proof of Lemma 2.1. Take any $\kappa > 1$ such that $\alpha \kappa < \gamma$. In the proof $c_1, c_2, \dots$ will denote constants independent of $k$ and $\theta$. Since the random variable $Y_1$ is symmetric we may write (using Lemma 1.3 in [5])
$$
m_k(\alpha \kappa) := E \left| \frac{Y_1 + \dots + Y_k}{k^{1/\gamma}} \right|^{\alpha \kappa} = c_1 \int_0^\infty \frac{\phi_k'(-\theta)}{\theta^{\alpha \kappa}} d\theta, \quad (A.1)
$$
for some constant $c_1$ which depends only on $\alpha$ and $\kappa$. Here $\phi_k$ denotes the characteristic function of $(1/k^{1/\gamma})(Y_1 + \dots + Y_k)$. Recall that by $\phi$ we denote the characteristic function of $Y_1$. Since $Y_1$ in the domain of normal attraction of $Z_\gamma$ we conclude (see [2] for proofs) that the function
$$
\theta \mapsto 1 - \phi(\theta) \quad (A.2)
$$
is regularly varying at 0 with exponent $\gamma$ and in particular
$$
\lim_{\theta \to 0} \frac{1 - \phi(\theta)}{|\theta|^\gamma} = c_2, \quad (A.3)
$$

ECP 23 (2018), paper 66. Page 10/11 http://www.imstat.org/ecp/


---

Random walks in doubly random scenery

with $c_2$ being a finite positive constant depending only on $\gamma$. $m_k(\alpha_k)$ can be bounded by
$$
c_1 \int_0^\infty \frac{|\phi'_k(\theta)|}{\theta^{\alpha_k}} d\theta \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad Charles V. John. The Political Constitution of the Kingdom of Hungary. Vienna, 1860.
 [2] J.L. Geluk and L.F.M. Haan. Stable probability distributions and their domains of attraction. 2007.
 [3] Paul Jung, Takashi Owada, and Gennady Samorodnitsky. Functional central limit theorem for negatively dependent heavy-tailed stationary infinitely divisible processes generated by conservative flows. *The Annals of Probability*, (4):2087–2130, 2017. MR-3693958
 [4] Harry Kesten and Frank Spitzer. A limit theorem related to a new class of self similar processes. *Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete*, 50(1):5–25, 1979. MR-0550121
 [5] Muneya Matsui and Zbyněk Pawlas. Fractional absolute moments of heavy tailed distributions. *Braz. J. Probab. Stat.*, 30(2):272–298, 2016. MR-3481104
 [6] Takashi Owada and Gennady Samorodnitsky. Functional central limit theorem for heavy-tailed stationary infinitely divisible processes generated by conservative flows. *The Annals of Probability*, 43(1):240–285, 2015. MR-3298473
 [7] Gennady Samorodnitsky. *Stochastic Processes and Long Range Dependence*. Springer Series in Operations Research and Financial Engineering. Springer International Publishing, first edition, 2016. MR-3561100

**Acknowledgments.** I am grateful to Anna Talarczyk-Noble who helped me clarify my ideas and solve technical difficulties.

ECP **23** (2018), paper 66.
http://www.imstat.org/ecp/
Page 11/11


---

Electronic Journal of Probability
Electronic Communications in Probability

## Advantages of publishing in EJP-ECP

*   Very high standards
*   Free for authors, free for readers
*   Quick publication (no backlog)
*   Secure publication (LOCKSS<sup>1</sup>)
*   Easy interface (EJMS<sup>2</sup>)

## Economical model of EJP-ECP

*   Non profit, sponsored by IMS<sup>3</sup>, BS<sup>4</sup> , ProjectEuclid<sup>5</sup>
*   Purely electronic

## Help keep the journal free and vigorous

*   Donate to the IMS open access fund<sup>6</sup> (click here to donate!)
*   Submit your best articles to EJP-ECP
*   Choose EJP-ECP over for-profit journals

1.  LOCKSS: Lots of Copies Keep Stuff Safe http://www.lockss.org/
2.  EJMS: Electronic Journal Management System http://www.vtex.lt/en/ejms.html
3.  IMS: Institute of Mathematical Statistics http://www.imstat.org/
4.  BS: Bernoulli Society http://www.bernoulli-society.org/
5.  Project Euclid: https://projecteuclid.org/
6.  IMS Open Access Fund: http://www.imstat.org/publications/open.htm