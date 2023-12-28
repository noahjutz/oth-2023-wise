$$
\begin{align*}
	\lim_{x \to 1} x^{
		\left(
			\frac{1}{x-1}
		\right)
	}

	&= \exp \left(
		\lim_{x \to 1} \frac{1}{x-1} \cdot \ln x
	\right) \\

	&= \exp \left(
		\lim_{x \to 1} \frac{\ln x}{x-1}
	\right) \\

	&\overset{\text{L'H}}{\underset{0/0}{=}}
	 \exp \left(
		\lim_{x \to 1} \frac{\frac{1}{x}}{1}
	\right) \\

	&= \exp(1) \\

	&= e
\end{align*}
$$

> [!info] 4.17 (3) L'Hospital Potenzen
>$$
>\begin{align*}
>	\lim_{x \to x_0} f(x)^{g(x)} &= \lim_{x \to x_0} \exp \Big(
>		g(x) \cdot \ln f(x)
>	\Big) \\
>
>	&= \exp \Big(
>		\lim_{x \to x_0} g(x) \cdot \ln f(x)
>	\Big)
>\end{align*}
>$$
>
> > [!NOTE]
> >$$
> >x = \exp(\ln x)
> >$$
> 
> > [!NOTE] 
> >$$
> >\exp(a)^b = \exp(a \cdot b)
> >$$
> 
> > [!NOTE]
> >$$
> >\lim \exp\Big(f(x)\Big) = \exp\Big(\lim f(x)\Big)
> >$$
> 
