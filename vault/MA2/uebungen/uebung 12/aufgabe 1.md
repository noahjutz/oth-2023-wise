# Gegeben

$$
\begin{gather*}
	f(x) = e^x \\
	g(x) = -\frac{x}{2} + 1
\end{gather*}
$$

$$
M = \{ (x, y) |\, 0 \le y \le \min\big(f(x), g(x)\big) \}
$$

# Skizze

![[aufgabe 1 skizze.svg|300]]

# Flächeninhalt

$$
A = \int_{-\infty}^0 e^x \,dx + \int_0^2 -\frac{x}{2}+1 \,dx
$$

$$
\begin{align*}
	\int_{-\infty}^0 e^x \,dx
	&= \lim_{r \to -\infty} \int_r^0 e^x \,dx \\
	&= \lim_{r \to -\infty} \left[ e^x \right]_r^0 \\
	&= \lim_{r \to -\infty} (e^0 - e^r) \\
	&= 1 - \lim_{x \to \infty} \frac{1}{e^x} \\
	&= 1 - 0 \\
	&= 1
\end{align*}
$$

$$
\begin{align*}
	\int_0^2 -\frac{x}{2} + 1 \,dx
	&= \left[
		-\frac{1}{2} \cdot \frac{1}{2}x^2 + x
	\right]_0^2 \\
	&= \left(
		-\frac{1}{4} \cdot 2^2 + 2
	\right) - 0 \\
	&= 1
\end{align*}
$$

$$
A = 1 + 1 = \underline 2
$$
