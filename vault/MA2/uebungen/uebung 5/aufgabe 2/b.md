$$
g(x) = \left\{
	\begin{align*}
		 &\cos(x+2)-1 &\text{für } x \le -2 \\
		 &-(x+2)^2+1 &\text{für } x > -2
	\end{align*}
\right.
$$

# x0
$$
x_0 = -2
$$

# Stetigkeit in $x_0$

## Linksseitiger Grenzwert

$$
\begin{align*}
	\lim_{x \nearrow x_0} g(x) &= \lim_{x \nearrow -2} \cos(x+2)-1 \\

	&= -1 + \lim_{\epsilon \searrow 0} \cos(-2-\epsilon+2) \\

	&= -1 + \lim_{\epsilon \searrow 0} \cos(-\epsilon) \\

	&= -1 + 1 \\

	&= \underline 0
\end{align*}
$$

## Rechtsseitiger Grenzwert

$$
\begin{align*}
	\lim_{x \searrow x_0} g(x) &= \lim_{x \searrow -2} -(x+2)^2+1 \\

	&= 1 + \lim_{\epsilon \searrow 0} -(-2+\epsilon+2) \\

	&= 1 - \lim_{\epsilon \searrow 0} \epsilon \\

	&= \underline 1
\end{align*}
$$

# Antwort

$$
\lim_{x \nearrow x_0} g(x) \ne \lim_{x \searrow x_0} g(x)
\implies g(x) \text{ ist nicht stetig.}
$$

> [!check] Richtig
