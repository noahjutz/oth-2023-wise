$$
\begin{align*}
	\lim_{x \to 1} \left(
		\frac{1}{\ln x} - \frac{x}{x-1}
	\right)
	
	&= \lim_{x \to 1} \frac{
		(x-1) - (x \ln x)
	}{
		(\ln x)(x - 1)
	} \\

	&= \lim_{x \to 1} \frac{
		x - 1 - x \ln x
	}{
		x \ln x - \ln x
	} \\

	&\overset{\text{L'H}}{\underset{0/0}{=}}
	\lim_{x \to 1} \frac{
		1 - 0 - \ln x - 1
	}{
		\ln x + 1 - \frac{1}{x}
	} \\

	&\overset{\text{L'H}}{\underset{0/0}{=}}
	\lim_{x \to 1} \frac{
		-\frac{1}{x}
	}{
		\frac{1}{x}+\frac{1}{x^2}
	} \\

	&= \frac{-1}{1+1} \\

	&= -\frac{1}{2}
	
\end{align*}
$$

> [!NOTE] Ableitung von x ln x
>$$
>\begin{align*}
>	(x \ln x)' &= 1 \cdot \ln x + x \cdot \frac{1}{x} \\
>
>	&= \ln x  +1
>\end{align*}
>$$
