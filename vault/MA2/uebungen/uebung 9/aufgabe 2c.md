$$
f_3(x) = \frac{
	\sin \left( \sqrt x \right)
}{
	1 + \cos \left( \sqrt x \right)
}
$$

# Ableitung

$$
\begin{align*}
	\frac{d}{dx} f_3 &= \frac{
		\frac{d}{dx} \left(
			\sin \left(
				\sqrt x
			\right)
		\right) \cdot \left(
			1 + \cos \left(
				\sqrt x
			\right)
		\right) - \left(
			\sin \left(
				\sqrt x
			\right)
		\right) \cdot \frac{d}{dx} \left(
			1 + \cos \left(
				\sqrt x
			\right)
		\right)
	}{
		\left(
			1 + \cos \left(
				\sqrt x
			\right)
		\right)^2
	} \\

	&= \frac{
		\left(
			\cos \left(
				\sqrt x
			\right) \cdot \left(
				\sqrt x
			\right)'
		\right) \cdot \left(
			1 + \cos \left(
				\sqrt x
			\right)
		\right) - \left(
			\sin \left(
				\sqrt x
			\right)
		\right) \cdot \left(
			-\sin \left(
				\sqrt x
			\right) \cdot \left(
				\sqrt x
			\right)'
		\right)
	}{
		\left(
			1 + \cos \left(
				\sqrt x
			\right)
		\right)^2
	} \\

	&= \frac{
		\left(
			\cos \left(
				\sqrt x
			\right) \cdot \frac{1}{2 \sqrt x}
		\right) \cdot \left(
			1 + \cos \left(
				\sqrt x
			\right)
		\right) - \left(
			\sin \left(
				\sqrt x
			\right)
		\right) \cdot \left(
			-\sin \left(
				\sqrt x
			\right) \cdot \frac{1}{2 \sqrt x}
		\right)
	}{
		\left(
			1 + \cos \left(
				\sqrt x
			\right)
		\right)^2
	} \\

	&= \frac{
		\frac{
			\left(
				\cos(\sqrt x)
			\right)\left(
				1 + \cos(\sqrt x)
			\right)
		}{2 \sqrt x} + \frac{
			\sin^2(\sqrt x)
		}{
			2 \sqrt x
		}
	}{
		(1 + \cos(\sqrt x))^2
	} \\

	&= \frac{
		\cos(\sqrt x) + \overbrace{\cos^2(\sqrt x) + \sin^2(\sqrt x)}^{=1}
	}{
		2 \sqrt x \cdot (1 + \cos(\sqrt x))^2
	} \\

	&= \frac{
		\cos(\sqrt x) + 1
	}{
		2 \sqrt x \cdot (1 + \cos(\sqrt x))^2
	} \\

	&= \frac{
		1
	}{
		2 \sqrt x \cdot (1 + \cos(\sqrt x))
	}
\end{align*}
$$

> [!NOTE] 2.21 (vii)
>$$
>\cos^2(x) + \sin^2(x) = 1
>$$
