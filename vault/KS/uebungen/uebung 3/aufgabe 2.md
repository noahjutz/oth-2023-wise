```
0.65.130.5/18
```
# Klasse
Subnetzmaske: `/18`
Klasse B: `/16`
Klasse C: `/24`
$\implies$ Klasse C

# Präfix (bin)
```
00000000 01000001 10
```

# Suffix (bin)
```
000010 00000101
```

# Netzwerk-Adresse
NW-Adresse = Präfix
```
0.65.128
```

# Max. Anzahl Hosts
Suffix/Interface-ID hat 14 Bit

$$
2^{14} = \underline{16\ 384} \text{ Mögliche Interface-IDs}
$$

# Broadcast-Adresse
Größte Interface-ID ist Broadcast

$$
\verb!00000000.01000001.10!\underbrace{
	\verb!111111.11111111!
}_{\text{Interface-ID}} \ _{(2)} =  \verb!0.65.191.255!\\
$$
