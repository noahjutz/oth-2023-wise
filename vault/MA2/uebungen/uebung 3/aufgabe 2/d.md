$$
\begin{align*}
	\lim_{n \to \infty} n \cdot (
		1 - \underbrace{
			(1 - \frac{1}{n})^{42}
		}_{\text{Binomischer Lehrsatz}}
	)

	&\stackrel{(5)}{=} \lim_{n \to \infty} n \cdot \Bigg(
		1 - \bigg(
			\colorbox{yellow}{$
				\sum_{k=0}^{42}
				\binom{42}{k} \cdot
				\underbrace{1^{42-k}}_{=1} \cdot
				(-\frac{1}{n})^k
			$}
		\bigg)
	\Bigg) \\

	&= \lim_{n \to \infty} n \cdot \Bigg(
		1-\bigg(
			\sum_{k=0}^{42}
			\binom{42}{k} \cdot
			(-\frac{1}{n})^k
		\bigg)
	\Bigg) \\

	&\stackrel{(7)}{=} \lim_{n \to \infty} n \cdot \Bigg(
		1 - \bigg(
			\colorbox{pink}{$
				\binom{42}{0} \cdot (-\frac{1}{n})^0
			$} +
			\sum_{\colorbox{pink}{$k=1$}}^{42}
			\binom{42}{k} \cdot
			(-\frac{1}{n})^k
		\bigg)
	\Bigg) \\

	&= \lim_{n \to \infty} n \cdot \Bigg(
		1 - \bigg(
			\colorbox{pink}{$1$} +
			\sum_{k=1}^{42}
			\binom{42}{k} \cdot
			(-\frac{1}{n})^k
		\bigg)
	\Bigg) \\

	&\stackrel{(7)}{=} \lim_{n \to \infty} n \cdot \Bigg(
		1 - \bigg(
			1 + \colorbox{lightblue}{$
				\binom{42}{1} \cdot (-\frac{1}{n})^1
			$} +
			\sum_{\colorbox{lightblue}{$k=2$}}^{42}
			\binom{42}{k} \cdot
			(-\frac{1}{n})^k
		\bigg)
	\Bigg) \\

	&= \lim_{n \to \infty} n \cdot \Bigg(
		1 - \bigg(
			1 + \colorbox{lightblue}{$
				42 \cdot (-\frac{1}{n})
			$} +
			\sum_{k=2}^{42}
			\binom{42}{k} \cdot
			(-\frac{1}{n})^k
		\bigg)
	\Bigg) \\

	&= \lim_{n \to \infty} n \cdot \Bigg(
		1 - \bigg(
			1 \colorbox{lightblue}{$- \frac{42}{n}$} +
			\sum_{k=2}^{42}
			\binom{42}{k} \cdot
			(-\frac{1}{n})^k
		\bigg)
	\Bigg) \\

	&\stackrel{(8)}{=} \lim_{n \to \infty} n \cdot \Bigg(
			\frac{42}{n} +
			\sum_{k=2}^{42}
			\binom{42}{k} \cdot
			(-\frac{1}{n})^k
	\Bigg) \\
 
	&= \lim_{n \to \infty}
	42 + n \cdot
	\sum_{k=2}^{42}
	\binom{42}{k} \cdot
	(-\frac{1}{n})^k \\

	&\stackrel{(9)}{=}
	\lim_{n \to \infty} 42 +
	\colorbox{violet}{$\lim_{n \to \infty}$}
	n \cdot
	\sum_{k=2}^{42}
	\binom{42}{k} \cdot
	(-\frac{1}{n})^k \\

	&= \lim_{n \to \infty} 42 +
	\lim_{n \to \infty}
	\sum_{k=2}^{42}
	\binom{42}{k} \cdot
	(-\frac{1}{n})^k 
	\colorbox{yellow}{$\cdot n$} \\
 
	&\stackrel{(9)}{=}
	\underbrace{
		\lim_{n \to \infty} 42
	}_{=42} +
	\sum_{k=2}^{42}
	\underbrace{
		\colorbox{violet}{$\lim_{n \to \infty}$}
		\binom{42}{k} \cdot
		(-\frac{1}{n})^k \cdot n
	}_{=0} \\

	&= 42 + \sum_{k=2}^{42} 0 \\

	&= \colorbox{lightgreen}{$42$}
\end{align*}
$$
