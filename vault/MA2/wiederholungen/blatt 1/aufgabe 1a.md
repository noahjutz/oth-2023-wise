$$
a_n = (-1)^n \cdot n + n^2
$$

$a_n$ ist monoton wachsend. Beweis:

# Induktionsanfang, n=1

$$
\begin {align*}
	a_n &\le a_{n+1} \\
	a_1 &\le a_2 \\
	(-1)^1 \cdot 1 + 1^2 &\le (-1)^2 \cdot 2 + 2^2 \\
	0 &\le 6 \ \checkmark
\end{align*}
$$

# Induktionsschritt, n -> n+1

Wir setzen voraus, dass $a_n \le a_{n+1}$ (Induktionsvoraussetzung). Zu zeigen ist $a_{n+1} \le a_{n+2}$.

$$
\begin{align*}
	&& a_{n+1} &\le a_{n+2} \\
	\overset{\text{IV}}{\iff} && a_n &\le a_{n+2} \\
	\iff && (-1)^n \cdot n + n^2 &\le (-1)^{n+2} \cdot (n+2) + (n+2)^2 \\
	\iff && (-1)^n \cdot n + n^2 &\le (-1)^n \cdot n + 2 \cdot (-1)^n + (n+2)^2
		&&|-((-1)^n \cdot n) \\
	\iff && 0 &\le \underbrace{2 \cdot (-1)^n}_{\in \{-2; 2\}} + (n+2)^2 \\
	\impliedby && 0 &\le -2 + (n+2)^2 \\
	\iff && 0 &\le n^2 + 4n + 2
\end{align*}
$$

Da $n \in \mathbb{N}$ gilt die obige Aussage. $\blacksquare$
