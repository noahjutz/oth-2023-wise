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
		\right) - x^3 \cdot \left(
			\ln \frac{x^3}{\ln x}
		\right)'
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
		\right) - x^3 \cdot \left(
			\frac{x^3}{\ln x}
		\right)^{-1} \cdot \left(
			\frac{x^3}{\ln x}
		\right)'
	}{
		\ln^2 \left(
			\frac{x^3}{\ln x}
		\right)
	} \\

	&= \frac{
		\ln \left(
			\frac{x^3}{\ln x}
		\right) \cdot 3x^2 \cdot \ln \left(
			\frac{x^3}{\ln x}
		\right) - x^3 \cdot \frac{\ln x}{x^3} \cdot \frac{
			(x^3)' \cdot \ln x - x^3 \cdot (\ln x)'
		}{
			\ln^2 x
		}
	}{
		x^3 \cdot \ln^2 \left(
			\frac{x^3}{\ln x}
		\right)
	} \\
		
	&= \frac{
		\ln \left(
			\frac{x^3}{\ln x}
		\right) \cdot 3x^2 \cdot \ln \left(
			\frac{x^3}{\ln x}
		\right)
	}{
		x^3 \cdot \ln^2 \left(
			\frac{x^3}{\ln x}
		\right)
	} - \frac{
		x^3 \cdot \ln x \cdot \left(
			3x^2 \cdot \ln x - x^3 \cdot x^{-1}
		\right)
	}{
		x^6 \cdot \ln^4 \left(
			\frac{x^3}{\ln x}
		\right)
	} \\

	&= \frac{3}{x} - \frac{
		
	}{
	
	} \\
\end{align*}
$$