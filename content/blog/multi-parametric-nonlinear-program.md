These notes collect definitions and sensitivity results for multi-parametric nonlinear programs, with emphasis on optimal-value continuity, convexity, differential stability, and directional differentiability of local solutions.

## The Problem

We begin with the abstract parametric optimization problem $\color{blue}{P(\epsilon)}$: $$\begin{aligned}
        \min_{x} ~& f(x,\epsilon),\\
        \mathrm{s.t.} ~& x \in R(\epsilon),
    \end{aligned}$$ where $\epsilon \in T \subset \mathbb{R}^r$, $R:\epsilon \mapsto 2^{\mathbb{R}^n}$.

$\color{blue}{P_1(\epsilon)}$: $$\begin{aligned}
        \min_{x} ~& f(x,\epsilon),\\
        \mathrm{s.t.} ~& x \in R(\epsilon) := {\color{red} \{x\in M:g(x,\epsilon) \leq 0, h(x,\epsilon) = 0\}},
    \end{aligned}$$ where $M \subset \mathbb{R}^n$, $g:\mathbb{R}^n \times T \to \mathbb{R}^p$, and $h: \mathbb{R}^n \times T \to \mathbb{E}^q$.

$\color{blue}{P_0(\epsilon)}$: $$\begin{aligned}
        \min_{x} ~& f(x,\epsilon),\\
        \mathrm{s.t.} ~& x \in M,
    \end{aligned}$$

$$
    (\mathrm{VI}(\epsilon)): \quad \begin{cases}
        &\text{Find $x^\star \in K(\epsilon)$ such that:}\\
        &F(x^\star,\epsilon)^\top (x-x^\star) \geq 0, \forall x \in K(\epsilon).
    \end{cases}
$$
## Optimality and Regularity Conditions in (NLP)

Consider the nonlinear program
$$
        (\mathrm{NLP}): \quad \begin{cases}
            &\min_{x \in \mathbb{R}^n} ~ f(x),\\
            &\mathrm{s.t.} ~ \begin{aligned}
                &g_i(x) \leq 0, i \in [m],\\
                &h_j(x) = 0, j \in [p],
            \end{aligned}
        \end{cases}
$$ where $f,g_i,h_j: \mathbb{R}^n \to \mathbb{R}$. It is assumed in this section that $f$, every $g_i$ and every $h_j$ are twice continuously differentiable around $$
        x^0 \in K = \{x\in \mathbb{R}^n: g_i(x) \leq 0, i \in [m]; h_j(x) = 0, j \in [p]\}.
$$ The *Lagrangian function* associated with (NLP) is defined as: $$
        \mathcal{L}(x,u,w) := f(x)+\sum_{i \in [m]} u_i g_i(x) + \sum_{j \in [p]} w_j h_j(x).
$$

Let $x^0 \in K$ be a local minimum for (NLP) and let an appropriate constraint qualification (to be stipulated) hold at $x^0$: Then, the Karush-Kuhn-Tucker (KKT) conditions hold at $x^0$; i. e. there exist Lagrange-Kuhn-Tucker multiplier vectors $u_0$ and $w_0$ such that: $$
            (\mathrm{KKT}) \quad \begin{cases}
                & \nabla_{x} \mathcal{L}(x^0,u^0,w^0) = 0,\\
                & u_i^0 g_i(x^0) = 0, i \in [m],\\
                & u_i^0 \geq 0, i \in [m].
            \end{cases}
$$
Define the set of *active indices of the inequality constraints* at $x^0 \in K$: $$
        I(x^0) := \{i \in [m]: g_i(x^0) = 0\};
$$

and the set of *strictly active inequality constraints* at $x^0 \in K$: $$
    \begin{split}
        I^+(u^0,w^0) = \{i \in I(x^0):&\exists (u^0,w^0) \\
        &\text{ satisfying (KKT), with } u_i^0 > 0\}.
        \end{split}
$$
### Constraint Qualifications

There are many constraint qualifications which assure the validity of the (KKT) conditions. Let $x^0 \in K$,

(a).The Mangasarian-Fromovitz Constraint Qualification (MFCQ) holds at $x^0$ if (i). $\nabla h_j(x^0), j \in [p]$ are linearly independent, and (ii). $\exists z$ such that $\nabla g_i(x^0) z < 0, \forall i \in I(x^0)$, and $\nabla h_j(x^0)z = 0, \forall j \in [p]$.

Applying a theorem of the alternative (see, e. g., Mangasarian (1969)), the equivalent dual form of (MFCQ) states that: zero is the unique solution of the relations $$
        \sum_{i\in I(x^0)}u_i \nabla g_i(x^0) + \sum_{j \in [p]} w_j \nabla h_j(x^0) = 0, u_i \geq 0, \forall i \in I(x^0).
$$

(b). The Linear Independence Constraint Qualification (LICQ) holds at $x^0$ if the vectors $$
        \{\nabla g_i(x^0), i \in I(x^0); \nabla h_j(x^0), j \in [p]\}
$$ are linearly independent.

(c). The Strict Mangasarian-Fromovitz Constraint Qualifications (SMFCQ) holds at $x^0$ if: (i). The gradients $\{\nabla g_i(x^0), i \in I^+(u^0,w^0); \nabla h_j(x^0), j \in [p]\}$ are linearly independent, and (ii). $\exists z$ such that $\nabla g_i(x^0) z < 0,\forall i \in \underbrace{I(x^0) \backslash I^+(u^0,w^0)}_{\text{binding but not strictly active}}$, $\nabla g_i(x^0) z = 0, \forall i \in I^+(u^0,w^0)$, and $\nabla h_j(x^0) z = 0, j \in [p]$.

