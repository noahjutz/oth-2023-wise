# Definitionen
[[1_layer1.pdf#page=34|Bitfehlerrate]]
$$
\text{BER} := \frac{N_\text{err}}{N_\text{total}}
$$

# Zahlen
Anzahl Rahmen: $a_1 = 10$
Fehlerquote $\text{BER} = 0.2$
Anzahl Übertragungen $x = \ ?$

# Bearbeitung
## Annahme 1: Mit Fehlerüberwachung
### Folge der Anzahl an Rahmen
#### Rekursiv
$$
\begin{gather*}
	a_1 := 10 \\
	a_{n+1} := a_n \cdot \text{BER} = a_n \cdot 0.2
\end{gather*}
$$

#### Explizit
$$
a_n := 10 \cdot (0.2)^{n-1}
$$

### Reihe der Anzahl an Rahmen
$$
\begin{align*}
	\sum_{k=1}^{\infty} a_k &= \sum_{k=0}^{\infty} 10 \cdot 0.2^k \\

	&= 10 \cdot \underbrace{
		\sum_{k=0}^{\infty} 0.2^k
	}_\text{Geom. Reihe} \\

	&= 10 \cdot \frac{1}{1-0.2} \\

	&= 10 \cdot 1.25 \\

	&= 12.5
\end{align*}
$$

### Antwort
Es müssen durchschnittlich $\sum_{k=0}^{\infty} (10 \cdot 0.2^k) = \underline{12.5}$ Fragmente geschickt werden.

> [!warning] Falsche Annahme
> Diese Lösung geht davon aus, dass der Sender eine Fehlererkennung implementiert, die nach dem Senden eines Rahmens sofort weiß, welche Fragmente fehlerhaft sind. Es wird also nicht berücksichtigt, dass bei der Rückmeldung des Empfängers bzgl. Fehlerhafter Bits eine Latenz entsteht.

## Annahme 2: Ohne Fehlerüberwachung
$$
\begin{align*}
	&X := \text{Versuche bis zum ersten Treffer} \\
	\implies &X \sim G(\pi = 0.8^{10})
	\ \color{gray}\text{(X ist geometrisch verteilt)} \\
	\implies &E(X) =
		\frac{1}{\pi} =
		\frac{1}{0.8^{10}} \simeq
		\underline{9.3} \ \checkmark \\
\end{align*}
$$

> [!NOTE]
> Bei dieser Lösung handelt es sich um 9.3 **Rahmen**, während es sich bei der vorherigen Lösung um 12.5 **Fragmente** handelt. 1 Rahmen = 10 Fragmente.

# Experimente
$$
\begin{align*}
	P(X=2) &= (1 - \pi)^{n-1} \cdot \pi \\
 
	&= (1 - 0.8)^{2-1} \cdot 0.8 \\

	&= 0.2 \cdot 0.8 \\
	
	&= 0.16
\end{align*}
$$

$$
\begin{align*}
	P(X \le 2) &= P(X=1) + P(X=2) \\
	&= 0.8 + 0.16 \\
	&= 0.96
\end{align*}
$$
$$
P(X=3) = 0.2^2 \cdot 0.8 = 0.04 \cdot 0.8 = 0.032
$$

$$
\begin{align*}
	\rlap{\text{z.z.: } P(X \in \mathbb{N}) = 1}\\
	P(X \ge 1) &= \sum_{k=1}^{\infty} 0.2^{k-1} \cdot 0.8 \\
	&= 0.8 \cdot \sum_{k=0}^{\infty} 0.2^k \\
	&= 0.8 \cdot \frac{1}{1-0.2} \\
	&= 0.8 \cdot 1.25 \\
	&= 1 \ \blacksquare
\end{align*}
$$
