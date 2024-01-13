# Gegeben

- Größe L
- Host A $\to$ Host B
- MSS = 1460 Byte

# Bearbeitung

- Sequence Number: 32 Bit
- 1460B pro Datagram
- Annahme: Sequenznummer fängt bei 0 an
- Man kann pro Sequenznummer ($2^{32}$ Möglichkeiten) ein Datagram (1460B) schicken.

$$
\begin{align*}
	2^{32} \cdot 1460 \text{B} &= 6\ 270\ 652\ 252\ 000 \text{B} \\
	&\approx 6.3 \text{TB}
\end{align*}
$$

L kann maximal ca. 6.3TB groß sein.

> [!info] TCP-Header
> ![[tcp header.png]]

> [!info] Metrische Präfixe
> ![[metric prefixes.png]]
