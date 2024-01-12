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

Jetzt ist die Anzahl der Einträge im rechten Blatt 3. Die maximale Anzahl an Einträgen in einem Blatt eines B+-Baums ist $2k^*$.