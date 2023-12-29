$$
f_1(x) = \frac{\sqrt x + x}{\sqrt x - x}
$$

# Ableitung

$$
\begin{align*}
	f_1'(x) &= \frac{
		\left(
			\sqrt x + x
		\right)' \cdot \left(
			\sqrt x - x
		\right) - \left(
			\sqrt x + x
		\right) \cdot \left(
			\sqrt x - x
		\right)'
	}{
		\left(
			\sqrt x - x
		\right)^2
	} \\

	&= \frac{
		\left(
			x^\frac{1}{2} + x
		\right)' \cdot \left(
			x^\frac{1}{2} - x
		\right) - \left(
			x^\frac{1}{2} + x
		\right) \cdot \left(
			x^\frac{1}{2} - x
		\right)'
	}{
		\left(
			\sqrt x - x
		\right)^2
	} \\

	&= \frac{
		\left(
			\frac{1}{2} x^{-\frac{1}{2}} + 1
		\right) \cdot \left(
			x^\frac{1}{2} - x
		\right) - \left(
			x^\frac{1}{2} + x
		\right) \cdot \left(
			\frac{1}{2} x^{-\frac{1}{2}} - 1
		\right)
	}{
		\left(
			\sqrt x - x
		\right)^2
	}
\end{align*}
$$

# Vereinfachen

$$
\begin{align*}
	&= \frac{
		\left(
			\frac{1}{2}x^{-\frac{1}{2}} \cdot x^\frac{1}{2} +
			1 \cdot x^\frac{1}{2} -
			\frac{1}{2}x^{-\frac{1}{2}} \cdot x -
			1 \cdot x
		\right) - \left(
			x^\frac{1}{2} \cdot \frac{1}{2} x^{-\frac{1}{2}} +
			x \cdot \frac{1}{2} x^{-\frac{1}{2}} -
			x^\frac{1}{2} \cdot 1 -
			x \cdot 1
		\right)
	}{
		\left(
			\sqrt x - x
		\right)^2
	} \\

	&= \frac{
		\left(
			\frac{1}{2} x^0 + x^\frac{1}{2} - \frac{1}{2} x^\frac{1}{2}  - x
		\right) - \left(
			\frac{1}{2} x^0 + \frac{1}{2} x^\frac{1}{2} - x^\frac{1}{2} - x
		\right)
	}{
		\left(
			\sqrt x - x
		\right)^2
	} \\

	&= \frac{
		\frac{1}{2} + x^\frac{1}{2} - \frac{1}{2} x^\frac{1}{2} - x -
		\frac{1}{2} - \frac{1}{2}x^\frac{1}{2} + x^\frac{1}{2} + x
	}{
		\left(
			\sqrt x - x
		\right)^2
	} \\

	&= \frac{
		\sqrt x
	}{
		\left(
			\sqrt x - x
		\right)^2
	} \\
\end{align*}
$$

> [!NOTE] Beachten
> - Quotientenregel benutzen
> - $x' = 1$