(d). The Constant Rank Condition (CR) holds at $x^0$ if for any subset $L \subset I(x^0)$ of active constraints, the family $$
        \nabla g_i(x), i \in L; \nabla h_j(x), j \in [p]
$$ remains of constant rank near the point $x^0$.

(e). The Weak Constant Rank Condition (WCR) holds at $x^0$ if for any subset $L \subset I^+(u^0,w^0)$ of strictly active constraints, the family $$
        \nabla g_i(x), i \in L; \nabla h_j(x), j \in [p]
$$ remains of constant rank near the point $x^0$.

The following implications hold.

(i). (LI) $\Rightarrow$ (SMFCQ) $\Leftrightarrow$ Uniqueness of (KKT) multipliers $\Rightarrow$ (MFCQ) + (WCR),\
(ii). (LI) $\Rightarrow$ (MFCQ) + (CR) $\Rightarrow$ (MFCQ) + (WCR),\
(iii). (CR) $\Rightarrow$ (WCR),\
(iv). (SMFCQ) $\nRightarrow$ (CR); (CR) $\nRightarrow$ (MFCQ).
The next theorem states the classical second order necessary conditions for local optimality in problem (NLP). These conditions are essentially due to McCormick (1967, 1976); see also Fiacco and McCormick (1968).

 Suppose that $x^0$ is a local solution of (NLP) and that the (LI) conditions hold at $x^0$: Then, the (KKT) conditions hold at $x^0$ with associated unique multiplier vectors $u^0$ and $w^0$; and the additional Second Order Necessary Conditions (SONC) hold at $x^0$: $$
            z^\top \nabla_x^2 \mathcal{L}(x^0,u^0,w^0) z \geq 0,\quad \forall z \in Z(x^0),
$$ where $Z(x^0)$ is the so-called *critical cone* or *cone of critical directions*, defined as follows: $$
        \begin{split}
            Z(x^0) := \left\{z \in \mathbb{R}^n: \begin{aligned}
                & \nabla g_i(x^0) z \leq 0, i \in I(x^0),\\
                & \nabla g_i(x^0) z = 0, i \in I(x^0) \text{ such that } u^0_i > 0,\\
                & \nabla h_j(x^0) z = 0, j \in [p].
            \end{aligned}\right\}
        \end{split}
$$
By strengthening (SONC) one obtains the following standard second order sufficient conditions for local strict optimality, conditions due to Pennisi (1953), McCormick (1967) and Fiacco and McCormick (1968).

Suppose that the (KKT) conditions hold at $x^0 \in K$ for (NLP) with multipliers vectors $u^0$ and $w^0$; and that the following additional Second Order Sufficient Conditions (SOSC) hold at $x^0$: $$
            z^\top \nabla_x^2 \mathcal{L}(x^0,u^0,w^0) z > 0, \forall 0 \neq z \in Z(x^0).
$$ Then, $x^0$ is a strict local minimum for (NLP), i. e. $f(x^0) < f(x)$ for all feasible $x$ in some neighborhood of $x^0$, $x \neq x^0$.
- Han and Mangasarian (1979) noted that if the (KKT) conditions are verified at $x^0 \in K$; the restrictions on $z$ are equivalent to: $z\neq 0$; $\nabla f(x^0)z = 0; \nabla g_i(x^0)z \leq 0; \forall i \in I(x^0);$ and $\nabla h_j(x^0)z = 0$ for every $j = [p]$.

- Robinson (1982) pointed out that the sufficient conditions of Theorem thm:second-order-sufficient do not assure that $x^0$ is an *isolated* (i. e. locally unique) local minimum for (NLP), as indicated by Fiacco and McCormick (1968). See also Fiacco (1983a). Robinson (1982) provides the following counterexample in $\mathbb{R}$:

Minimize $f(x) = \frac{1}{2}x^2$; $x\in\mathbb{R}$, subject to $h_1(x) = x^6 \sin(\frac{1}{x}) = 0$; where $h_1(0) = 0$ by definition. One can verify that the conditions of Theorem thm:second-order-sufficient are verified at $x^0 = 0$: Moreover, every point of the set $$
        \{(n\pi)^{-1}, n=\pm 1, \pm 2,...\},
$$ is an isolated feasible point, and therefore also a local minimum. Thus $x^0 = 0$ is not an isolated local minimum.
Other second order sufficient optimality conditions for (NLP), used in the literature, are the following ones,

The Strong Second Order Sufficient Conditions (SSOSC) hold at $x^0 \in K$ with multipliers ($u^0,w^0$) if for all $z \neq 0$ such that $\nabla g_i(x^0) z = 0, \forall i, u_i^0 > 0$ and $\nabla h_j(x^0)z = 0, j \in [p]$.

The General Second Order Sufficient Conditions (GSOSC) hold at $x^0 \in K$ if (SOSC) hold at $x^0 \in K$ with $(u^0,w^0)$ for every $(u^0,w^0)$ satisfying (KKT).

