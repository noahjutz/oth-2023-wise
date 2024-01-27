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
| $R$ | B/s | Datenrate (=10Mb/s) |
| $t_R$ | s | Round-Trip-Time (=$t_S+t_L$) |
| $t_S$ | s | Signallaufzeit |
| $t_L$ | s | Verzögerungen |
| $x$ | m | Maximale Trunk-Strecke (=2.5km) |
| $v$ | m/s | Ausbreitungsgeschwindigkeit (=2/3 c) |

Zu zeigen ist, dass die Mindestframegröße $N = 64 \ \text{B}$ beträgt. Sie hängt von der Datenrate $R = 10 \ \text{MB/s}$ und der Round-Trip-Time $t_R$ ab.

$$
N = R \cdot t_R
$$

Die Round-Trip-Time $t_R$ besteht aus der Signallaufzeit $t_S$ und weiteren Verzögerungen $t_L$.

$$
\begin{align*}
	t_R &= t_S + t_L \\
	&= \frac{x}{v} + t_L \\
	&= \frac{
		2.5 \ \text{km}
	}{
		\frac{2}{3} \cdot 300.000 \ \text{km/s}
	} + t_L\\
	&= 1.25 \cdot 10^{-5} + t_L \ \text{s} \\
\end{align*}
$$

Da $t_T \ge t_R$ ist die Mindestframegröße $N$ also mindestens:

$$
\begin{align*}
	N &= R \cdot t_R \\
	&= R \cdot (t_S + t_L) \\
	&\ge R \cdot t_S \\
	&= 10 \ \text{Mb/s} \cdot 1.25 \cdot 10^{-5} \ \text{s} \\
	&= 1.25 \cdot 10^{-4} \ \text{Mb} \\
	&= 1.25 \cdot 10^{-4} \cdot 10^6 \ \text{b} \\
	&= 125 \ \text{b} \\
	&\approx 16 \ \text{B}
\end{align*}
$$

Die maximale zulässige Verzögerungszeit $t_L$ lässt sich folgendermaßen berechnen:

$$
\begin{align*}
	N &= R \cdot (t_S + t_L) \\
	\iff t_L &= \frac{N}{R} - t_S \\
	&= \frac{64\ \text{B}}{10\ \text{Mb/s}} - 1.25 \cdot 10^{-5} \ \text{s} \\
	&= \frac{512\ \text{b}}{10^7\ \text{b/s}} - 1.25 \cdot 10^{-5} \ \text{s} \\
	&= 512 \cdot 10^{-7} \ \text{s} - 1.25 \cdot 10^{-5} \ \text{s} \\
	&= (512 \cdot 10^{-2} - 1.25) \cdot 10^{-5} \ \text{s} \\
	&= (5.12 - 1.25) \cdot 10^{-5} \ \text{s} \\
	&= 3.87 \cdot 10^{-5} \ \text{s} \\
	&= 3.87 \cdot 10^{-5} \cdot 10^6 \ \micro\text{s} \\
	&= 38.7 \ \micro\text{s}
\end{align*}
$$
