# Gegeben

- Rechteck: $h \cdot b$
- Dreieck: $\frac{1}{2} \cdot 5 \cdot 10$

# Bearbeitung

Wir stellen die Fläche des Rechtecks als Funktion in abhängigkeit der Breite des Rechtecks auf:

$$
\begin{gather*}
	A_\square = \underbrace{h}_{=f(x)} \cdot \underbrace{b}_{=x} \\
	\implies A_\square(x) = f(x) \cdot x
\end{gather*}
$$

Betrachten wir das Dreieck als die Fläche unter einer Geraden im 1. Quadranten des Koordinatensystems, so ist diese Gerade definiert als:

$$
f(x) = -\frac{5}{10}x + 5
$$

Die Funktion, die die Fläche des Rechtecks in Abhängigkeit der Breite $x \in \left]0, 10\right[$ beschreibt, lautet also:

$$
A_\square(x) = -\frac{1}{2}x^2+5x
$$

Die Extremwerte dieser Funktion sind die Nullstellen der Ableitung.

$$
\begin{align*}
	A_\square'(x) &= 0 \\
	-x + 5 &= 0 \\
	-x &= -5 \\
	x &= 5
\end{align*}
$$

Die maximale Fläche ist im Extremwert $x = 5$.

$$
\begin{align*}
	A_\square(5) &= -\frac{1}{2} \cdot 5^2 + 5 \cdot 5 \\
	&= 25-\frac{25}{2} \\
	&= 12.5
\end{align*}
$$

Aus den obigen Definitionen $b = x$ und $h = f(x)$ ergibt sich:

$$
b = x = \boxed{5}
$$

$$
h = f(x) = f(5) = -\frac{1}{2} \cdot 5 + 5 = \boxed{2.5}
$$
