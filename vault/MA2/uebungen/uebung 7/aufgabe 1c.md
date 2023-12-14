$$
f(x) = x^3 + 2x - 1
$$

# Zweite Ableitung der Umkehrfunktion

Gesucht ist $\left(f^{-1}\right)''$.

> [!info] 4.9 Umkehrfunktion
>$$
>\left(f^{-1}\right)'(y_0) = \frac{1}{f'(x_0)}
>$$

$$
\begin{align*}
	\left(f^{-1}\right)''(y_0) &= \left(
		\frac{1}{f'\big(f^{-1}(y_0)\big)}
	\right)' \\

	&= -\frac{
		\Big(f'\big(f^{-1}(y_0)\big)\Big)'
	}{
		\Big(f'\big(f^{-1}(y_0)\big)\Big)^2
	} \\

	&= -\frac{
		f''\big(f^{-1}(y_0)\big) \cdot \big(f^{-1}\big)'(y_0)
	}{
		\Big(f'\big(f^{-1}(y_0)\big)\Big)^2
	} \\

	&= -\frac{
		f''\big(f^{-1}(y_0)\big) \cdot \frac{1}{f'\big(f^{-1}(y_0)\big)}
	}{
		\Big(f'\big(f^{-1}(y_0)\big)\Big)^2
	} \\

	&= \boxed{-\frac{
		f''\big(f^{-1}(y_0)\big)
	}{
		\Big(f'\big(f^{-1}(y_0)\big)\Big)^3
	}} \\
\end{align*}
$$

# In 2

Gesucht ist $\left(f^{-1}\right)''(2)$.

> [!NOTE] Ableitung von f
>$$
>\begin{gather*}
>	f'(x) = 3x^2+2 && f''(x) = 6x
>\end{gather*}
>$$

> [!NOTE] x und y
> Wir wissen aus [[aufgabe 1b]], dass $f(1) = 2 \iff f^{-1}(2) = 1$.

$$
\begin{align*}
	\left(f^{-1}\right)''(2) &= -\frac{
		f''\big(f^{-1}(2)\big)
	}{
		\Big(f'\big(f^{-1}(2)\big)\Big)^3
	} \\

	&= -\frac{f''(1)}{\big(f'(1)\big)^3} \\
 
	&= -\frac{6}{(3+2)^3} \\

	&= \boxed{-\frac{6}{125}}
\end{align*}
$$
