# a

![[IEEE802.3.png]]

# b

Die Präambel ist ein konstanter 8-Byte-Wert, der wie folgt aussieht (LSb-first):

```
10101010 10101010 10101010 10101010
10101010 10101010 10101010 10101011
```

Die ersten 62 bit bestehen aus abwechselnden 1en und 0en, und dienen der Taktkalibrierung des Empfängers. Die letzten zwei bit (11) markieren den Start des Ethernet-Frames.

# c

-

# d

Die Größe der Nutzdaten $a$ darf zwischen 0 und 1500 Byte sein. Ein Pad-Füllfeld mit einer Größe von $46-a$ wird angelegt, falls $a<46$.

# e

Die Mindestgröße des Datenblocks von 46 Byte ergibt sich aus der Differenz der Mindestgröße des Frames (64 Byte) und der aufsummierten Größe der übrigen Felder (18 Byte). $64 - 18 = 46$.

Ein 10BASE5 Ethernet-Frame muss mindestens 64 Byte groß sein. Bei dieser Größe dauert die Sendung eines Frames länger als ein Round Trip.

Dauert die Übertragung kürzer, so werden Late Collisions nicht erkannt. Eine Kollision wird erkannt, wenn während dem Senden ein Paket eintrifft. Sende ich aber so schnell, dass das einkommende Paket erst danach ankommt, wird keine Kollision erkannt.

## Beweis

> [!NOTE] Angaben richten sich nach IEEE 802.3-1985 (10BASE5 Ethernet)

| Symbol | Einheit | Beschreibung |
| ---- | ---- | ---- |
| $N$ | B | Mindestframegröße (=64B) |
| $R$ | B/s | Datenrate (=10MB/s) |
| $t_T$ | s | Transfer-Dauer (größer als RTT) |
| $t_R$ | s | Round-Trip-Time |
| $x$ | m | Maximale Trunk-Strecke (=2.5km) |
| $v$ | m/s | Ausbreitungsgeschwindigkeit (=0.77c) |

Zu zeigen ist, dass die Mindestframegröße $N = 64 \ \text{B}$ beträgt. Sie hängt von der Datenrate $R = 10 \ \text{MB/s}$ und der Transferdauer $t_T$ ab.

$$
N = R \cdot t_T
$$

Die Transferdauer muss mindestens so lange sein wie die maximale Round-Trip-Time $t_R$.

$$
\begin{align*}
	t_R &= \frac{2x}{v} \\
	&= \frac{
		2 \cdot 2.5 \ \text{km}
	}{
		0.77 \cdot 300.000 \ \text{km/s}
	} \\
	&\approx 2.1645 \cdot 10^{-5} \ \text{s} \\
\end{align*}
$$

Die Mindestframegröße $N$ ist also mindestens:

$$
\begin{align*}
	N &\ge 10 \ \text{MB/s} \cdot 2.1645 \cdot 10^{-5} \ \text{s} \\
	N &\ge 2.1645 \cdot 10^{-4} \ \text{MB} \\
	N &\ge 2.1645 \cdot 10^{-4} \cdot 10^6 \ \text{B} \\
	N &\ge 216.45 \ \text{B}
\end{align*}
$$

!! Widerspruch
