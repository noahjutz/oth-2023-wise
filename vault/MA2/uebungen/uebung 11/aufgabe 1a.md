$$
\int t^2 e^t \,dt = \ldots
$$

> [!info] 5.10 Partielle Integration
> $$
> \int f(x) \cdot g'(x) \,dx = f(x) \cdot g(x) - \int f'(x) \cdot g(x) \,dx
> $$

> [!NOTE] Nebenrechnung
> $$
> \begin{gather*}
> 	f(t) = t^2 & f'(t) = 2t \\
> 	g(t) = e^t & g'(t) = e^t
> \end{gather*}
> $$

$$
\ldots =t^2 \cdot e^t - \int 2t \cdot e^t
$$

> [!note] Nebenrechnung
> $$
> \begin{gather*}
> 	f(t) = 2t & f'(t) = 2 \\
> 	g(t) = e^t & g'(t) = e^t
> \end{gather*}
> $$

$$
\ldots = t^2 \cdot e^t - \left(
	2t \cdot e^t - \int 2 \cdot e^t
\right)
$$

> [!note] Nebenrechnung
> $$
> \begin{gather*}
> 	f(t) = 2 & f'(t) = 0 \\
> 	g(t) = e^t & g'(t) = e^t
> \end{gather*}
> $$

$$
\begin{align*}
	\ldots &= t^2 \cdot e^t - \left(
		2t \cdot e^t - \left(
			2 \cdot e^t - \int 0 \cdot e^t
		\right)
	\right) \\

	&= t^2 \cdot e^t - 2t \cdot e^t + 2 \cdot e^t - 0 \color{red} + c \\
	&= \underline{e^t \cdot (t^2 - 2t + 2) + c}
\end{align*}
$$

> [!warning] +c nicht vergessen
