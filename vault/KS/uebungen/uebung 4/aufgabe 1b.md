# Gegeben

- L = 6 270 652 252 000 Byte
- Header H = 58 Byte
- R = 100Mbps

# Bearbeitung

## Gesamtgröße N

$$
\begin{align*}
	N &= 2^{32} \cdot (1460 + 58) \text{ B} \\
	&= 6.519760355 \cdot 10^{12} \text{ B} \\
	&= 5.215808284 \cdot 10^{13} \text{ b} \\
	&= 5.215808284 \cdot 10^{7} \text{ Mb} \\
\end{align*}
$$

##  Übertragungsdauer t

$$
\begin{align*}
	\text{s} &= \text{Mb} \div \frac{\text{Mb}}{\text{s}} \\
	t &= N \div R \\
	&= 5.215808284 \cdot 10^7 \text{Mb} \div 100 \text{Mbps} \\
	&= 5.215808284 \cdot 10^7 \text{Mb} \cdot 10^{-2} \text{Mbps} \\
	&= 5.215808284 \cdot 10^5 \text{s} \\
	&\approx 6 \text{d}
\end{align*}
$$