The General Strong Second Order Sufficient Conditions (GSSOSC) hold at $x^0 \in K$ if (SSOSC) hold at $x^0 \in K$ with $(u^0,w^0)$ for every $(u^0,w^0)$ satisfying (KKT).

The following conditions, due to Robinson (1982), are sufficient for $x^0 \in K$ to be an *isolated* local minimum for problem (NLP).

 Let $x^0 \in K$ and suppose that the (KKT) conditions hold at $x^0$ with some $u^0$ and $w^0$. Suppose that the Mangasarian-Fromovitz constraint qualification holds at $x^0$; moreover, assume that the General Second Order Sufficient Conditions hold at $x^0$. Then $x^0$ is an isolated local minimum of (NLP), i. e. there exists a neighborhood of $x^0$ such that $x^0$ is the only local minimum of (NLP) in that neighborhood.
**Remark 1**. Note that if the (LICQ) or also the (SMFCQ) is substituted for (MFCQ) in Theorem thm:isolated_minimum, then (GSOSC) coincides with (SOSC), since the multipliers vectors $u^0$ and $w^0$ are unique, under the said constraint qualifications.
## Basic Sensitivity Results under Second Order Differentiability for (NLP($\epsilon$))

## Preliminaries

This section collects two preliminary notions.

A function $\phi: \mathbb{R}^r \to \mathbb{R}^l$ is said to be *locally Lipschitz* near $\bar z \in \mathbb{R}^r$ if there is a neighborhood $N(\bar z)$ of $\bar z$ and a $L > 0$ such that $$
            \|\phi(z_1)-\phi(z_2)\| \leq L\|z_1-z_2\|, \quad \forall z_1,z_2 \in N(\bar z).
$$
The *directional derivative* of $\phi$ at the point $\bar z$ in the direction $v \in \mathbb{R}^r$ is defined as $$
            D\phi(\bar z;v) := \lim_{\beta \to 0^+} \frac{1}{\beta} \left[ \phi(\bar z + \beta v) - \phi(\bar z) \right].
$$
If the above limit exists for every $v \in \mathbb{R}^r$, we say $\phi$ is *directionally differentiable* at $\bar z$. Directionally differentiability does not imply differentiability.
## Continuity

Continuity In this section we will consider conditions under which the optimal-value function $f^\star$ and the optimal solution map $S$ are continuous. We begin with definitions of continuity of a point-to-set map. Let $T$ be a metric space, $\psi:T \to 2^{\mathbb{R}^n}$, and $\bar \epsilon \in T$.

A point-to-set function $\psi$ is said to be *upper (lower) semi-continuous* at $\bar \epsilon$ if for each open set $O \subset \mathbb{R}^n$ satisfying $\psi(\bar \epsilon) \in O$ ($\psi(\bar \epsilon) \cap O \neq \emptyset$), there exists a neighborhood $N(\bar \epsilon)$ such that $\psi(\epsilon) \subset O$ ($\psi(\epsilon) \cap O \neq \emptyset$), for all $\epsilon \in N(\bar \epsilon)$.
A point-to-set function $\psi$ is said to be *closed* at $\bar \epsilon$ if $\epsilon_n \in T, \epsilon_n \to \bar \epsilon, x_n \in \psi(\epsilon_n)$, and $x_n \to \bar x$ imply $\bar x \in \psi(\bar \epsilon)$.
A point-to-set function $\psi$ is said to be *open* at $\bar \epsilon$ if $\epsilon_n \in T, \epsilon_n \to \bar \epsilon$, and $\bar x \in \psi(\bar \epsilon)$ imply that $\exists m$ and $\{x_n\}$ such that $x_n \in \psi(\epsilon_n)$ for all $n \geq m$ and $x_n \to \bar x$.
A point-to-set function $\psi$ is said to be *uniformly compact* near $\bar \epsilon$ if the set $\cup_{\epsilon \in N(\bar \epsilon)} \psi(\epsilon)$ is bounded for some neighborhood $N(\bar \epsilon)$.
Let $\{A_n\}$ be a sequence of subsets of $\mathbb{R}^n$. The *inner limit* of $\{A_n\}$ is defined as $$
            \underline{\lim}_{n\to\infty} A_n := \left\{\begin{aligned}
                x \in \mathbb{R}^n: &\exists m, \{x_n\} \text{ such that } x_n \in A_n, \\
                &\forall n \geq m, x_n \to x
            \end{aligned}\right\}.
$$
Hogan showed that (a) lower semicontinuity and openness at a point are equivalent, and (b) if $\psi$ is uniformly compact near $\bar \epsilon$, then $\psi$ is closed if and only if $\psi(\bar \epsilon)$ is compact and $\psi$ is upper semicontinuous at $\bar \epsilon$.

$\psi$ is closed (open) at $\bar \epsilon$ if and only if $\underline{\lim}_{n \to \infty} \psi(\epsilon_n) \subset (\supset) \psi(\bar \epsilon)$, for any $\{\epsilon_n\} \subset T$ such that $\epsilon_n \to \bar \epsilon$.
$\psi$ is *continuous at $\bar \epsilon$* if it is upper semicontinuous and lower semicontinuous at $\bar \epsilon$.
For $P(\epsilon)$, we have

(a). If $R$ is lower semicontinuous at $\bar \epsilon$, and $f$ is usc on $R(\bar \epsilon) \times \{\bar \epsilon\}$, then $f^\star$ is usc at $\bar \epsilon$.

