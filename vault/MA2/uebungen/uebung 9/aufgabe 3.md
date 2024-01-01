# Taylorpolynom

$$
T(f, x_0, x) = \sum_{k=0}^n \frac{f^{(k)}(x_0)}{k!} (x - x_0)^k
$$

# exp(x)

$$
\begin{gather*}
	f(x) = e^x & f^{(k)}(x) = e^x
\end{gather*}
$$

# Taylorpolynom für exp(x)

$$
\begin{align*}
	T_n(\exp(x), 0, x) &= \sum_{k=0}^n \frac{\exp(0)}{k!} x^k \\

	&= \sum_{k=0}^n \frac{x^k}{k!}
\end{align*}
$$

![[aufgabe 3 graph.svg|300]]

# k = 0

Das 0-te Taylorpolynom der Exponentialfunktion $\exp(x)$ ist:

$$
T_0(\exp(x), 0, x) = \frac{x^0}{0!} = 1
$$

Die Abweichung des n-ten Taylorpolynoms zur Exponentialfunktion sei definiert als:

$$
d_n(x) = \exp(x)-T_n(\exp(x), 0, x)
$$

Maximiere $d_0(x)$ in $x \in [0; 1]$:

$$
\begin{align*}
	\frac{d}{dx} d_0(x) &= 0 \\

	\exp(x) &= 0 \\

	x &= \ln 0 \text{ (nicht definiert)}
\end{align*}
$$

$\implies$ Keine Nullstelle, Extremwert in Randpunkten.

$$
\begin{gather*}
	d_0(0) = \exp(0) - 1 = 0 & d_0(1) = \exp(1) - 1 = \underline{e - 1}
\end{gather*}
$$
Maximale Abweichung $e - 1 > 5 \cdot 10^{-5}$. k=0 reicht also nicht aus.

# k = 1

$$
T_1 = 1 + x
$$

Maximiere $d_1(x)$:

$$
\begin{align*}
	\exp(x) - 1 &= 0 \\
	x &= \ln 1 \\
	x &= 0
\end{align*}
$$

$$
\begin{gather*}
	d_1(0) = 0 & d_1(1) = \underline{e - 1}
\end{gather*}
$$

# k = 2

$$
T_2 = 1 + x + \frac{x^2}{2}
$$

Maximiere $d_2(x)$:

$$
\begin{align*}
	\exp(x) - 1 - x &= 0 \\

	\exp(x) &= x + 1
\end{align*}
$$

$\implies$ Keine Nullstelle, Extremwert in Randpunkten.

$$
\begin{gather*}
	d_2(0) = 1 & d_2(1) = \underline{e - \frac{1}{2}}
\end{gather*}
$$