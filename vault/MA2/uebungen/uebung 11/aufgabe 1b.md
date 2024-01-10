> [!info] 5.11 Substitutionsregel
> $$
> \int_a^b f(g(x)) \cdot g'(x) = \int_{g(a)}^{g(b)} f(t) \,dt
> $$
> wobei $t = g(x)$.

# Ohne berücksichtigung der Grenzen

> [!question] Ist das weglassen der Grenzen des Integrals erlaubt?

$$
\int te^{t^2} \,dt = \frac{1}{2} \int
	\underbrace{2t}_{g'(t)} \cdot
	\underbrace{
		e^{\overbrace{
			t^2
		}^{g(t)}}
	}_{f(t)} \,dt = \ldots
$$

> [!note] Substitution
> $$
> x = g(t) = t^2
> $$

$$
\begin{align*}
	\ldots &= \frac{1}{2} \int e^{x} \,dx \\
	&= \frac{1}{2} e^x + c
\end{align*}
$$

> [!note] Rücksubstitution
> $$
> x = g(t) = t^2
> $$

$$
\ldots = \underline{\frac{1}{2} e^{t^2} + c}
$$

# Unter Berücksichtigung der Grenzen

$$
\begin{align*}
	\int te^{t^2} \,dt &\overset{?}{=} \int_a^bte^{t^2} \,dt \\
	&= \frac{1}{2} \int_a^b 2t \cdot e^{t^2} \,dt \\
	&= \frac{1}{2} \int_{g(a)}^{g(b)} e^x \,dt &\text{(Substitution)} \\
	&= \frac{1}{2} \bigg[ e^x \bigg]_{g(a)}^{g(b)} \\
	&= \frac{1}{2} \left( e^{g(b)} - e^{g(a)} \right) + \tilde c \\
	&= \frac{1}{2} \left( e^{b^2} - e^{a^2} \right) + \tilde c \\
	&= \frac{1}{2} e^{b^2} + c \\
	&\overset{?}{=} \frac{1}{2} e^{t^2} + c
\end{align*}
$$


> [!question] Sind der erste und letzte Schritt erlaubt?