(b). If $R$ is upper semicontinuous at $\bar \epsilon$, $R(\bar \epsilon)$ is compact, and $f$ is lsc on $R(\bar \epsilon) \times \{\bar \epsilon\}$, then $f^\star$ is lsc at $\bar \epsilon$.
For $P(\epsilon)$, if

(1). $f$ is continuous on $R(\bar \epsilon) \times \{\bar \epsilon\}$;

(2). $R$ is closed and open (i.e. lower semi-continuous) at $\bar \epsilon$;

(3). $S(\bar \epsilon)$ is nonempty and a singleton;

(4). $S$ is uniformly compact near $\bar \epsilon$;

then $S$ is closed and open (under (4), $S$ is continuous) at $\bar \epsilon$.
Note that (1) openness is equivalent to lower semi-continuity, and (2) uniform compactness $+$ closedness imply upper semi-continuity. Therefore, $S$ is continuous.

For $P(\epsilon)$, if

(1). $f$ is quasi-convex in $x$ for every fixed $\epsilon \in T$ and continuous on $\mathbb{R}^n \times T$;

(2). $R$ is closed at every $\epsilon$ near $\bar \epsilon$ and open at $\bar \epsilon$.

(3). $R$ is convex-valued near $\bar \epsilon$ (i.e. $R(\epsilon)$ is convex near for $\epsilon$ near $\bar \epsilon$);

then $S(\epsilon)$ is nonempty and uniformly compact near $\bar \epsilon$ if and only if $S(\bar \epsilon)$ is nonempty and compact.
For $P(\epsilon)$, if

(1). $f(x,\epsilon) = \max\{f_1(x,\epsilon),f_2(\epsilon)\}$, where $f_1$ is continuous on $\mathbb{R}^n \times T$ and strictly quasi-convex in $x$ for each fixed $\epsilon \in T$, and $f_2$ is continuous on $T$;

(2). $R$ is nonempty, convex-valued, and continuous on $T$;

then $S$ is continuous and convex-valued on $T$.
In order to specialize these general theorems to the concrete nonlinear (or linear) programming problem $P_1(\epsilon)$, we need to know the conditions that guarantee the continuity of an inequality and/or equality constraint map $R$ of $P_1(\epsilon)$. The following two theorems are concerned with the constraint map: $$

        R(\epsilon) := \{x \in M: g(x) \leq \epsilon\},
$$ where $M \subset \mathbb{R}^n, g: \mathbb{R}^n \to \mathbb{R}^p$, and $\epsilon \in \mathbb{R}^p$.

For the map $R$ of eq:constraint_map, suppose that $M = \mathbb{R}^n$, $g$ is continuous on $\mathbb{R}^n$, and that $R(\bar \epsilon)$ is compact. Then

(1). $R$ is upper semi-continuous at $\bar \epsilon$ if and only if there exists a vector $\epsilon' > \bar \epsilon$ such that $R(\epsilon')$ is a compact set.

(2). if the set $R^0(\bar \epsilon) := \{x\in\mathbb{R}^n:g(x)<\bar \epsilon\}$ is nonempty, then $R$ is lower semi-continuous at $\bar \epsilon$ if and only if $\overline{R^0(\bar \epsilon)} = R(\bar \epsilon)$, namely, $$\overline{\{x\in\mathbb{R}^n:g(x)<\bar\epsilon\}} = \overline{R^0(\bar \epsilon)} = R(\bar \epsilon) = \{x\in\mathbb{R}^n:g(x)\leq\bar\epsilon\}$$
Note that in (1) of the above theorem, the compactness of $R(\bar \epsilon)$ and the upper semi-continuity of $R$ at $\bar \epsilon$ imply the closedness of $R$ at $\bar \epsilon$.

For the map $R$ of eq:constraint_map, suppose that $M$ is compact and convex, and that $g_i$ are lsc and strictly convex on $M$. Then $R$ is closed (i.e. upper semi-continuous, under the assumptions) and open (i.e. lower semi-continuous) at every $\epsilon \in \mathrm{dom}(R)$ relative to $\mathrm{dom}(R)$, where $\mathrm{dom}(R):=\{\epsilon \in \mathbb{R}^p:R(\epsilon) \neq \emptyset\}$.
The next theorem, dut to Dantzig et al., is concerned with a linear inequality (and equality) constraint: $$
        R(A,b) := \{x \in M: Ax \geq b\},
$$ where $M \subset \mathbb{R}^n$, $A$ is a $p \times n$ real matrix, and $b \in \mathbb{R}^p$.

Let $\bar A$ be a $p \times n$ real matrix consisting of $p$ row vectors $\bar a_i^\top \in \mathbb{R}^n, i = 1,...,p$, $\bar b \in \mathbb{R}^p$, and $$I := \{i = 1,...,p:\bar a_i^\top x = \bar b_i, \forall x \in R(\bar A, \bar b)\}.$$ If the matrix $\bar A_I$, whose rows are $\bar a_i^\top, i \in I$, has full rank, then, for every sequence $\{(A_n,b_n)\}$ converging to $(\bar A, \bar b)$, either $$\underline{\lim}_{n\to\infty} R(A_n,b_n) = R(\bar A, \bar b),$$ or $R(A_n,b_n)$ is empty for infinitely many $n$, and consequently, $R$ is closed and open at $(\bar A, \bar b)$ relative to $\mathrm{dom}(R)$ if $(\bar A, \bar b) \in \mathrm{dom}(R)$.
We next consider nonlinear inequality constraints. Let $$

        R(\epsilon) := \{x \in M:g(x,\epsilon) \leq 0\}.
