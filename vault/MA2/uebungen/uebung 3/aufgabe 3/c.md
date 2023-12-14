$$
a_{n+1} := \frac{1}{2}\big(
	a_n+\frac{x_0}{a_n}
\big), n \in \mathbb{N}, x_0 \ge 0
$$

$$
a_1 > \sqrt{x_0}
$$
# Behauptung
$$
\text{z.z.: } \lim_{n \to \infty} a_n = \lim_{n \to \infty} \sqrt{x_0}
$$

# Beweis
$$
\begin{align*}
	\lim_{n \to \infty} a_n &= \lim_{n \to \infty} a_{n+1} \\

	&=\lim_{n \to \infty} \frac{1}{2}(a_n+\frac{x_0}{a_n}) \\
\end{align*}
$$

$$
\begin{align*}
	a &= \lim_{n \to \infty} \frac{1}{2}(a_n+\frac{x_0}{a_n}) \\

	2a &= \lim_{n \to \infty} a_n+\frac{x_0}{a_n} \\
\end{align*}
$$
