# ERD $\to$ Relationenschema

| ERD | Relationenschema |
| ---- | ---- |
| Entität | Tabelle |
| Attribut | Spalte |
| Subattribut | Einzelne Spalten |
| Mehrwertiges Attribut | 1:N Beziehung |
| Beziehungen | Fremdschlüssel |
| Schwache Entität | Zusammengesetzter PK |
| Ternäre Beziehung | wie N:M Beziehungen |
| Generalisierung | siehe unten |

# Generalisierung

| Methode | Erklärung |
| ---- | ---- |
| Volle Redundanz | Jede Entität wird zu einer Tabelle mit allen Spalten, führt zu Redundanz |
| Hausklassenmodell | Wie volle Redundanz, aber es wird nur in eine Tabelle eingefügt |
| Vertikale Partitionierung | Bei Subentitäten nur spezielle Spalten übernehmen |
| Hierarchierelation | Nur eine Tabelle mit allen Spalten, + type tag |

# Mengenoperationen

- $\cap$ Schnittmenge
- $\textbackslash -$ Subtraktion
- $\cup$ Vereinigung

# Projektion $\pi$

$\pi_\text{Spalte 1, Spalte 2, ...} (R)$ begrenzt die Ausgabe auf die angegebenen Spalten.

# Selektion $\sigma$

$\sigma_\text{Kriterium}(R)$ begrenzt die Ausgabe auf die Zeilen, die das Kriterium erfüllen.

# Kartesisches Produkt $\times$

$R \times S$ hat alle Spalten aus R und S, und weist jeder Zeile aus R jede Zeile aus S zu.

# Umbenennung $\rho$

$\rho_\text{Alias}(R)$ gibt der Tabelle R den Namen 'Alias'.

# Join $\Join$

$R \Join_P S$ ist äquivalent zu $\sigma_P(R \times S)$. P ist das join-Kriterium.

![[3 joins.png]]

| Typ | Erklärung |
| ---- | ---- |
| Inner join | (= Join) $\Join$ |
| Outer Join | ⟕ ⟖ ⟗ |
| Equi-Join | Nur $=$ |
| Theta-Join | $<\ \le\ =\ \ne\ \ge\ >$ |
| Natural Join | Equi-Join mit gleich heißenden Attributen |
| Self-Join | $R \Join R$ |
| Semi-Join | R⋉S bzw. R⋊S: $\pi_{R.*}$ bzw. $\pi_{S.*}$ |

# Division $\div$

$R \div S$ gibt eine Tabelle mit allen Spalten aus R, welche nicht auch in S sind. Die resultierenden Zeilen sind jene aus R, für die gilt: Die Zeile hat alle möglichen Kombinationen mit S.

Man kann $R \div S$ folgendermaßen umschreiben (nicht klausurrelevant):

$$
R \div S = \pi_{R.*-S.*}(R) - \pi_{R.*-S.*} \Big(
	\big(
		\pi_{R.*-S.*}(R) \times S
	\big) - R
\Big)
$$

Es gilt:

$$
(R \times S) \div S = R
$$

Sind die Spalten in S keine Teilmenge von jenen in R, so ist das Ergebnis der Division immer leer.

https://en.wikipedia.org/wiki/Relational_algebra#Division_(%C3%B7)

# Anfrageoptimierung

**Heuristiken**
- Frühstmögliche Selektion
- Join statt Kreuzprodukt
- Frühstmögliche Projektion (ohne Duplikateliminierung)
- Join-Reihenfolge so wählen, dass Zwischenergebnisse klein sind
- Folgen von Selektionen und Projektionen zusammenfassen
- Selektionen statt Mengenoperationen
- Nichts doppelt berechnen

**Kardinalitätsschätzung**
- Selektion
	- $|\sigma_{R.a=x}(R)| = \frac{|R|}{|R.a|}$
	- $sf_P = \frac{|\sigma_PR|}{|R|}$
- Kartesisches Produkt
	- $|R \times S| = |R| \cdot |S|$
- Join
	- $0 \le |R \Join S| \le |R| \cdot |S|$
	- $|R \Join_{R.a=S.a} S| = |R|$ bzw. $|S|$

# Normalformenlehre

## Abhängigkeiten

**Funktionale Abhängigkeit**
- $A \to B$ (A bestimmt B)
- A und B sind Attributmengen aus R

**Volle Funktionale Abhängigkeit
- $A \Rightarrow B$ (A bestimmt B voll-funktional)
- Voraussetzung: $A \to B$ und es gibt keine Teilmenge aus A, für die gilt $A' \to B$.

## Schlüssel

**Superschlüssel**
- $A \to R$ (A bestimmt alle Attribute, A ist also Superschlüssel)

**Schlüsselkandidat**
- Voraussetzung: A ist superschlüssel und bestimmt R voll-funktional
- minimaler Superschlüssel

## Normalformen

**NFNF**
- Non-First Normal Form
- Nicht in Normalform

**1NF**
- Attribute sind nicht zusammengesetzt oder Tabellen

**2NF**
- in 1NF
- jedes nicht-Schlüsselattribut hängt voll vom ganzen Schlüssel ab

**3NF**
- in 2NF
- keine transitiven Abhängigkeiten $A \to B \to C$
