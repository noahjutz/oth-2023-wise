# Gegeben

## Kommunikation

- A$\to$(Bytes 0-358)$\to$B

- A$\to$(Segment 1)$\to$B
- A$\gets$(Ack)$\gets$B
- A$\to$(Segment 2)$\to$B
- A$\gets$(Ack)$\gets$B

## Hosts


|  | Type | Port |
| ---- | ---- | ---- |
| A | src | 1028 |
| B | dst | 80 |

## Segmente

|  | Größe | Byte-Nr |
| ---- | ---- | ---- |
| 1 | 50B | 359 |
| 2 | 80B | ? |

# Bearbeitung

- Ursprungsport: 1028
- Zielport: 80
- Sequenznummer $n$

n = startseqnr + 50