# Gegeben

- Datei: $L = 2^{32} \text{B}$
- MSS: $S = 1460 \text{B}$
- Header: $H = 58 \text{B}$ pro Segment
- Datenrate $R = 100 \text{Mbps}$

# Bearbeitung

## Gesamtgröße N

$$
\begin{align*}
	N &= \left\lceil \frac{L}{S} \right\rceil \cdot H + L \\
	&= \left\lceil \frac{2^{32}}{1460} \right\rceil \cdot
	58 + 2^{32} \\
	&= 4.465589318 \cdot 10^9 \ [\text B] \\
	&= 3.572471454 \cdot 10^{10} \ \text{b} \\
	&= 3.572471454 \cdot 10^{4} \ \text{Mb} \\
\end{align*}
$$

##  Übertragungsdauer t

$$
\begin{align*}
	\text{s} &= \text{Mb} \div \frac{\text{Mb}}{\text{s}} \\
	t &= N \div R \\
	&= 3.572471454 \cdot 10^4 \ \text{Mb} \div 100 \ \text{Mbps} \\
	&= 3.572471454 \cdot 10^2 \ \text{s} \\
	&\approx 5.95 \ \text{min}
\end{align*}
$$
