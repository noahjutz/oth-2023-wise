$$
f(x) = \left\{
	\begin{align*}
		 &\sin(x-3)+4 &\text{für } x \le 3 \\
		 &(x-2)^3+3 &\text{für } x > 3
	\end{align*}
\right.
$$

# x_0
$$
x_0 = 3
$$

# Stetigkeit in $x_0$

## Für $x \le 3$
$$
f(x_0) = \sin(x_0-3)+4 = \sin(3-3)+4 = \underline 4
$$

> [!warning] Korrektur
> Nich $f(x_0)$ berechnen, sondern $\lim_{x \nearrow x_0} f(x)$

## Für $x > 3$
$$
\begin{align*}
	\lim_{x \nearrow x_0} (x-2)^3+3 &= \lim_{x \nearrow 3} (x-2)^3+3 \\

	&= 3 + \lim_{\epsilon \searrow 0} \big(
		(3 - \epsilon) - 2
	\big)^3 \\

	&= 3 + \left(
		\lim_{n \to \infty} \left(
			3 - \frac{1}{n} - 2
		\right)
	\right)^3 \\

	&=3 + \left(
		3 - 2 - \lim_{n \to \infty} \frac{1}{n}
	\right)^3 \\

	&= 3 + (3 - 2)^3 \\

	&= \underline 4 \\

	&= f(x_0)
\end{align*}
$$

Gilt auch für $\lim_{x \searrow x_0}$.


> [!warning] Korrektur
> Nicht $\lim_{x \nearrow x_0} f(x)$ berechnen, sonder $\lim_{x \searrow x_0} f(x)$.

# Antwort
$f(x)$ ist in $x_0 = 3$ stetig, da $\lim_{x \to x_0} f(x) = f(x_0)$.

> [!danger] Falsche Begründung
> Richtig wäre: $f(x)$ ist in $x_0 = 3$ stetig, da der linksseitige Grenzwert $\lim_{x \nearrow x_0} f(x)$ gleich dem rechtsseitigen Grenzwert $\lim_{x \searrow x_0} f(x)$ ist (=4).
