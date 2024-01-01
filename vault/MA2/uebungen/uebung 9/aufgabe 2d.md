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
		$} - \colorbox{yellow}{$
			\ln \left(
				\frac{x^3}{\ln x}
			\right)
		$} \cdot
		\colorbox{aqua}{$x^3$} \cdot
		\frac{\ln x}{\colorbox{aqua}{$x^3$}} \cdot \colorbox{pink}{$
			\frac{
				(x^3)' \cdot \ln x - x^3 \cdot (\ln x)'
			}{
				\ln^2 x
			}
		$}
	}{
		x^3 \cdot \colorbox{yellow}{$
			\ln^2 \left(
				\frac{x^3}{\ln x}
			\right)
		$}
	} \\

	&= \frac{3x^2}{x^3} - \frac{\ln x}{
		x^3 \ln \left(
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
		\colorbox{lightgray}{$\ln x$} \cdot \left(
			3x^2 \cdot \ln x - x^2
		\right)
	}{
		x^3 \ln \left(
			\frac{x^3}{\ln x}
		\right) \colorbox{lightgray}{$\ln^2 x$}
	} \\

	&= \frac{3}{x} - \frac{
		3\colorbox{violet}{$x^2$} \cdot \ln x - \colorbox{violet}{$x^2$}
	}{
		\colorbox{violet}{$x^3$} \ln \left(
			\frac{x^3}{\ln x}
		\right) \ln x
	} \\

	&= \frac{3}{x} - \frac{
		3 \ln x - 1
	}{
		x \colorbox{lavender}{$
			\ln \left(
				\frac{x^3}{\ln x}
			\right)
		$} \ln x
	} \\

	&= \frac{3}{x} - \frac{3 \ln x - 1}{x \ln x \colorbox{lavender}{$
		\left(
			3 \ln x - \ln \ln x
		\right)
	$}}
\end{align*}
$$

> [!NOTE] Beachte
> - Summen/Differenzen in Brüchen $\to$ nicht einfach zusammenführen
> - Einfacher wäre: f und g als Nenner und Zähler definieren und erst später einsetzen
> - $\lambda ab-a \ne (\lambda-1)ab$
> - Bruch-Logarithmus vereinfachen

> [!info] 4.13 Eigenschaften des Logarithmus
>$$
>\begin{gather*}
>	\ln(xy) = \ln x + \ln y \\
>	\ln \frac{1}{x} = -\ln x \\
>	\ln x^r = r \ln x
>\end{gather*}
>$$
