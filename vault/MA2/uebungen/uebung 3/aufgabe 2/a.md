$$
\begin{align*}
	\lim_{n \to \infty} \frac{(2^n-6)^2}{2\cdot4^n+1}
	&\stackrel{(1)}{=}
	\lim_{n \to \infty} \frac{(2^n)^2-2\cdot2^n\cdot6+6^2}{2\cdot4^n+1} \\
	&=\lim_{n \to \infty} \frac{4^n - 12 \cdot 2^n + 36}{2 \cdot 4^n + 1} \\
	&=\lim_{n \to \infty} \frac{2^{2n} - 12 \cdot 2^n + 36}{2 \cdot 2^{2n} + 1} \\
	&=\lim_{n \to \infty} \frac{2^{2n}}{2^{2n}} \cdot \frac{1 - \frac{12}{2^{n}} + \frac{36}{2^{2n}}}{2 + \frac{1}{2^{2n}}} \\
	&\stackrel{(2)}{=} \frac{\lim_{n \to \infty}1 - \frac{12}{2^n} + \frac{36}{2^{2n}}}{\lim_{n \to \infty} 2 + \frac{2}{2^{2n2}}} \\
	&=\frac{1}{2}
\end{align*}
$$
