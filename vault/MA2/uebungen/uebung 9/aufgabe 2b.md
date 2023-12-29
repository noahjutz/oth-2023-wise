$$
f_2(x) = \sin\left(\frac{\cos x}{x}\right)
$$

# Ableitung

$$
\begin{align*}
	f_2'(x) &= \cos \left(
		\frac{\cos x}{x}
	\right) \cdot \left(
		\frac{\cos x}{x}
	\right)' \\

	&= \cos \left(
		\frac{\cos x}{x}
	\right) \cdot \frac{
		(\cos x)' \cdot x - \cos x \cdot x'
	}{
		x^2
	} \\

	&= \cos \left(
		\frac{\cos x}{x}
	\right) \cdot \frac{
		-\sin x \cdot x - \cos x
	}{
		x^2
	} \\

	&= -\cos \left(
			\frac{\cos x}{x}
		\right) \cdot
		\frac{\sin x}{x} -
		\frac{\cos x}{x^2}
\end{align*}
$$
