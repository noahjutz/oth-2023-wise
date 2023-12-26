$$
\begin{align*}
	\lim_{x \to 1} \frac{x^x-x}{1-x+\ln x}
	
	&\overset{\text{L'H}}{\underset{0/0}{=}}
	\lim_{x \to 1} \frac{
		x^x \cdot (\ln x + 1) - 1
	}{
		0 - 1 + \frac{1}{x}
	} \\

	&\overset{\text{L'H}}{\underset{0/0}{=}}
	\lim_{x \to 1} \frac{
		x^x \cdot (\ln x + 1)^2 + x^x \cdot \frac{1}{x}
	}{
		-\frac{1}{x^2}
	} \\

	&= -2
\end{align*}
$$

> [!NOTE] Ableitung von x hoch x
>$$
>\begin{align*}
>	(x^x)' &= \left( e^{x\ln x} \right)' \\
>
>	&= e^{x \ln x} \cdot (x \ln x)' \\
>
>	&= e^{x \ln x} \cdot \left(
>		(x)' \cdot \ln x + x \cdot (\ln x)'
>	\right) \\
>
>	&= e^{x \ln x} \cdot \left(
>		1 \cdot \ln x + x \cdot \frac{1}{x}
>	\right) \\
>
>	&= e^{x \ln x} \cdot \left(
>		\ln x + 1
>	\right) \\
>
>	&= x^x \cdot \left(
>		\ln x + 1
>	\right) \\
>\end{align*}
>$$

> [!NOTE] Ableitung von 1 durch x
>$$
>\begin{align*}
>	\left(\frac{1}{x}\right)' &= \left(x^{-1}\right)' \\
>
>	&= -1 \cdot x^{-2} \\
>
>	&= -\frac{1}{x^2}
>\end{align*}
>$$
