$$
\lim_{n \to \infty} n^2 - \sqrt{n^4 + 3n^2 + 2} = \text{?}
$$
**Optionen**
- Divergenz beweisen $\to$ (s7)
- Grenzwert berechnen
	- Sandwichtheorem
	- Auf wichtige Reihen zurückführen $\to$ (s15)
	- Auf wichtige Grenzwerte zurückführen $\to$ (s8)
	- $\lim$-Regeln $\to$ (s7)

**Bearbeitung**
Umformen mit 3. binom. Formel

$$
\begin{align*}
	\lim_{n \to \infty} n^2 - \sqrt{n^4+3n^2+2}
 
	&= \lim_{n \to \infty} n^2 - \sqrt{n^4+3n^2+2} 
	\cdot \colorbox{yellow}{$\frac{n^2+\sqrt{n^4+3n^2+2}}{n^2+\sqrt{n^4+3n^2+2}}$} \\
 
	&= \lim_{n \to \infty}  \frac{(n^2 - \sqrt{n^4+3n^2+2}) \cdot (n^2+\sqrt{n^4+3n^2+2})}{n^2+\sqrt{n^4+3n^2+2}} \\
 
	&\stackrel{(4)}{=} \lim_{n \to \infty} \frac{
		\colorbox{yellow}{$
			(n^2)^2-(\sqrt{n^4+3n^2+2})^2
		$}
	}{
		n^2+\sqrt{n^4+3n^2+2}
	} \\
 
	&= \lim_{n \to \infty} \frac{
		n^4-(n^4+3n^2+2)
	}{
		n^2+\sqrt{n^4+3n^2+2}
	} \\
 
	&= \lim_{n \to \infty} \frac{
		-3n^2-2
	}{
		n^2+\sqrt{n^4+3n^2+2}
	} \\
 
	&= \lim_{n \to \infty} \frac{
		-3n^2-2
	}{
		n^2+\sqrt{n^4+3n^2+2}
	} \cdot \colorbox{yellow}{$\frac{\frac{1}{n^2}}{\frac{1}{n^2}}$} \\
 
	&= \lim_{n \to \infty} \frac{
		\frac{-3n^2-2}{n^2}
	}{
		\frac{n^2+\sqrt{n^4+3n^2+2}}{n^2}
	} \\

	&= \lim_{n \to \infty} \frac{
		\frac{-3n^2}{n^2}-\frac{2}{n^2}
	}{
		\frac{n^2}{n^2} + \frac{\sqrt{n^4+3n^2+2}}{n^2}
	} \\

	&= \lim_{n \to \infty} \frac{
		\frac{-3n^2}{n^2}-\frac{2}{n^2}
	}{
		\frac{n^2}{n^2}+\sqrt{
			\colorbox{yellow}{$
				\frac{n^4+3n^2+2}{(n^2)^2}
			$}
		}
	} \\

	&= \lim_{n \to \infty} \frac{
		-3-\frac{2}{n^2}
	}{
		1+\sqrt{\frac{n^4}{n^4}+\frac{3n^2}{n^4}+\frac{2}{n^4}}
	} \\

	&= \lim_{n \to \infty} \frac{
		-3-\frac{2}{n^2}
	}{
		1+\sqrt{1+\frac{3}{n^2}+\frac{2}{n^4}}
	} \\
	
	&\stackrel{(2)}{=} \frac{
		\lim_{n \to \infty} -3-\frac{2}{n^2}
	}{
		\lim_{n \to \infty} 1+\sqrt{1+\frac{3}{n^2}+\frac{2}{n^4}}
	} \\

	&= \colorbox{lightgreen}{$\frac{-3}{2}$}
\end{align*}
$$