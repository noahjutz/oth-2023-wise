# Gegeben

- $k=k^*=1$

```mermaid
graph TD

subgraph root[ ]
    rootL(( ))
    rootKim[Kim]
    rootM(( ))
    rootTom[Tom]
    rootR(( ))
end

rootL-->leaf1

subgraph leaf1[ ]
    Bob
    Kai
end

rootM-->leaf2

subgraph leaf2[ ]
    Kim
end

rootR-->leaf3

subgraph leaf3[ ]
    Tom
    Uwe
end
```

# Einfügen von Leo

Wo soll Leo hin?

```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
           ^
```

K < L < T --> Leo muss in das mittlere Blatt, rechts von Kim. Weil es hier noch platz gibt, einfach einfügen.

```mermaid
graph TD

subgraph root[ ]
    rootL(( ))
    rootKim[Kim]
    rootM(( ))
    rootTom[Tom]
    rootR(( ))
end

rootL-->leaf1

subgraph leaf1[ ]
    Bob
    Kai
end

rootM-->leaf2

subgraph leaf2[ ]
    Kim
    Leo
end

rootR-->leaf3

subgraph leaf3[ ]
    Tom
    Uwe
end

style Leo stroke:red
```

# Einfügen von Zoe

Wo soll Zoe hin? T < U < Z --> Zoe muss in das rechte Blatt, rechts von Uwe.

```mermaid
graph TD
%%{init: {"width": "10%"} }%%

subgraph root[ ]
    rootL(( ))
    rootKim[Kim]
    rootM(( ))
    rootTom[Tom]
    rootR(( ))
end

rootL-->leaf1

subgraph leaf1[ ]
    Bob
    Kai
end

rootM-->leaf2

subgraph leaf2[ ]
    Kim
    Leo
end

rootR-->leaf3

subgraph leaf3[ ]
    Tom
    Uwe
    Zoe
end

style Zoe stroke:red
```

Jetzt ist die Anzahl der Einträge im rechten Blatt 3. Die maximale Anzahl an Einträgen in einem Blatt sind aber 2 ($2k^*$). Es gibt also in diesem Blatt einen Überlauf, es muss also **gesplittet** werden. Zuerst wird der mittlere Eintrag (Uwe) in den Vaterknoten kopiert.

```mermaid
graph TD
%%{init: {"width": "10%"} }%%

subgraph root[ ]
    root1(( ))
    rootKim[Kim]
    root2(( ))
    rootTom[Tom]
    root3(( ))
    rootUwe[Uwe]
    root4(( ))
end

root1-->leaf1

subgraph leaf1[ ]
    Bob
    Kai
end

root2-->leaf2

subgraph leaf2[ ]
    Kim
    Leo
end

rootUwe~~~leaf3

subgraph leaf3[ ]
    Tom
    Uwe
    Zoe
end

style rootUwe stroke:red
```

Das Blatt wird dann in ein linkes und ein rechtes Blatt gespalten.

| Links | Rechts |
| ---- | ---- |
| Einträge $<$ Uwe | Uwe $\le$ Einträge |
| Tom | Uwe, Zoe |

```mermaid
graph TD
%%{init: {"width": "10%"} }%%

subgraph root[ ]
    root1(( ))
    rootKim[Kim]
    root2(( ))
    rootTom[Tom]
    root3(( ))
    rootUwe[Uwe]
    root4(( ))
end

root1-->leaf1

subgraph leaf1[ ]
    Bob
    Kai
end

root2-->leaf2

subgraph leaf2[ ]
    Kim
    Leo
end

root3-->leaf3

subgraph leaf3[ ]
    Tom
end

root4-->leaf4

subgraph leaf4[ ]
    Uwe
    Zoe
end

style leaf3 stroke:red
style leaf4 stroke:red
```