$$

For the map $R$ of eq:nonlinear_inequality_constraint_map, suppose that $M$ is closed, $g$ is continuous on $M \times \{\bar \epsilon\}$, and that $$\overline{\{x\in M:g(x,\bar \epsilon) < 0\}} = R(\bar \epsilon),$$ then $R$ is closed and open at $\bar \epsilon$.
For the map $R$ of eq:nonlinear_inequality_constraint_map, suppose that $M$ is compact and convex, $g$ is continuous on $M \times T$, and that $g_i$ are strictly convex on $M$ for each fixed $\epsilon \in T$. Then $R$ is closed and open at every $\epsilon \in \mathrm{dom}(R)$ relative to $\mathrm{dom}(R)$.
By using implicit function theorem, Aiyoshi extends Theorem 2.8 to the inequality-equality constrained case.

Stein-Topkis essentially show that, for $P(\epsilon)$, if $f$ and $R$ are locally Lipschitz (in the sense of Hausdorf distance), then $f^\star$ is locally Lipschitz. For the inequality-equality constrained problem $P_1(\epsilon)$, some **constraint qualifications** (e.g. MFCQ and LICQ) and the uniform compactness of $R$ are sufficient for $f^\star$ to be (locally Lipschitz) continuous.
## Convexity

Convexity of Optimal-value Function Throughout this section it is assumed that $T \subset \mathbb{R}^r$ is nonempty and convex.

A point-to-set map $R:T \to 2^{\mathbb{R}^n}$ is said to be *convex (concave)* on $T$ if for all $\epsilon_1, \epsilon_2 \in T$ and $\lambda \in (0,1)$ $$

            \lambda R(\epsilon_1) + (1-\lambda) R(\epsilon_2) \subset (\supset) R\left( \lambda \epsilon_1 + (1-\lambda)\epsilon_2 \right).
$$
- If in eq:convex_map, the inclusion $\subset$ holds only for all $\epsilon_1 \neq \epsilon_2 \in T$ and $\lambda \in (0,1)$, then $R$ is said to be *essentially convex* on $T$.

- $R$ is said to be *essentially affine* on $T$ if $R$ is both essentially convex and concave on $T$.

For $P(\epsilon)$, suppose that $f$ is jointly convex on $\{(x,\epsilon):x\in R(\epsilon),\epsilon\in T\}$, and that $R$ is essentially convex on $T$. Then $f^\star$ is convex on $T$.
A function $\phi:M \to \mathbb{R}$ is said to be (strictly) quasi-convex on a convex set $M$ if, for all $x_1, x_2 \in M$ and $\lambda \in (0,1)$ $$
            \phi(\lambda x_1 + (1-\lambda)x_2) \leq (<) \min\{\phi(x_1),\phi(x_2)\}.
$$
For $P_1(\epsilon)$, suppose that $g_i$ are jointly quasi-convex on $M \times T$, $h_j$ are jointly affine on $M \times T$, and that $M$ is convex. Then $R$ is convex on $T$.
For $P(\epsilon)$, suppose that $f$ is jointly concave on $\mathbb{R}^n \times T$, and that $R$ is concave on $T$. Then $f^\star$ is concave on $T$.
For $P_0(\epsilon)$, suppose that $f$ is concave in $\epsilon$ on $T$ for all $x \in M$. Then $f^\star$ is concave on $T$.
For $P(\epsilon)$, suppose that $f$ is jointly affine on $\mathbb{R}^n \times T$, $R$ is essentially affine on $T$, and that $T \subset \mathrm{dom}(R)$. Then $f^\star$ is both convex and concave on $T$, and $S$ is essentially affine on $T$.
## Differential Stability of Optimal-value functions

Differential Stability A number of results on the rate of change in $f^\star$ under small perturbations have been obtained by means of the first- and second-order directional derivatives of $f^\star$ in the direction along which the perturbation is made. The first result is due to Danskin.

For $P_0(\epsilon)$, suppose that $T = \mathbb{R}^r$, and that $f$ and $\nabla_{\epsilon} f$ are continuous on $M \times N(\epsilon)$, where $N(\epsilon)$ is a neighborhood of $\epsilon \in \mathbb{R}^r$. Then $f^\star$ is locally Lipschitz near $\epsilon$, directionally differentiable at $\epsilon$, and $$
            Df^\star(\epsilon;v) = \min_{x \in S(\epsilon)} \nabla_{\epsilon} f(x,\epsilon) v.
$$
Another theorem, due to Gauvin-Dubeau and Fiacco, gives lower and upper bounds for the directional derivative of $f^\star$ in $P_1(\epsilon)$. In the sequel, we assume in $P_1(\epsilon)$, $M=\mathbb{R}^n$, and that $f,g,$ and $h$ are continuously differentiable in $(x,\epsilon)$. The Lagrangian and the set of multipliers of $P_1(\epsilon)$ are defined as follows: $$
        \begin{split}
            &L(x,u,w,\epsilon) = f(x,\epsilon) - u^\top g(x,\epsilon) + w^\top h(x,\epsilon),\\
            &K(x,\epsilon) = \left\{(u,w) \in \mathbb{R}^p \times \mathbb{R}^q: 
            \begin{aligned}
            &\nabla_x L(x,u,w,\epsilon) = 0, \\
            &u_i g_i(x,\epsilon) = 0, \\
            &u_i \geq 0, i\in[p]
            \end{aligned}
            \right\}.
        \end{split}
