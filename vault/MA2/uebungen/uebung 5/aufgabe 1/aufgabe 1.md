$$
\begin{align*}
	x &= \sqrt{3} \\
	x^2 &= 3 \\
	x^2 - 3 &= 0
\end{align*}
$$

$$
f(x) = x^2 - 3
$$
# Bisektion

$$
\overline x_n := \frac{a_n+b_n}{2}
$$

$$
[a_{n+1},b_{n+1}] = \left\{
	\begin{align*}
		&[
			a_n, \overline x_n
		]
		& \text{falls } f(\overline x_n) > 0 \\
		&[
			\overline x_n, b_n
		]
		& \text{falls } f(\overline x_n) \le 0
	\end{align*}
\right.
$$

## Folgenglieder

### n = 0

$$
[a_0, b_0] = [0, 3] \qquad  \begin{gather*}
	f(0) = -3 \\
	f(3) = 3
\end{gather*}
$$

### n = 1

$$
\begin{align*}
	f(\overline x_0) &= f\Big(\frac{a_0+b_0}{2}\Big) \\
	&= f\Big(\frac{3}{2}\Big) \\
	&= \Big(\frac{3}{2}\Big)^2 - 3 \\
	&= -\frac{3}{4} \le 0
\end{align*}
$$

$$
\begin{align*}
	\implies [a_1, b_1] &= [\overline x_0, b_0] \\

	&= \left[
		\frac{3}{2}, 3
	\right]
\end{align*}
$$

### n = 2

$$
f(\overline x_1) = f\left(\frac{9}{4}\right) > 0
$$

$$
\begin{align*}
	\implies [a_2, b_2] &= [a_1, \overline x_1] \\
	
	&= \left[
		\frac{3}{2}, \frac{9}{4}
	\right]
\end{align*}
$$

### n = 3

$$
f(\overline x_2) = f\left(\frac{15}{8}\right) > 0
$$

$$
\begin{align*}
	\implies [a_3, b_3] &= [a_2, \overline x_2] \\

	&= \left[
		\frac{3}{2}, \frac{15}{8}
	\right]
\end{align*}
$$

### n = 4

$$
f(\overline x_3) = f\left(\frac{27}{16}\right) \le 0
$$

$$
\begin{align*}
	\implies [a_4, b_4] &= [\overline x_3, b_3] \\

	&= \left[
		\frac{27}{16},\frac{15}{8}
	\right]
\end{align*}
$$

### n = 5

$$
f(\overline x_4) = f\left(\frac{57}{32}\right) > 0
$$

$$
\begin{align*}
	\implies [a_5, b_5] &= [a_4, \overline x_4] \\

	&= \colorbox{lightgreen}{$
		\left[
			\frac{27}{16}, \frac{57}{32}
		\right]
	$}
\end{align*}
$$

> [!quote] 3.6 Zwischenwertsatz Beweis
> $$
> \begin{gather*}
> 	b_0 - a_0 = b - a \\
> 	b_1 - a_1 = b_0 - \frac{a_0+b_0}{2} = \frac{2b_0 - a_0 + b_0}{2} = \frac{b_0 - a_0}{2} = \frac{1}{2} (b-a) \\
> 	b_2 - a_3 = \frac{1}{2}(b_1-a_1) = \Big(\frac{1}{2}\Big)^2(b-a) \\
> 	\colorbox{yellow}{$
> 		b_n-a_n = \Big(\frac{1}{2}\Big)^n (b - a)
> 	$}
> \end{gather*}
> $$

