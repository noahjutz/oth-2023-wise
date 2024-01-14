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

# Sequenzdiagramm

```mermaid
sequenceDiagram
    participant A AS A<br/>Port 1028
    participant B AS B<br/>Port 80

    A-->>B: syn, seq=x
    B-->>A: syn, ack=x+1, seq=y
    A-->>B: ack=y+1, seq=x+1
    note over A, B: TCP Handshake complete
    A->>B: ack=y+1, seq=x+1
    note over B: 358B received
    B->>A: ack=x+359, seq=y+1
    note over A: Ack (0B) received
    A->>B: ack=y+1, seq=x+359
    note over B: 358+50B received
    B->>A: ack=x+409, seq=y+1
    note over A: Ack (0B) received
    A->>B: ack=y+1, seq=x+409
    note over B: 358+50+80B received
    B->>A: ack=x+489, seq=y+1
    note over A: Ack (0B) received
```

# Antworten

## a

- Ursprungsport: 1028
- Zielport: 80
- Sequenznummer: x+409

## b

- Ursprungsport: 80
- Zielport: 1028
- Ack: x+409
- Seq: y+1

## c

- Ack: x+489

## d

![[seq diagram.png]]

Letztes Ack fehlt!