$$

We say that MFCQ holds at $x \in R(\epsilon)$ for $P(\epsilon)$ if

(1). the vectors $\{\nabla_x h_j(x,\epsilon),j\in[p]\}$ are linearly independent;

(2). there exists $z \in \mathbb{R}^n$ such that $$
            \begin{split}
                &\nabla_x g_i(x,\epsilon)z < 0, i \in \mathcal{A}(x,\epsilon)\\
                &\nabla_x h_j(x,\epsilon)z = 0, \forall j \in [q],
            \end{split}
$$ where $\mathcal{A}(x,\epsilon) := \{i \in [p]:g_i(x,\epsilon) = 0\}$.
For $P_1(\epsilon)$, suppose that $M = \mathbb{R}^n$, that $R(\epsilon) \neq \emptyset$ and $R$ is uniformly compact near $\epsilon \in \mathbb{R}^r$, and that (MFCQ) holds at each $x \in S(\epsilon)$. Then $f^\star$ is locally Lipschitz near $\epsilon$, and for any $v \in \mathbb{R}^r$, $$
            \begin{split}
                &\inf_{x \in S(\epsilon)} \min_{(u,w)\in K(x,\epsilon)} \nabla_{\epsilon} L(x,u,w,\epsilon)^\top v \\
                &\leq \liminf_{\beta \to 0^+} \frac{1}{\beta} \left[ f^\star(\epsilon+\beta v) - f^\star(\epsilon) \right]\\
                &\leq \limsup_{\beta \to 0^+} \frac{1}{\beta} \left[ f^\star(\epsilon+\beta v) - f^\star(\epsilon) \right]\\
                &\leq \inf_{x \in S(\epsilon)} \max_{(u,w)\in K(x,\epsilon)} \nabla_{\epsilon} L(x,u,w,\epsilon)^\top v
            \end{split}
$$ Furthermore, if $f$ and $g$ are convex on $\mathbb{R}^n \times \{\epsilon\}$, and if $h$ is affine on $\mathbb{R}^n \times \{\epsilon\}$, then $f^\star$ is directionally differentiable at $\epsilon$, and $$

            Df^\star(\epsilon;v) = \min_{x\in S(\epsilon)} \max_{(u,w)\in K(\epsilon)} \nabla_{\epsilon} L(x,u,w,\epsilon)^\top v,
$$ where, under the assumptions $K(x,\epsilon) = K(\epsilon)$ is constant for $x \in S(\epsilon)$.
There are two immediate consequences of Theorem 4.2. Under stronger CQ than (MFCQ) at $x \in S(\epsilon)$ (e.g. (SMFCQ), or (LICQ)), $K(x,\epsilon)$ reduces to a singleton, say $\{u(x),w(x)\}$, so the directional derivative formula reduces to $$
    Df^\star(\epsilon;v) = \min_{x\in S(\epsilon)} \nabla_{\epsilon} L[x,{\color{red}{u(x)}},{\color{red}{w(x)}},\epsilon]^\top v
$$

Another special case is the jointly convex case: if $f$ and $g$ are jointly convex and $h$ is jointly affine on $\mathbb{R}^n \times \mathbb{R}^r$, then for each $(u,w) \in K(x,\epsilon)$, $\nabla_{\epsilon}L(x,u,w,\epsilon)$ does not depend on $x \in S(\epsilon)$, and hence eq:directional_derivative becomes $$
    Df^\star(\epsilon;v) = \max_{(u,w)\in K(\epsilon)} \nabla_{\epsilon} L(x,u,w,\epsilon)^\top v,
$$ where $x \in S(\epsilon)$. Since in this case, $f^\star$ is convex (since $f$ is jointly convex and $R(\epsilon)$ is convex for all $\epsilon$. See Theorem 3.1). The above equation means that for each $x \in S(\epsilon)$ and $(u,w) \in K(x,\epsilon)$, $\nabla_\epsilon L(x,u,w,\epsilon)$ is a subgradient of $f^\star$ at $\epsilon$.
## Sensitivity Analysis under Second-order Conditions

## Differential Stability of Optimal Solution

Differential Stability of Optimal Solution Assume $x(\epsilon)$ is a local solution to $P_1(\epsilon)$ and let $z(\epsilon) := (\epsilon,x(\epsilon))$. Given $(u,w) \in K(x(\epsilon),\epsilon)$, let $\mathcal{A}_u(\epsilon):=\{i \in [p]:u_i > 0\}$, and $\mathcal{A}^0_u(\epsilon):=[p]-\mathcal{A}_{u}$.

The *critical cone* of the system of constraints $g(x,\epsilon) \leq 0$ and $h(x,\epsilon) = 0$ with respect to $u$ is $$
            \begin{split}
            \mathcal{K}_u(\epsilon) := \{v \in \mathbb{R}^{r+n}:&\forall i \in \mathcal{A}^0_{u}(\epsilon),\nabla g_i(z(\epsilon))v \leq 0 \\
            &\forall i \in \mathcal{A}_{u}(\epsilon),\nabla g_i(z(\epsilon))v = 0,\\
            &\forall j \in [q], \nabla h_j(z(\epsilon)) = 0\}.
            \end{split}
