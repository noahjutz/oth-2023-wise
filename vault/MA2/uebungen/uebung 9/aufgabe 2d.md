$$
f_4(x) = \ln \left(
	\frac{x^3}{\ln \left(
		\frac{x^3}{\ln x}
	\right)}
\right)
$$

# Ableitung

$$
\begin{align*}
	f_4'(x) &= \left(
		\frac{x^3}{\ln \left(
			\frac{x^3}{\ln x}
		\right)}
	\right)^{-1} \cdot \frac{
		(x^3)' \cdot \ln \left(
			\frac{x^3}{\ln x}
		\right) - x^3 \cdot \colorbox{lightgreen}{$
			\left(
				\ln \frac{x^3}{\ln x}
			\right)'
		$}
	}{
		\ln^2 \left(
			\frac{x^3}{\ln x}
		\right)
	} \\

	&= \frac{
		\ln \left(
			\frac{x^3}{\ln x}
		\right)
	}{
		x^3
	} \cdot \frac{
		3x^2 \cdot \ln \left(
			\frac{x^3}{\ln x}
		\right) - x^3 \cdot \colorbox{lightgreen}{$
			\left(
				\frac{x^3}{\ln x}
			\right)^{-1} \cdot \left(
				\frac{x^3}{\ln x}
			\right)'
		$}
	}{
		\ln^2 \left(
			\frac{x^3}{\ln x}
		\right)
	} \\

	&= \frac{
		\colorbox{yellow}{$
			\ln \left(
				\frac{x^3}{\ln x}
			\right)
		$} \cdot 3x^2 \cdot \colorbox{yellow}{$
			\ln \left(
				\frac{x^3}{\ln x}
			\right)
		$} - \colorbox{aqua}{$x^3$} \cdot \frac{
			\ln x
		}{
			\colorbox{aqua}{$x^3$}
		} \cdot \colorbox{pink}{$
			\frac{
				(x^3)' \cdot \ln x - x^3 \cdot (\ln x)'
			}{
				\ln^2 x
			}
		$}
	}{
		x^3 \cdot \ln^2 \left(
			\frac{x^3}{\ln x}
		\right)
	} \\

	&= \frac{
		\colorbox{yellow}{$
			\ln^2 \left(
				\frac{x^3}{\ln x}
			\right)
		$} \cdot 3x^2
	}{
		x^3 \ln^2 \left(
			\frac{x^3}{\ln x}
		\right)
	} - \frac{
		\ln x
	}{
		x^3 \ln^2\left(
			\frac{x^3}{\ln x}
		\right)
	} \cdot \colorbox{pink}{$
		\frac{
			3x^2 \cdot \ln x - x^3 \cdot \frac{1}{x}
		}{
			\ln^2 x
		} 
	$} \\

	&= \frac{3}{x} - \frac{
		\ln^2 x \cdot 2x^2
	}{
		x^3 \ln^2 \left(
			\frac{x^3}{\ln x}
		\right) \ln^2 x
	}

\end{align*}
$$

> [!NOTE] Beachte
> - 
