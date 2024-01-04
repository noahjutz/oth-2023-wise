# Gegeben

$$
\begin{gather*}
	P_0 = (3, 2) \\
	P_1 = (0, ?) \\
	P_2 = (?, 0) \\
	m < 0
\end{gather*}
$$

# Geradengleichung

Die Gerade g sei definiert als $g(x) = mx + t$.

$$
\begin{alignat*}{2}
	&& y &= m \cdot x + t \\
	\iff&& 2 &= m \cdot 3 + t \\
	\iff&& t &= -3m + 2 \\
	\iff&& m &= \frac{2-t}{3} \\
\end{alignat*}
$$

# Dreiecksgleichung

$$
A = \frac{P_1^x \cdot P_2^y}{2}
$$

$$
\begin{align*}
	P_2^y &= g(0) = m \cdot 0 + t = t \\
	P_1^x &= -\frac{t}{m}
\end{align*}
$$

$$
\begin{align*}
	A(m) &= -\frac{t \cdot \frac{t}{m}}{2} \\
	&= -\frac{t^2}{2m} \\
	&= -\frac{(-3m+2)^2}{2m} \\
	&= -\frac{4-12m+9m^2}{2m} \\
	&= \frac{-4+12m-9m^2}{2m} \\
	&= -2m^{-1} + 6 - \frac{9}{2}m
\end{align*}
$$

# Maximieren

## Hauptfunktion definieren

$$
A(m) = -2m^{-1} + 6 - \frac{9}{2}m
$$

## Definitionsbereich angeben

$$
D =\left]-\infty; 0\right[
$$

## Ableitung bestimmen

$$
A'(m) = 2m^{-2}-\frac{9}{2}
$$

## Nullstellen der Ableitung bestimmen

$$
\begin{align*}
	A'(m) &= 0 \\
	2m^{-2}-\frac{9}{2} &= 0 \\
	\frac{2}{m^2} &= \frac{9}{2} \\
	\frac{m^2}{2} &= \frac{2}{9} \\
	m^2 &= \frac{4}{9} \\
	m &= \sqrt \frac{4}{9} \\
	&= \pm \frac{2}{3}
\end{align*}
$$

## Definitionsbereich prüfen

$-\frac{2}{3} \notin D \implies$ nur $\frac{2}{3}$ kommt in Frage.

## Hinreichende Bedingung für Extremum

- $n = 2$
- $x_0 = \frac{2}{3}$

Es gilt

$A'(x_0) = 0$

## Antwort

Das Dreieck hat bei einer Steigung $m = -\frac{2}{3}$ den minimalen Flächeninhalt mit $A\left(-\frac{2}{3}\right) = 12$.

> [!NOTE] Beachte
> - Minus vor Bruch $\implies$ Summen invertieren.
> - Das Extremum muss nicht angenommen werden, siehe 4.25 Hinreichende Bedingung für Extremum