$$
The critical cone at $z(\epsilon)$ with respect to $u$ in the direction of $d \in \mathbb{R}^r$ is $$\mathcal{K}_{u}(\epsilon;d) := \{v \in \mathbb{R}^n:(d,v) \in \mathcal{K}_{u}(\epsilon)\}.$$

For each $(u,w) \in K(x(\bar \epsilon),\bar \epsilon)$, and each $v \neq 0$ such that $\nabla_x g_i(z(\bar \epsilon))v = 0, \forall i \in \mathcal{A}_u(\bar \epsilon)$ and $\nabla_x h(z(\bar \epsilon))v = 0$, $$
        v^\top \nabla^2_{xx} L(z(\bar \epsilon),u,w) v > 0.
$$
Differential Stability of Optimal Solution

For $P_1(\epsilon)$, assume that (1) $f$, $g$, and $h$ are $C^2$ near $z(\bar \epsilon)$; (2) MFCQ holds at $x(\bar \epsilon) \in R(\bar \epsilon)$; and (3) (GSSOSC) holds at $x(\bar \epsilon)$. There exist neighborhoods $U$ of $\bar \epsilon$ and $V$ of $x(\bar \epsilon)$, and a mapping $x(\cdot)$ from $U$ to $V$ such that

(1). $x(\cdot)$ is continuous and, for each $\epsilon \in U$, $x(\epsilon)$ is the unique local solution of $P_1(\epsilon)$ in $V$; and

(2). $x(\cdot)$ is directionally differentiable; indeed for each $\epsilon \in U$, $d \in \mathbb{R}^n$ there exists $(u,w) \in K(x(\epsilon),\epsilon)$ such that $Dx(\epsilon;d)$ is the unique solution to the convex quadratic program $\mathrm{QP}_{u,w}(\epsilon;d)$ $$\begin{aligned}
                \min_v ~& \frac{1}{2}v^\top \nabla^2_{xx} L(z(\epsilon),u,w)v + d^\top \nabla^2_{x\epsilon}L(z(\epsilon),u,w)v,\\
                \mathrm{s.t.} ~& v \in \mathcal{K}_u (\epsilon;d).
            \end{aligned}$$
Unfortunately, $Dx(\epsilon;d)$ is not given in a constructive way by part (2) of the above theorem since we do not know which $(u,w) \in K(x(\epsilon),\epsilon)$ to use. However, if *the constant rank constraint qualification* (CRCQ) is assumed, $Dx(\epsilon;d)$ is the solution to $\mathrm{QP}_{u,w}(\epsilon;d)$ for some extreme $(u,w) \in K(x(\epsilon),\epsilon)$.

### Constant Rank Constraint Qualification

We say that (CRCQ) holds at $x(\bar \epsilon)$ if there exists a neighborhood $W$ of $z(\bar \epsilon)$ such that for any subsets $I$ of $\mathcal{A}(x(\bar \epsilon),\bar \epsilon) := \{i \in [p]:g_i(x(\bar \epsilon),\bar\epsilon) = 0\}$ and $J \subset [q]$, the family of gradients $\{\nabla_x g_i(x(\epsilon),\epsilon): i \in I\}$ and $\{\nabla_x h_j(x(\epsilon),\epsilon),j\in J\}$ has the same rank for all $z \in W$.
We can choose $(u,w)$ specially, namely as a member of $$

        \mathcal{S}(\epsilon;d):=\mathop{\mathrm{arg\,max}}_{(u,w)\in K(z(\epsilon))} u^\top \nabla_\epsilon g(z(\epsilon))d + w^\top \nabla_\epsilon h(z(\epsilon))d.
$$ Note that $\mathcal{S}(\epsilon;d)$ is nonempty because $K(z(\epsilon))$ is nonempty and compact (by MFCQ); and that linear programming methods provide a practical way to calculate an element of $\mathcal{S}(\epsilon;d)$. Furthermore for fixed d, Theorem 1(2) holds when assumption (GSSOSC) is weakened to only include those $u$ corresponding to some $(u,w) \in \mathcal{S}(\epsilon;d)$.

### Piecewise Smoothness

A function is said to be $\mathrm{PC}^1$ near $\bar \epsilon$ if it is continuous and there is a finite family of $C^1$ functions $y^1(\epsilon),...,y^N(\epsilon)$ defined on a neighborhood of $\bar \epsilon$ such that $y(\epsilon) \in \{y^1(\epsilon),...,y^N(\epsilon)\}$ for each $x$ in that neighborhood. The $\mathrm{PC}^1$ property is a kind of piecewise smoothness.
Under the conditions in Theorem 1 and furthermore assume (CRCQ). Then for some open neighborhood $U$ of $x(\bar \epsilon)$ and $V$ of $\bar \epsilon$, there is a function $x(\cdot)$ from $U$ to $V$ such that in addition to conclusions in Theorem 1 (1),

(1). $x(\cdot)$ is $\mathrm{PC}^1$, hence locally Lipschitz and $B$-differentiable.

