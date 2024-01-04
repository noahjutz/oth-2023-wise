
> [!info] 4.5 Taylor-Entwicklung
> $$
> T_n(f, x_0, x) = \sum_{k=0}^n \frac{f^{(k)}(x_0)}{k!} (x - x_0)^k
> $$
> 
> $$
> R_{n+1}(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}
> $$
> 
> $$
> f(x) = T_n(f, x_0, x) + R_{n+1}(x)
> $$

# Ableitung von exp(x)

$$
\begin{gather*}
	f(x) = e^x \\
	f^{(k)}(x) = e^x
\end{gather*}
$$

# Taylorpolynom von exp(x)

$$
\begin{align*}
	T_n(\exp(x), 0, x) &= \sum_{k=0}^n \frac{\exp(0)}{k!} x^k \\

	&= \sum_{k=0}^n \frac{x^k}{k!}
\end{align*}
$$

![[aufgabe 3 graph.svg|300]]

# Versuch: 7tes Taylorpolynom

$$
\begin{align*}
	T_7(\exp(x), 0, x) &= \sum_{k=0}^7 \frac{x^k}{k!} \\
	&= 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24} +
	\frac{x^5}{120} + \frac{x^6}{720} + \frac{x^7}{5040}
\end{align*}
$$

## Abweichung prüfen

Die Abweichung des Taylorpolynoms zur Exponentialfunktion sei definiert als:

$$
d(x) = \exp(x) - T_7(\exp(x), 0, x)
$$

Maximiere $d(x)$ in $x \in [0; 1]$:

$$
\begin{align*}
	\frac{dd}{dx} &= 0 \\
	e^x - T_7'(e^x, 0, x) &= 0 \\
	e^x - \sum_{k=0}^6 \frac{x^k}{k!} &= 0 \\
	x &= 0
\end{align*}
$$

$$
\begin{gather*}
	d(0) = e^0 - 1 = 0 \\
	d(1) = e - \sum_{k=0}^6 \frac{1}{k!} \approx 0.0002 > 5 \cdot 10^{-5}
\end{gather*}
$$

$\implies$ Die Abweichung ist zu groß.

# Versuch: n rechnerisch ermitteln

$$
e^x = \underbrace{
	\sum_{k=0}^n \frac{x^k}{k!}
}_{T_n} + \underbrace{
	\frac{x^{n+1}}{(n+1)!} \cdot \exp(\xi)
}_{R_{n+1}}
$$
$$
\begin{gather*}
	\xi \in [0, 1] \implies \exp(\xi) \in [1, e] \\
	x \in [0, 1]
\end{gather*}
$$

Wir wollen, dass $R_{n+1}$ für alle $\xi$ kleiner gleich $5 \cdot 10^{-5}$ ist. Das ist immer erfüllt, wenn wir von $\xi = 1$ und $x=1$ ausgehen, da damit die Faktoren $\exp(\xi)$ und $x^{n+1}$ maximal sind.

$$
\begin{align*}
	R_{n+1}(x) &\le 5 \cdot 10^{-5} \\
	\frac{x^{n+1}}{(n+1)!} \cdot \exp(\xi) &\le 5 \cdot 10^{-5} \\
	\frac{1}{(n+1)!} \cdot e &\le 5 \cdot 10^{-5} \\
	\frac{1}{(n+1)!} &\le \frac{5 \cdot 10^{-5}}{e} \\
	(n+1)! &\ge \frac{e}{5 \cdot 10^{-5}} \\
\end{align*}
$$