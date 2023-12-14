# Gegeben
- Funktion der Straße: $ax^2$ mit $a$ gesucht
- Statue in $(100|50)$
- Auto in $(-100|100)$

# Straße, durch die Auto geht

$$
\begin{align*}
	f(x) &= ax^2 \\

	f(-100) &= a \cdot (-100)^2 \\

	y &= a \cdot 100^2 \\

	100 &= a \cdot 100^2 \\

	\frac{1}{100} &= a \\\\

	f(x) &= \frac{x^2}{100} \\

	\color{grey}
		f'(x) &
	\color{grey}
		= \frac{2x}{100}
\end{align*}
$$

# Tangente der Straße, durch die Statue geht

> [!info] Tangentengleichung
>
>$$
>t(x) = f(x_0) + f'(x_0) \cdot (x-x_0)
>$$

## Schnittpunkt der Tangente zu $f$

> [!info] Quotientenregel
>$$
>\left(\frac{f}{g}\right)'(x_0) = \frac{
>	f'(x_0) \cdot g(x_0) - f(x_0) \cdot g'(x_0)
>}{
>	g^2(x_0)
>}
>$$

> [!info] Mitternachtsformel
>$$
>x_{1,2} = \frac{-b \pm \sqrt{b^2-4ac}}{2a}
>$$

$$
\begin{align*}
	t(100) &= 50 \\

	f(x_0) + f'(x_0) \cdot (100-x_0) &= 50 \\

	\frac{x_0^2}{100} + \left(\frac{x_0^2}{100}\right)' \cdot (100 - x_0) &= 50 \\

	\frac{x_0^2}{100} + \frac{2x_0 \cdot 100 - x_0^2 \cdot 0}{100^2} \cdot
		(100 - x_0) &= 50 \\

	\frac{x_0^2}{100} + \frac{2x_0}{100} \cdot (100 - x_0) &= 50 \\
 
	\frac{x_0^2}{100} + 2x_0 - \frac{2x_0^2}{100} &= 50 \\
 
	-\frac{x_0^2}{100} + 2x_0 &= 50 \\
 
	-0.01 x_0^2 + 2x_0 - 50 &= 0
\end{align*}
$$

$$
\begin{align*}
	x_0 &= \frac{
		-2 \pm \sqrt{2^2 - 4 \cdot (-0.01) \cdot (-50)}
	}{
		2 \cdot (-0.01)
	} \\
 
	&= 50 \cdot \left( 2 \pm \sqrt{2} \right) \\
	&= \underline{50 \cdot \left( 2 - \sqrt 2\right)}
	\ \text{weil das Auto von links kommt}
\end{align*}
$$

$\implies$ Die Tangente liegt in $\left(50 \cdot \left( 2 - \sqrt 2\right)\middle|f\left(50 \cdot \left( 2 - \sqrt 2\right)\right)\right)$.

## Tangentengleichung

$$
\begin{align*}
	t(x) &= f(x_0) + f'(x_0) \cdot (x-x_0) \\

	&= \frac{x_0^2}{100} + \frac{2x_0}{100} \cdot (x-x_0) \\

	&= \frac{x_0^2}{100} + x \cdot \frac{2x_0}{100} - \frac{2x_0^2}{100} \\
 
	&= \frac{2x_0}{100} x + \frac{x_0^2 - 2x_0^2}{100} \\

	&\approx \underline{0.586x - 8.579}
\end{align*}
$$

# Antwort
Das Auto befindet sich (ungefähr) im Punkt $(29.289|8.579)$, wenn die Scheinwerfer die Statue anstrahlen.

![[aufgabe_2_diagram.svg]]
- Blau: Straße
- Orange: Auto (Startpunkt)
- Grün: Statue
- Lila: Scheinwerfer
