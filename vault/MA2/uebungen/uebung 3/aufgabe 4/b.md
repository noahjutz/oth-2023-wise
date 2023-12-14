# Folge Fördermenge
$$
\begin{gather*}
	a_1 := 250 \cdot 10^6 \\
	a_{n+1} := a_n \cdot 0.98 \\
	\iff \\
	a_n := 250 \cdot 10^6 \cdot 0.98^{n-1}
\end{gather*}
$$

# Reihe Verbrauch über $n$ Jahre
$$
\begin{alignat*}{2}
	&\qquad&
	13 \cdot 10^9 - \sum_{k=1}^{n} \Big(
		250 \cdot 10^6 \cdot 0.98^{k-1}
	\Big) &= 0 \\

	&\iff&
	13 \cdot 10^9 - \sum_{\colorbox{yellow}{$k=0$}}^{\colorbox{yellow}{$n-1$}} \Big(
		250 \cdot 10^6 \cdot 0.98^\colorbox{yellow}{$k$}
	\Big) &= 0 \\
 
	&\iff&
	\sum_{k=0}^{n-1} \Big(
		250 \cdot 10^6 \cdot 0.98^k
	\Big)
	&= \colorbox{yellow}{$13 \cdot 10^9$} \\

	&\iff&
	\sum_{k=0}^{n-1} 0.98^k &=
	\frac{13 \cdot 10^9}{\colorbox{yellow}{$250 \cdot 10^6$}} \\

	&\stackrel{2.9}{\iff}&
	\colorbox{yellow}{$\frac{1 - 0.98^n}{1-0.98}$}
	&= \frac{1300}{25} \\

	&\iff&
	1-0.98^n
	&= \frac{1300 \colorbox{yellow}{$\cdot 0.02$}}{25} \\

	&\iff&
	-0.98^n
	&= \frac{26}{25} \colorbox{yellow}{$- 1$} \\

	&\iff&
	0.98^n
	&= 1 - \frac{26}{25} \\

	&\iff&
	0.98^n
	&= -\frac{1}{25} \\

	&\iff&
	\log_{0.98} 0.98^n
	&= \underbrace{\log_{0.98} -\frac{1}{25}}_\text{nicht definiert}
\end{alignat*}
$$
$$
\implies \text{Die Reserven werden nie erschöpft sein.}
$$

# Alternativ: Unendliche Reihe ($n = \infty$)
$$
\begin{align*}
	\sum_{k=0}^{\infty} 250 \cdot 10^6 \cdot 0.98^k &= 250 \cdot 10^6 \cdot \sum_{k=0}^{\infty} 0.98^k \\

	&= 250 \cdot 10^6 \cdot \frac{1}{1-0.98} \\

	&= 250 \cdot 10^6 \cdot 50 \\

	&= 12.5 \cdot 10^9 \\

	&< 13 \cdot 10^9
\end{align*}
$$
$$
\implies \text{Die Reserven werden nie erschöpft sein.}
$$
> [!check] Richtig
