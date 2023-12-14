$$
\sum_{k=0}^{\infty} \frac{(2k)!}{(k!)^k} \cdot (x+2)^k =

\sum_{k=0}^{\infty} \underbrace{
	\frac{(2k)!}{(k!)^k}
}_{a_k} \cdot \big( x - \underbrace{
	(-2)
}_{x_0} \big)^k
$$

# Bearbeitung
$$
a_n = \frac{(2n)!}{(n!)^n}
$$

## Quotientenmethode
$$
\begin{align*}
	q &= \lim_{n \to \infty} \left|
		\frac{
			a_{n+1}
		}{
			a_n
		}
	\right| \\

	&= \lim_{n \to \infty} \left|
		\frac{
			\frac{
				(2n+2)!
			}{
				\big( (n+1)! \big)^{n+1}
			}
		}{
			\frac{
				(2n)!
			}{
				(n!)^n
			}
		}
	\right| \\

	&= \lim_{n \to \infty} \left|
		\frac{
			(2n+2)!
		}{
			\big( (n+1)! \big)^{n+1}
		} \cdot
		\frac{
			(n!)^n
		}{
			(2n)!
		}
	\right| \\

	&= \lim_{n \to \infty}
		\frac{
			(2n+2)!
		}{
			\big( (n+1)! \big)^{n+1}
		} \cdot
		\frac{
			(n!)^n
		}{
			(2n)!
		} \\

	&= \lim_{n \to \infty}
		\frac{
			(2n)! \cdot (2n+1) \cdot (2n+2)
		}{
			(n!)^{n+1} \cdot (n+1)^{n+1}
		} \cdot \frac{
			(n!)^n
		}{
			(2n)!
		} \\

	&= \lim_{n \to \infty}
		\frac{
			(2n)! \cdot (2n+1) \cdot (2n+2) \cdot (n!)^n
		}{
			(n!)^{n+1} \cdot (n+1)^{n+1} \cdot (2n)!
		} \\

	&= \lim_{n \to \infty}
		\frac{
			(2n+1) \cdot (2n+2)
		}{
			(n!) \cdot (n+1)^{n+1}
		} \\
  
	&= \lim_{n \to \infty}
		\frac{
			(2n+1) \cdot 2 \cdot (n+1)
		}{
			(n!) \cdot (n+1)^{n+1}
		} \\
  
	&= \lim_{n \to \infty}
		\frac{
			(2n+1) \cdot 2
		}{
			(n!) \cdot (n+1)^n
		} \\

	&= \lim_{n \to \infty}
		\frac{
			4 \cdot (n+\frac{1}{2})
		}{
			(n!) \cdot (n+1)^n
		} \\

	&\le \lim_{n \to \infty}
		\frac{
			4 \cdot (n+1)
		}{
			(n!) \cdot (n+1)^n
		} \\

	&= \lim_{n \to \infty}
		\frac{
			4
		}{
			(n!) \cdot (n+1)^{n-1}
		} \\

	&= 0
\end{align*}
$$
$$
\implies r = \frac{1}{q} = \frac{1}{0} = \infty
$$

> [!danger] Alte Lösung (Falsch)
> $$
> \begin{align*}
> \dots &\stackrel{\text{L'H}}{=} \lim_{n \to \infty}
>	\frac{
>		\big( 4n+2 \big)'
>	}{
>		\big( (n+1)^{n-1} \big)'
>	} \\
>
>&= \lim_{n \to \infty}
>	\frac{
>		4
>	}{
>		(n-1) \cdot (n+1)^{n-2} \cdot 1
>	} \\
>
>&= \lim_{n \to \infty}
>	\frac{
>		4
>	}{
>		(n-1) \cdot (n+1) \cdot (n+1)^{n-3}
>	} \\
>
>&= \lim_{n \to \infty}
>	\frac{
>		4
>	}{
>		(n^2-1) \cdot (n+1)^{n-3}
>	} \\
>
>&= 0
>\end{align*}
>$$
