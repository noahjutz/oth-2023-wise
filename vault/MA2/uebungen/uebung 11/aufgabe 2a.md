$$
f(x) = \frac{x}{x+3}
$$

# Taylorpolynom 2. Ordnung

> [!note] Ableitungen von f(x)

$$
\begin{gather*}
	f(x) = \frac{x}{x+3} \\
	f'(x) = \frac{3}{(x+3)^2} \\
	f''(x) = -\frac{-3 \cdot 2(x+3) \cdot (1+0)}{}
\end{gather*}
$$

$$
\begin{alignat*}{3}
	&T_2(f, 1, x) &=& \sum_{k=0}^2 \frac{f^{(k)}(1)}{k!}(x-1)^k \\
	&&=& \frac{0}{0+3}(x-1)^0 + \frac{3}{(1+3)^2}(x-1)^1 + \\
	&&& \frac{1}{2!} \cdot \frac{6 \cdot 2 + 18}{(2+3)^4}
		(x-1)^2 \\
	&&=& 0 + \frac{3}{16} \cdot (x-1) + \frac{3}{125}(x-1)^2 \\
	&&=& \frac{3}{16}x - \frac{3}{16} + \frac{3}{125} (x^2-2x+1) \\
	&&=& \frac{3}{16}x - \frac{3}{16} + \frac{3}{125}x^2 - \frac{6}{125}x + \frac{3}{125} \\
	&&=& \frac{1}{2000} \left(
		3 \cdot 125x - 3 \cdot 125 + 3 \cdot 16x^2  - 6 \cdot 16x + 3 \cdot 16
	\right) \\
	&&=& \frac{1}{2000} \left(
		375x-375+48x^2-96x+48
	\right) \\
	&&=& \frac{1}{2000} \left(
		48x^2 + 279x - 327
	\right) \\
	&&=& \underline{0.024x^2 + 0.1395x - 0.1635}
\end{alignat*}
$$


> [!fail] Falsch
> $f(1)$, nicht $f(k)$.

$$
\begin{align*}
	T_2(f, 1, x) &= \sum_{k=0}^2 \frac{f^{(k)}(1)}{k!}(x-1)^k \\
	&= \frac{1}{1+3}(x-1)^0 + \frac{3}{(1+3)^2}(x-1)^1 +
	\frac{1}{2!} \cdot \frac{6 + 18}{(1+3)^4} (x-1)^2 \\
	&= \frac{1}{4} + \frac{3}{16}(x-1) + \frac{24}{16 \cdot 8 \cdot 2}
	(x-1)^2 \\
	&= \frac{1}{4} + \frac{3}{16}x - \frac{3}{16} + \frac{1}{32}(x^2-2x+1) \\
	&= \frac{1}{32}x^2 + \frac{3}{16}x - \frac{1}{16}x +
	\frac{1}{4} - \frac{3}{16} + \frac{1}{32} \\
	&= \frac{1}{32} \left(
		x^2 + (3 \cdot 2) x - (1 \cdot 2)x + (1 \cdot 8) - (3 \cdot 2) + 1
	\right) \\
	&= \frac{1}{32} \left(
		x^2 + 4x + 3
	\right) \\
	&= \underline{
		\frac{1}{32}x^2 + \frac{1}{8}x + \frac{3}{32}
	}
\end{align*}
$$


> [!fail] Falsch
> $f''(x) \ne \frac{6x+18}{(x+3)^4}$

