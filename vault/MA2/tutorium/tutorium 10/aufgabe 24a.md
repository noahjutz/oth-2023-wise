$$
\begin{align*}
	\lim_{x \to 1} \frac{
		\sqrt{x+1} - \sqrt{2x}
	}{
		\sqrt{x+2} - \sqrt{3x}
	} &= \lim_{x \to 1} \frac{
		\sqrt{x+1} - \sqrt 2 \sqrt  x
	}{
		\sqrt{x+2} - \sqrt 3 \sqrt x
	} \\

	&\stackrel{L'H}{=} \lim_{x \to 1} \frac{
		\left(
			\sqrt{x+1} - \sqrt 2 \sqrt  x
		\right)'
	}{
		\left(
			\sqrt{x+2} - \sqrt 3 \sqrt x
		\right)'
	} \\

	&= \lim_{x \to 1} \frac{
		\frac{1}{2}(x+1)^{-\frac{1}{2}} - \big(
			2^{\frac{1}{2}} \cdot \frac{1}{2} \cdot x^{-\frac{1}{2}}
		\big)
	}{
		\frac{1}{2}(x+1)^{-\frac{1}{2}} - \big(
			3^{\frac{1}{2}} \cdot \frac{1}{2} 
		\big)
	}
\end{align*}
$$