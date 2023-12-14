$$
\sum_{n=1}^{\infty} \frac{\sin(n)}{n^2}
$$

# Notwendiges Kriterium
$$
\lim_{n \to \infty} \frac{\sin(n)}{n^2} = 0
\text{, weil } \mathbb{D}_{\sin(n)} = [-1, 1]
$$

# Quotientenkriterium
$$
\begin{align*}
	q &= \lim_{n \to \infty} \left|
		\frac{
			\frac{\sin(n+1)}{(n+1)^2}
		}{
			\frac{\sin(n)}{n^2}
		}
	\right| \\

	&= \lim_{n \to \infty} \left|
		\frac{\sin(n+1)}{(n+1)^2} \cdot
		\frac{n^2}{\sin(n)}
	\right| \\
	 
	&= \lim_{n \to \infty} \left|
		\frac{
			\sin(n+1) \cdot n^2
		}{
			(n+1)^2 \cdot \sin(n)
		}
	\right| \\
 
	&= \lim_{n \to \infty} \left|
		\frac{
			n^2 \cdot \Big(
				\sin(n) \cdot \cos(1) +
				\cos(n) \cdot \sin(1)
			\Big)
		}{
			(n^2+2n+1) \cdot \sin(n)
		}
	\right| \\

	&= \lim_{n \to \infty} \left|
		\frac{
			n^2 \cdot \Big(
				\sin(n) \cdot \cos(1) +
				\cos(n) \cdot \sin(1)
			\Big)
		}{
			\sin(n) \cdot n^2 + \sin(n) \cdot 2n + \sin(n) \cdot 1
		}
	\right| \\

	&= \lim_{n \to \infty} \left|
		\frac{
			n^2 \cdot \Big(
				\sin(n) \cdot \cos(1) +
				\cos(n) \cdot \sin(1)
			\Big)
		}{
			n^2 \cdot \Big(
				\sin(n) + \frac{\sin(n) \cdot 2}{n} + \frac{\sin(n)}{n}
			\Big)
		}
	\right| \\
 
	&= \lim_{n \to \infty} \left|
		\frac{
			\sin(n) \cdot \cos(1) + \cos(n) \cdot \sin(1)
		}{
			\sin(n) + \frac{\sin(n) \cdot 2}{n} + \frac{\sin(n)}{n}
		}
	\right| \\

	&= \lim_{n \to \infty} \left|
		\frac{
			\sin(n) \cdot \cos(1) + \cos(n) \cdot \sin(1)
		}{
			\sin(n)
		}
	\right| \\

	&= \lim_{n \to \infty} \left|
		\cos(1) +
		\sin(1) \cdot
		\frac{
			\cos(n)
		}{
			\sin(n)
		}
	\right| \\

	&= \cos(1) + \sin(1) \cdot \lim_{n \to \infty} \left|
		\frac{
			\cos(n)
		}{
			\sin(n)
		}
	\right| \\

	&= \cos(1) + \sin(1) \cdot \lim_{n \to \infty} \left|
		\tan(n)
	\right| \\
 
\end{align*}
$$
$$
\begin{gather*}
	\implies q \text{ existiert nicht.} \\
	\implies \text{Keine Aussage über Konvergenz/Divergenz.}
\end{gather*}
$$


> [!question] Frage
> - Erhält man für eine Folge $a_n$ immer die gleichen Werte $w = q$?
> - Lohnt es sich, das Wurzelkriterium anzuwenden, wenn das Quotientenkriterium kein $q$ bzw. $q=1$ liefert? (und andersherum)

# Majoranten-Kriterium
$$
\begin{gather*}
	A_k = \frac{\sin(k)}{k^2} \\
	B_k := \frac{1}{k^2}
\end{gather*}
$$

## z.z.: $|A_k| \le B_k$
$$
\begin{align*}
	\frac{\sin(k)}{k^2} &\le \frac{1}{k^2} \\

	\sin(k) &\le 1 \ \checkmark \ \text{da} \ D=[-1,1]
\end{align*}
$$

## z.z.: $\sum_{k=1}^{\infty} B_k$ konvergent
$\sum_{k=1}^{\infty} B_k$ ist die verallgemeinerte harmonische Reihe mit $a > 1$ $\implies$ $B_k$ ist konvergent

## Antwort
$$
\implies \sum_{k=1}^{\infty} \frac{\sin(k)}{k^2} \ \text{ist konvergent.}
$$
