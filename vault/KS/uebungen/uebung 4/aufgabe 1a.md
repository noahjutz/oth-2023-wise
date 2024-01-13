# Gegeben

- Größe L
- Host A $\to$ Host B
- MSS = 1460 Byte

# Bearbeitung

- Sequence Number: 32 Bit
- 1460B pro Datagram
- Annahme: Sequenznummer fängt bei 0 an
- Man kann pro Sequenznummer ($2^{32}$ Möglichkeiten) ein ~~Datagram (1460B)~~ Byte schicken.

$$
\begin{align*}
	L = 2^{32} \text{B} &= 2^2 \text{GiB} = 4 \text{GiB}
\end{align*}
$$

L kann maximal ca. 4GiB groß sein.

> [!info] TCP-Header
> ![[KS/uebungen/uebung 4/tcp header.png]]

> [!info] Metrische Präfixe
> ![[KS/uebungen/uebung 4/metric prefixes.png]]
