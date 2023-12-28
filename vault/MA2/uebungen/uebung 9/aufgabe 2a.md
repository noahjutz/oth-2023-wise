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
			\frac{1}{2} x^{-\frac{1}{2}} + x
		\right) \cdot \left(
			x^\frac{1}{2} - x
		\right) - \left(
			x^\frac{1}{2} + x
		\right) \cdot \left(
			\frac{1}{2} x^{-\frac{1}{2}} - x
		\right)
	}{
		\left(
			\sqrt x - x
		\right)^2
	}
\end{align*}
$$

# Zähler Vereinfachen

$$
\begin{align*}

	&= \frac{
		\left(
			\frac{1}{2}x^{-\frac{1}{2}} \cdot x^\frac{1}{2} +
			x \cdot x^\frac{1}{2} -
			\frac{1}{2}x^{-\frac{1}{2}} \cdot x -
			x^2
		\right) - \left(
			x^\frac{1}{2} \cdot \frac{1}{2} x^{-\frac{1}{2}} +
			x \cdot \frac{1}{2} x^{-\frac{1}{2}} -
			x^\frac{1}{2} \cdot x -
			x^2
		\right)
	}{
		\left(
			\sqrt x - x
		\right)^2
	} \\

	&= \frac{
		\left(
			\frac{1}{2} x^0 + x^\frac{3}{2} - \frac{1}{2} x^\frac{1}{2}  - x^2
		\right) - \left(
			\frac{1}{2} x^0 + \frac{1}{2} x^\frac{1}{2} - x^\frac{3}{2} - x^2
		\right)
	}{
		\left(
			\sqrt x - x
		\right)^2
	} \\

	&= \frac{
		\frac{1}{2} + x^\frac{3}{2} - \frac{1}{2} x^\frac{1}{2} - x^2 -
		\frac{1}{2} - \frac{1}{2}x^\frac{1}{2} + x^\frac{3}{2} + x^2
	}{
		\left(
			\sqrt x - x
		\right)^2
	} \\

	&= \frac{
		2 x^\frac{3}{2} - x^\frac{1}{2}
	}{
		\left(
			\sqrt x - x
		\right)^2
	}
\end{align*}
$$

# Nenner Vereinfachen

$$
\begin{align*}
	&= \frac{
		2 x \sqrt x - \sqrt x
	}{
		x - 2 x \sqrt x + x^2
	} \\

	&= \frac{
		2 x \sqrt x \left(
			1 - \frac{\sqrt x}{2 x \sqrt x}
		\right)
	}{
		2 x \sqrt x \left(
			\frac{x}{2 x \sqrt x} - 1 + \frac{x^2}{2 x \sqrt x}
		\right)
	} \\

	&= \frac{
		1 - \frac{1}{2x}
	}{
		\frac{1}{2 \sqrt x} - 1 + \frac{x}{2 \sqrt x}
	} \\

	&= \frac{
		\frac{2x - 1}{2x}
	}{
		\frac{1 + x - 2 \sqrt x}{2 \sqrt x}
	} \\

	&= \frac{2x - 1}{2x} \cdot \frac{2 \sqrt x}{1 + x - 2 \sqrt x} \\

	&= \frac{
		4x \sqrt x - 2 \sqrt x
	}{
		2x + 2x^2 - 4x \sqrt x
	} \\

	&= \frac{
		4 x \sqrt x \left(
			1 - \frac{\sqrt{2x}}{4 x \sqrt x}
		\right)
	}{
		4x \sqrt x \left(
			\frac{2x + 2x^2}{4 x \sqrt x} - 1
		\right)
	} \\

	&= \frac{
		\frac{4 x \sqrt x - \sqrt{2x}}{4 x \sqrt x}
	}{
		\frac{2x + 2x^2 - 4 x \sqrt x}{4 x \sqrt x}
	} \\

	&= \frac{4 x \sqrt x - \sqrt{2x}}{4 x \sqrt x} \cdot
		\frac{4 x \sqrt x}{2x + 2x^2 - 4 x \sqrt x} \\

	&= \frac{
		4 x \sqrt x - \sqrt{2x}
	}{
		2x + 2x^2 - 4 x \sqrt x
	}
\end{align*}
$$
