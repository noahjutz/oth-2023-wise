# 1
**Falsch** weil schüler $\to$ instrument

# 2
**Falsch** weil instrument ausschließlich von schüler bestimmt wird

# 3
**Falsch** weil {schüler, instrument} $\supsetneq$ {schüler} $\to$ {instrument}

# 4
**Richtig** weil {wochentag, uhrzeit, raum} $\to$ {lehrer, schüler}

# 5
**Falsch** weil {wochentag, uhrzeit, raum} $\subsetneq$ {wochentag, uhrzeit, instrumant, raum}

# 6
**Richtig** weil {wochentag, lehrer} $\to$ raum $\wedge$ {wochentag, uhrzeit, raum} $\to$ schüler $\wedge$ schüler $\to$ instrument

# 7
**Falsch** weil {wochentag, uhrzeit, lehrer} und {wochentag, uhrzeit raum} sind Schlüsselkandidaten

# 8
**Richtig** weil alle Elemente sind Atomar.

# 9
**Richtig** weil:
- In 1NF
- {wochentag, uhrzeit, raum} ist Schlüsselkandidat.
- {instrument, lehrer, schüler} hängen voll vom ganzen Schlüsselkandidat ab.
  $\implies$ In 2NF

# 10
**Falsch** weil:
- {wochentag, uhrzeit, raum} $\to$ {==schüler==} und
  {==schüler==} $\to$ {instrument}

>[!warning] Falsche Begründung
>- {wochentag, uhrzeit, raum} $\to$ {==lehrer==} und
>  {==lehrer==, raum} $\to$ {raum}
>- {wochentag, lehrer} $\to$ {==raum==} und
>  {wochentag, uhrzeit, ==raum==} $\to$ {lehrer, schüler}
>
>Falsche Begründungen, weil Schlüsselattribute in B (A $\to$ B $\to$ C)

