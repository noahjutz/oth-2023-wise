$$
\left(
	\int_0^x \frac{\sin t}{t} \,dt
\right)'
$$

- Ein Integral $\int_a^b f(x) \,dx$ ist $F(b) - F(a)$.
- Die Ableitung eines Integrals ist $f(x)$.

> [!info] 5.7 Hauptsatz der Differential- und Integralrechnung
> $$
> F(x) = \int_a^x f(t) \,dt
> $$

- Die Ableitung des Integrals ist auf $D = [0; \infty[$ definiert.

# Antwort

$$
F'(x) = \frac{\sin x}{x}
$$

# Begründung

Die Ableitung eines Integrals $\int_a^b f(x) \,dx$ ist nach dem HDI (5.7) die Funktion $f(x)$. Man kann auch die Ableitung als $F'(t) = \frac{\sin t}{t}$ definieren, das ist äquivalent. Die Übrigen 2 Optionen wären die zweite Ableitung des Integrals. Man braucht keine feste obere Grenze $x$, um den Integral abzuleiten.

# Alternativ

$$
\begin{align*}
	\frac{d}{dx} \int_0^x \frac{\sin t}{t} \,dt
	&= \frac{d}{dx} \int_0^x g(t) \,dt \\
	&= \frac{d}{dx} \int_0^x G'(t) \,dt \\
	&= \frac{d}{dx} [G(t)]_0^x \\
	&= \frac{d}{dx} (G(x) - G(0)) \\
	&= \frac{d}{dx} G(x) - \frac{d}{dx} G(0) \\
	&= \frac{d}{dx} G(x) - 0 \\
	&= g(x) \\
	&= \frac{\sin x}{x}
\end{align*}
$$

> [!question] Woher weiß ich, dass ich nach x ableite und nicht nach t?
