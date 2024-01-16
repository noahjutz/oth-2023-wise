$$
\begin{align*}
	\int_0^\infty e^{-x} \,dx
	&= \lim_{R \to \infty} \int_0^R e^{-x} \,dx \\
	&= \lim_{R \to \infty} \left[
		-e^{-x}
	\right]_0^R \\
	&= \lim_{R \to \infty} -e^{-R} - (-e^0) \\
	&= -\underbrace{
		\lim_{R \to \infty} \frac{1}{e^R}
	}_{= 0} + 1 \\
	&= \underline{1}
\end{align*}
$$


> [!warning] Hier gehört kein +c hin.
