# Gegebene Relation

serien_folgen(__serie, staffel, folge__, titel, produzent, regisseur, sprache, {schauspieler})

serie $\to$ produzent
serie, staffel $\to$ regisseur
serie, staffel, folge $\to$ titel
produzent $\to$ sprache

# 1NF
## Bedingungen
- Atomar

## Probleme
- {schauspieler}

## Lösung
serien_folgen(__serie, staffel, folge__, titel, produzent, regisseur, sprache, ==__schauspieler__==)

# 2NF
## Bedingungen
- Attribute hängen vom ganzen Schlüssel ab

## Probleme
- serie $\to$ produzent $\checkmark$
- serie, staffel $\to$ regisseur $\checkmark$ 
- produzent $\to$ sprache $\checkmark$ 

## Lösung
serien(__serie__, produzent, sprache)
staffeln(__serie, staffel__, regisseur)
folgen(__serie, staffel, folge__, titel)
schauspieler(__serie, staffel, folge__, __schauspieler__)

schauspieler(serie, staffel, folge) ist FK auf folgen(serie, staffel, folge)
produzenten.serie ist FK auf folgen.serie
regisseure(serie, staffel) ist FK auf folgen(serie, staffel)
sprachen.produzent ist FK auf produzenten.produzent
# 3NF
## Bedingungen
- Keine transitive Abhängigkeiten __A__ $\to$ B $\to$ C innerhalb einer Tabelle

## Probleme
- serien: __serie__ $\to$ produzent $\to$ sprache

## Lösung
==serien(__serie__, produzent)==
staffeln(__serie, staffel__, regisseur)
folgen(__serie, staffel, folge__, titel)
==produzenten(__produzent__, sprache)==
schauspieler(__serie, staffel, folge__, __schauspieler__)

serien.produzent ist FK auf produzenten.produzent
staffeln.serie ist FK auf serien.serie
folgen(serie, staffel) ist FK auf staffeln(serie, staffel)
schauspieler(serie, staffel, folge) ist FK auf folgen(serie, staffel, folge)