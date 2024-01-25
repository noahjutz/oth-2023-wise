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

> [!NOTE] Angaben richten sich nach IEEE 802.3-1985 (10BASE5 Ethernet)

Die Mindestgröße des Datenblocks von 46 Byte ergibt sich aus der Differenz der Mindestgröße des Frames (64 Byte) und der aufsummierten Größe der übrigen Felder (18 Byte). $64 - 18 = 46$.

Ein 10BASE5 Ethernet-Frame muss mindestens 64 Byte groß sein. Bei dieser Größe dauert die Sendung eines Frames länger als ein Round Trip.

Dauert die Übertragung kürzer, so werden Late Collisions nicht erkannt. Eine Kollision wird erkannt, wenn während dem Senden ein Paket eintrifft. Sende ich aber so schnell, dass das einkommende Paket erst danach ankommt, wird keine Kollision erkannt.

Rechnung:

| Symbol | Einheit | Beschreibung |
| ---- | ---- | ---- |
| $N$ | B | Slot Time (gesucht) |
| $R$ | B/s | Datenrate (bis zu 100Mb/s) |
| $t_T$ | s | Transfer-Dauer (größer als RTT) |
| $t_R$ | s | Round-Trip-Time |
| $x$ | m | Maximale Trunk-Strecke (=2.5km) |
| $v$ | m/s | Ausbreitungsgeschwindigkeit (=0.77c) |

$$
N = R \cdot t_T
$$

$$
t_R = 2 \cdot \frac{x}{v} = 
$$