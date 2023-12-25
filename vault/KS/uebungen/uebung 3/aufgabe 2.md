```
0.65.130.5/18
```

> [!fail] Falsch abgeschrieben
> `10.65.130.5/18`

# Klasse

Subnetzmaske: `/18`
Klasse B: `/16`
Klasse C: `/24`
$\implies$ Klasse C

# Präfix (bin)

```
00000000 01000001 10
```

> [!fail] Folgefehler
> `00001010 ...`

# Suffix (bin)

```
000010 00000101
```

> [!check] Richtig

# Netzwerk-Adresse

NW-Adresse = Präfix

```
0.65.128
```

> [!fail] Falsch
> NW-Adresse = Präfix + 000... statt Suffix
> `10.65.128.0`

# Max. Anzahl Hosts

Suffix/Interface-ID hat 14 Bit

$$
2^{14} = \underline{16\ 384} \text{ Mögliche Interface-IDs}
$$

> [!warning] Broadcast- und Netzwerkadresse abziehen
> $\implies x = 2^{14} - 2 = 16\ 382$

# Broadcast-Adresse

Größte Interface-ID ist Broadcast

$$
\verb!00000000.01000001.10!\underbrace{
	\verb!111111.11111111!
}_{\text{Interface-ID}} \ _{(2)} =  \verb!0.65.191.255!\\
$$


> [!fail] Folgefehler
> `10.65.191.255`
