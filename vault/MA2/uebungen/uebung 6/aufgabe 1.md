$$
f(x) = \left\{
	\begin{align*}
		&x-2 &\text{für } x < 2 \\
		&\frac{(x-1)^2}{2} - \frac{1}{2} &\text{für } x \ge 2
	\end{align*}
\right.
$$

# Untersuche auf Differenzierbarkeit
$$
x_0 = 2
$$
## Stetigkeit in $x_0$
$f$ ist stetig in $x_0 \in D$, falls $\lim_{x \to x_0} f(x) = f(x_0)$.

$$
f(x_0) = f(2) = \underline{0}
$$

### Linksseitiger Grenzwert

$$
\lim_{x \nearrow x_0} f(x) = \lim_{x \nearrow 2} x - 2 = \underline{0}
$$

### Rechtsseitiger Grenzwert

$$
\begin{align*}
	\lim_{x \searrow x_0} f(x) &=
		\lim_{x \searrow 2} \frac{(x-1)^2}{2} - \frac{1}{2} \\

	&= -\frac{1}{2} + \frac{1}{2} \left(
		\lim_{x \searrow 2} x-1
	\right)^2 \\

	&= -\frac{1}{2} + \frac{1}{2} (1)^2 \\

	&= \underline{0}
\end{align*}
$$

### Folgerung

$$
f(x_0) = \lim_{x \to x_0} f(x) = 0 \implies f \text{ ist stetig in } x_0.
$$

## Differenzierbarkeit in $x_0$
$f$ ist differenzierbar in $x_0 \in D$, falls $f$ stetig ist und der Grenzwert $f'(x)$ existiert.

### Linksseitiger Grenzwert

$$
\begin{align*}
	f'(x_0) &= \lim_{x \nearrow x_0} \frac{f(x) - f(x_0)}{x-x_0} \\

	&= \lim_{x \nearrow 2} \frac{f(x) - f(2)}{x-2} \\

	&= \lim_{x \nearrow 2} \frac{f(x)}{x-2} \\

	&= \lim_{\epsilon \searrow 0} \frac{f(2 - \epsilon)}{-\epsilon} \\

	&= \lim_{\epsilon \searrow 0} -\frac{1}{\epsilon} \cdot (2 - \epsilon - 2) \\

	&= \lim_{\epsilon \searrow 0}-\frac{1}{\epsilon} \cdot (-\epsilon) \\

	&= \underline{1}
\end{align*}
$$

### Rechtsseitiger Grenzwert

$$
\begin{align*}
	f'(x_0) &= \lim_{x \searrow x_0} \frac{f(x) - f(x_0)}{x - x_0} \\

	&= \lim_{x \searrow 2} \frac{f(x) - f(2)}{x - 2} \\

	&= \lim_{x \searrow 2} \frac{f(x)}{x-2} \\

	&= \lim_{\epsilon \searrow 0} \frac{f(2+\epsilon)}{\epsilon} \\

	&= \lim_{\epsilon \searrow 0} \frac{1}{\epsilon} \cdot \left(
		\frac{(2+\epsilon-1)^2}{2} - \frac{1}{2}
	\right) \\

	&= \lim_{\epsilon \searrow 0} \frac{1}{\epsilon} \cdot \left(
		\frac{(1+\epsilon)^2 - 1}{2}
	\right) \\
 
	&= \lim_{\epsilon \searrow 0} \frac{1}{\epsilon} \cdot \left(
		\frac{1+2\epsilon+\epsilon^2 - 1}{2}
	\right) \\

	&= \lim_{\epsilon \searrow 0} \frac{1}{\epsilon} \cdot \left(
		\frac{2\epsilon+\epsilon^2}{2}
	\right) \\

	&= \lim_{\epsilon \searrow 0} \frac{1}{\epsilon} \cdot \left(
		\epsilon + \frac{\epsilon^2}{2}
	\right) \\

	&= \lim_{\epsilon \searrow 0} 1 + \frac{\epsilon}{2} \\

	&= \underline{1}
\end{align*}
$$

### Folgerung
$f'(x_0)$ existiert $\implies f$ ist differenzierbar in $x_0$.

# Antwort
$f$ ist in $x_0 = 2$ differenzierbar. $f$ hat in $x_0 = 2$ einen Funktionswert von $0$ und eine Steigung von $1$.


