# Gegeben

## Kommunikation

- A$\to$(Bytes 0-358)$\to$B
- A$\to$(Segment 1 50B)$\to$B
- A$\to$(Segment 2 80B)$\to$B

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
