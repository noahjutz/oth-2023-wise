$$
f(x) = x^3 + 2x - 1
$$

![[f.svg|250]]

# Ableitung der Umkehrfunktion in 2

Gesucht ist $\left(f^{-1}\right)'(2)$

> [!info] 4.9 Umkehrfunktion
>$$
>\left(f^{-1}\right)'(y_0) = \frac{1}{f'(f^{-1}(y_0))} = \frac{1}{f'(x_0)}
>$$

$$
\begin{align*}
	\left(f^{-1}\right)'(2) &= \frac{1}{f'\big(
		f^{-1}(2)
	\big)}
\end{align*}
$$

Was ist $f^{-1}(2)$?

> [!info] 4.9 Umkehrfunktion
>$$
>\begin{gather*}
>	f^{-1}\big(f(x)\big) = x && f\big(f^{-1}(y)\big) = y \\
>	f^{-1}(y) = x && f(x) = y
>\end{gather*}
>$$

$$
\begin{align*}
	f(x) &= 2 \\
	x^3 + 2x - 1 &= 2 \\
	x &= 1
\end{align*}
$$

$\implies f^{-1}(2) = 1$

$$
\begin{align*}
	\left(f^{-1}\right)(2) &= \frac{1}{f'(1)} \\

	&= \frac{1}{3+2} \\

	&= \underline{\frac{1}{5}}
\end{align*}
$$
