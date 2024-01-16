$$
\int x^2 \sin x \,dx = \ldots
$$

$$
\begin{gather*}
	f(x) = x^2 & g(x) = -\cos x \\
	f'(x) = 2x & g'(x) = \sin x
\end{gather*}
$$

$$
\ldots = x^2 \cdot (-\cos x) - \int 2x \cdot (-\cos x) = \ldots
$$

$$
\begin{gather*}
	f(x) = 2x & g(x) = -\sin x \\
	f'(x) = 2 & g'(x) = -\cos x
\end{gather*}
$$

$$
\begin{align*}
	\ldots &= x^2 \cdot (-\cos x) - \left(
		2x \cdot (-\sin x)  - \int 2 \cdot (-\sin x) \,dx
	\right) \\
	&= -x^2 \cdot \cos x + 2x \cdot \sin x - 2 \int \sin x \,dx \\
	&= \underline{-x^2 \cdot \cos x + 2x \cdot \sin x + 2 \cos x + c}
\end{align*}
$$


> [!warning] +c nicht vergessen
