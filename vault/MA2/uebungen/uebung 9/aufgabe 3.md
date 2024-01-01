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

# n = 0

Das 0-te Taylorpolynom der Exponentialfunktion $\exp(x)$ ist:

$$
T_0(\exp(x), 0, x) = \frac{x^0}{0!} = 1
$$

Die Abweichung des n-ten Taylorpolynoms zur Exponentialfunktion sei definiert als:

$$
d_n(x) = \exp(x)-T_n(\exp(x), 0, x)
$$

Maximiere $d_0(x)$ in $x \in [0; 1]$:
- $d_n(x)$ ist monoton steigend $\implies$ Maximum ist $d_n(1)$.

$$
d_0(1) = \underline{e - 1}
$$

# n = 1

Berechne $T_1$:

$$
T_1 = 1 + x
$$

Maximiere $d_1(x)$:

$$
d_1(1) = \underline{e - 2}
$$

# n = 2

Berechne $T_2$:

$$
T_2 = 1 + x + \frac{x^2}{2}
$$

Maximiere $d_2(x)$:
$$
d_2(1) = \underline{e - \frac{3}{2}}
$$

# n = 5

Berechne $T_5$:

$$
T_5 = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24} + \frac{x^5}{120}
$$

Maximiere $d_5(x)$:

$$
d_5(1) = \underline{e - \frac{163}{60}}
$$

# n = 10

$$
d_{10}(1) = \underline{e - \frac{9\ 864\ 101}{3\ 628\ 800}}
$$

# n rechnerisch ermitteln

$$
\begin{align*}
	e - \sum_{k=0}^n \frac{1}{k!} &\le 5 \cdot 10^{-5} \\
	
	\sum_{k=0}^n \frac{1}{k!} &\ge e - 5 \cdot 10^{-5} \\
\end{align*}
$$

 todo solve for n