Jetzt ist die Anzahl der Einträge in der Wurzel 3. Die maximale Anzahl an Einträgen in einem inneren Knoten ist aber 2 ($2k$). Es gibt also in diesem Knoten einen Überlauf, es muss also **gesplittet** werden. Zuerst wird der mittlere Eintrag (Tom) in den Vaterknoten **verschoben**. Da es keinen Vaterknoten gibt, wird eine neue Wurzel erstellt.

```mermaid
graph TD
%%{init: {"width": "10%"} }%%

subgraph newroot[ ]
    newrootL(( ))
    newrootTom[Tom]
    newrootR(( ))
end

newrootTom~~~rootM

subgraph root[ ]
    rootL(( ))
    rootKim[Kim]
    rootM(( ))
    rootUwe[Uwe]
    rootR(( ))
end

rootL-->leaf1

subgraph leaf1[ ]
    Bob
    Kai
end

rootL~~~leaf2

subgraph leaf2[ ]
    Kim
    Leo
end

rootR~~~leaf3

subgraph leaf3[ ]
    Tom
end

rootR-->leaf4

subgraph leaf4[ ]
    Uwe
    Zoe
end

style newroot stroke:red
style rootM display:none
```

Die alte Wurzel wird in einen linken und einen rechten inneren Knoten gespalten.

| Links | Rechts |
| ---- | ---- |
| Einträge $<$ Tom | Tom $<$ Einträge |
| Kim | Uwe |

```mermaid
graph TD
%%{init: {"width": "10%"} }%%

subgraph root[ ]
    rootL(( ))
    rootTom[Tom]
    rootR(( ))
end

rootL-->nodeL
rootR-->nodeR

subgraph nodeL[ ]
    nodeLL(( ))
    nodeLKim[Kim]
    nodeLR(( ))
end

subgraph nodeR[ ]
    nodeRL(( ))
    nodeRUwe[Uwe]
    nodeRR(( ))
end

nodeLL-->leaf1
nodeLR~~~leaf2
nodeRL~~~leaf3
nodeRR-->leaf4

subgraph leaf1[ ]
    Bob
    Kai
end

subgraph leaf2[ ]
    Kim
    Leo
end

subgraph leaf3[ ]
    Tom
end

subgraph leaf4[ ]
    Uwe
    Zoe
end

style nodeL stroke:red
style nodeR stroke:red
```

Das Blatt, das ursprünglich zwischen Kim und Tom war, ist jetzt das rechte Kind von Kim. Das Blatt, das ursprünglich zwischen Tom und Uwe war, ist jetzt das linke Kind von Uwe.

```mermaid
graph TD
%%{init: {"width": "10%"} }%%

subgraph root[ ]
    rootL(( ))
    rootTom[Tom]
    rootR(( ))
end

rootL-->nodeL
rootR-->nodeR

subgraph nodeL[ ]
    nodeLL(( ))
    nodeLKim[Kim]
    nodeLR(( ))
end

subgraph nodeR[ ]
    nodeRL(( ))
    nodeRUwe[Uwe]
    nodeRR(( ))
end

nodeLL-->leaf1
nodeLR-->leaf2
nodeRL-->leaf3
nodeRR-->leaf4

subgraph leaf1[ ]
    Bob
    Kai
end

subgraph leaf2[ ]
    Kim
    Leo
end

subgraph leaf3[ ]
    Tom
end

subgraph leaf4[ ]
    Uwe
    Zoe
end

linkStyle 3,4 stroke:red
```

# Prüfen

https://www.cs.usfca.edu/~galles/visualization/BPlusTree.html

Alles richtig.

# 20 Zahlen, k=k*=2, h=2

- $k = 2 \implies N=2k=4$ (N: Maximale Anzahl Einträge pro Knoten/Blatt)
- $\frac{20}{N+1} = 4 \implies$ Vielfache von 4
- 4 gleichmäßig verteilte Werte: 4, 8, 12, 16
- Wir wollen in der Wurzel diese Werte
- Füge für jeden dieser Werte zuerst 2 kleinere, dann 2 größere ein.
