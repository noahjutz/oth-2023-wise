$$
\sum_{n=0}^{\infty}\Big( \frac{1}{2^n} + \frac{1}{3^n} \Big) \cdot x^n
$$

# Formeln
## Potenzreihe
$$
\sum_{n=0}^{\infty} a_n (x-x_0)^n
$$

## Quotientenmethode
$$
q = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|,\ r = \frac{1}{q}
$$

## Wurzelmethode
$$
w = \sqrt[n]{\left|a_n\right|},\ r = \frac{1}{w}
$$

# Versuch 1
$$
\begin{align*}
	a_n &= \Big( \frac{1}{2^n} + \frac{1}{3^n} \Big) \cdot x^n \\

	&= \Big( 
		\frac{3^n}{3^n} \cdot \frac{1}{2^n} + \frac{2^n}{2^n} \cdot \frac{1}{3^n}
	\Big) \cdot x^n \\

	&= \Big(
		\frac{3^n+2^n}{3^n \cdot 2^n}
	\Big) \cdot x^n \\

	&= \frac{3^n + 2^n}{5^n} \cdot x^n \\

	&= \Big(
		\frac{(3^n+2^n)^\frac{1}{n}}{5}
	\Big)^n \cdot x^n
\end{align*}
$$
> [!error] Falsch
> Richtig wäre $a_n = \frac{1}{2^n} + \frac{1}{3^n}$

## Wurzelmethode
$$
\begin{align*}
	w &= \lim_{n \to \infty} \sqrt[n]{\left|a_n\right|} \\

	&= \lim_{n \to \infty} \sqrt[n]{\left| 
		\Big(
			\frac{(3^n+2^n)^\frac{1}{n}}{5} \cdot x
		\Big)^n
	\right|} \\
 
	&= \lim_{n \to \infty} \sqrt[n]{
		\Big(
			\frac{(3^n+2^n)^\frac{1}{n}}{5} \cdot x
		\Big)^n
	} \\

	&\stackrel{!}{=} \lim_{n \to \infty} \frac{(3^n+2^n)^\frac{1}{n}}{5} \\

	&= \lim_{n \to \infty} \frac{\sqrt[n]{3^n+2^n}}{5} \\

	&= \lim_{n \to \infty} \frac{
		\sqrt[n]{3^n \cdot \big(1 + (\frac{2}{3})^n \big)}
	}{5} \\

	&= \lim_{n \to \infty} \frac{
		3 \cdot \sqrt[n]{
			1 + \underbrace{
				( \frac{2}{3} )^n
			}_{\to 0}
		}
	}{5} \\

	&= \lim_{n \to \infty} \frac{3 \cdot \sqrt[n]{1}}{5} = \frac{3}{5}
\end{align*}
$$
$$
\implies r = \frac{5}{3}
$$
> [!error] Falsch
> - Folgefehler, $a_n \ne \Big( \frac{1}{2^n} + \frac{1}{3^n} \Big) \cdot x^n$
> - Bei (!) vergessen, x mitzunehmen

# Versuch 2
$$
\sum_{n=0}^{\infty}\Big( \frac{1}{2^n} + \frac{1}{3^n} \Big) \cdot x^n =
\sum_{n=0}^{\infty}  \underbrace{
	\Big(
		\frac{1}{2^n} + \frac{1}{3^n}
	\Big)
}_{a_n} \cdot (x - \underbrace{0}_{x_0})^n
$$

## Wurzelmethode
$$
\begin{align*}
	w &= \lim_{n \to \infty} \sqrt[n]{\left| a_n \right|} \\

	&= \lim_{n \to \infty} \sqrt[n]{\left| 2^{-n} + 3^{-n} \right|} \\

	&= \lim_{n \to \infty} \sqrt[n]{2^{-n}+3^{-n}} \\

	&= \lim_{n \to \infty} \sqrt[n]{
		2^{-n} \cdot \bigg(
			1 + \Big(\frac{3}{2}\Big)^{-n}
		\bigg)
	} \\
 
	&= \lim_{n \to \infty} \sqrt[n]{
		\Big(\frac{1}{2}\Big)^n \cdot \bigg(
			1 + \Big(\frac{2}{3}\Big)^n
		\bigg)
	} \\

	&= \lim_{n \to \infty} \frac{1}{2} \cdot \sqrt[n]{
		1 + \Big(\frac{2}{3}\Big)^n
	} \\
 
	&= \frac{1}{2} \cdot \lim_{n \to \infty} \sqrt[n]{1} \\

	&= \frac{1}{2} \cdot 1 = \frac{1}{2} \\
\end{align*}
$$
$$
\implies r = \frac{1}{w} = 2
$$

> [!check] Richtig

> [!question] Frage
> Ist das weglassen der Betragstriche hier erlaubt? (Begründung: mit $n \in \mathbb{N}$ kann die Summe nicht negativ sein)

> [!question] Frage
> Kann man hier nicht auch auf $w = \frac{1}{3}$ kommen, wenn man anders ausklammert?
> >[!check] Antwort
> > Nein, weil $(\frac{3}{2})^n$  divergiert, ist also unbrauchbar
