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

$$
R \div S = \pi_{R.*-S.*}(R) - \pi_{R.*-S.*} \Big(
	\big(
		\pi_{R.*-S.*}(R) \times S
	\big) - R
\Big) \ \text{(Nicht Klausurrelevant)}
$$

Es gilt $(R \times S) \div S = R$.
