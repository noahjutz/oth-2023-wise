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

Die Größe der Nutzdaten $n$ darf zwischen 0 und 1500 Byte sein. Ein Pad-Füllfeld mit einer Größe von $46-n$ wird angelegt, falls $n<46$.

# e

Die Minimalgröße des Datenblocks von 46 Byte ermöglicht die Minimalgröße des Ethernet-Frames von 64 Byte (46+18=64).

Ein Ethernet-Frame muss bei einem Half-Duplex Ethernet mit bis zu 100Mbps mindestens 64 Byte groß sein, weil die Sendung eines Frames mindestens so lange wie ein round-trip dauern muss.



time it takes to transmit a package: $t$
round trip time of a 10Mbps 2.5km-long Cable