(2). $Dx(\epsilon;\cdot)$ is piece-wise linear such that for each $\epsilon \in U, d \in \mathbb{R}^n$, and $(u,w) \in \mathcal{S}(\epsilon;d)$, $Dx(\epsilon;d)$ is the unique solution to the convex quadratic program $\mathrm{QP}_{u,w}(\epsilon;d)$.
We mention that each multiplier $(u,w) \in \mathcal{S}(\epsilon;d)$ is a vector of marginal costs or shadow prices of constraint perturbations. To explain this, consider $$
        \begin{split}
            Df^\star(\epsilon;d) = \nabla_\epsilon f(z(\epsilon))^\top d + \nabla_x f(z(\epsilon))^\top Dx(\epsilon;d),
        \end{split}
$$ By examing the KKT conditions of $\mathrm{QP}_{u,w}(\epsilon;d)$, it is easy to see that the second summand is the optimal value of the LP eq:finding_suitable_multipliers: $$
        \begin{split}
        \forall (u,w) &\in \mathcal{S}(\epsilon;d), 
        \\&\nabla_x f(z(\epsilon))^\top Dx(\epsilon;d) = u^\top \nabla_\epsilon g(z(\epsilon))d + w^\top \nabla_\epsilon h(z(\epsilon))d.
        \end{split}
$$ Since $(\nabla_\epsilon g(z(\epsilon))d,\nabla_\epsilon h(z(\epsilon))ds)$ is the marginal perturbation of the constraints, it follows that each $(u,w) \in \mathcal{S}(\epsilon;d)$ is the marginal cost of such perturbations.

$\mathcal{K}_u(\epsilon;d)$ is nonempty if and only if $(u,w) \in \mathcal{S}(\epsilon;d)$.
Assume the hypothesis of Theorem 2, let $U,V$ and $x(\cdot): U \to V$ be given by the theorem.

(1). Let $\epsilon \in U, d \in \mathbb{R}^n$, and $(u,w) \in K(x(\epsilon),\epsilon)$. If $$
            \mathrm{Range}\begin{bmatrix}
                \nabla_x g(z(\epsilon))\\
                \nabla_x h(z(\epsilon))
            \end{bmatrix}
            \supset
            \mathrm{Range}\begin{bmatrix}
                \nabla_\epsilon g(z(\epsilon))\\
                \nabla_\epsilon h(z(\epsilon))
            \end{bmatrix},
$$ then $Dx(\epsilon;d)$ is the unique solution to $\mathrm{QP}_{u,w}(\epsilon;d)$.

\(2\) If $g$ and $h$ do not depend on $\epsilon$, then for each $\epsilon \in U, d \in \mathbb{R}^n$, and $(u,w) \in K(x(\epsilon),\epsilon)$, $Dx(\epsilon;d)$ is the unique solution to $\mathrm{QP}_{u,w}(\epsilon;d)$.
*Proof.* Note part (2) follows from part (1). To prove part (1), use the fact that the condition on ranges implies $\mathcal{K}_u(\epsilon;d) \neq \emptyset$ for the chosen $x, d$, and $(u,w)$.
### Monotonicity Note

Rewrite the statement as: $$
    \begin{split}
        \mathbf{a^\top [H(x)-H(y)]} < 0 \quad \Leftrightarrow \quad & \mathbf{a^\top [x-y]} < 0, \\
        &\forall \mathbf{a} \in \mathbb{R}_{++}^2, \mathbf{x,y} \in \mathbb{R}^2,
    \end{split}
$$ where $\mathbf{a} := [a_1,a_2]^\top, \mathbf{x} := [x_1,x_2]^\top$, $\mathbf{y}:=[y_1,y_2]^\top$, and $\mathbf{H(x)}:=[h(x_1),h(x_2)]^\top:\mathbb{R}^2\mapsto \mathbb{R}^2$.

Let $\mathbf{x},\mathbf{y}$ be fixed. For any $\mathbf{a}\in \mathbb{R}^2_{++}$, it is clear that either $$
            \underbrace{\begin{bmatrix}
                \mathbf{(H(x)-H(y))^\top}\\
                \mathbf{(x-y)^\top}
            \end{bmatrix}}_{\in \mathbb{R}^{2\times 2}}
            \mathbf{a}<\begin{bmatrix}
0\\
0   
\end{bmatrix},
$$ or $$

            \begin{bmatrix}
                \mathbf{(H(x)-H(y))^\top}\\
                \mathbf{(x-y)^\top}
            \end{bmatrix}
            \mathbf{a}\geq\begin{bmatrix}
0\\
0   
\end{bmatrix},
$$ holds. Equation (42) implies $\mathbf{H(x)-H(y) \leq 0}$ and $\mathbf{x-y \leq 0}$. Similarly, Equation eq:geq implies $\mathbf{H(x)-H(y) > 0}$ and $\mathbf{x-y > 0}$. Put them together, we obtain $$
            \left[\mathbf{H(x)-H(y)}\right]^\top (\mathbf{x-y}) \geq 0, \quad \forall \mathbf{x,y} \in \mathbb{R}^2,
$$ which means $\mathbf{H}$ is monotone. If we choose $\mathbf{x}$ and $\mathbf{y}$ to be such that $x_2 = y_2 = 0$, we have $[h(x_1)-h(y_1)] \cdot [x_1-y_1] \geq 0$.

## References

- Anthony V. Fiacco and Yo Ishizuka, "Sensitivity and stability analysis for nonlinear programming," *Annals of Operations Research*, 1990.
- Daniel Ralph and Stephan Dempe, "Directional derivatives of the solution of a parametric nonlinear program," *Mathematical Programming*, 1995.
