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
\text{z.z.: } (a_n)_{n \in \mathbb{N}} \text{ ist monoton fallend}
$$

# Beweis
$$
\begin{gather*}
a_n \text{ monoton fallend} \iff a_n \ge a_{n+1}
\end{gather*}
$$

$$
\begin{align*}
	&&
	a_n &\ge a_{n+1} \\

	&\iff&
	a_n &\ge \frac{1}{2}(a_n+\frac{x_0}{a_n}) \\

	&\iff&
	2 \cdot a_n &\ge a_n+\frac{x_0}{a_n} \\

	&\iff&
	a_n &\ge \frac{x_0}{a_n} \\

	&\iff&
	a_n^2 &\ge x_0 \\

	&\iff&
	a_n &\ge \sqrt{x_0} \\
	
	&\impliedby&
	a_n &> \sqrt{x_0} \text{ bewiesen in (3a) } \blacksquare \\
\end{align*}
$$
