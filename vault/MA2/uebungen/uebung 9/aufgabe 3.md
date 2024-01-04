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

# 7tes Taylorpolynom

Das 7te Taylorpolynom der Exponentialfunktion in $x_0 = 0$ ist:

$$
\begin{align*}
	T_7(\exp(x), 0, x) &= \sum_{k=0}^7 \frac{x^k}{k!} \\
	&= 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24} +
	\frac{x^5}{120} + \frac{x^6}{720} + \frac{x^7}{5040}
\end{align*}
$$

Die Abweichung des Taylorpolynoms zur Exponentialfunktion sei definiert als:

$$
d(x) = \exp(x) - T_7(\exp(x), 0, x)
$$

Maximiere $d(x)$ in $x \in [0; 1]$:

$$
\begin{align*}
	\frac{dd}{dx} &= 0 \\

	\exp(x) - T_7
\end{align*}
$$