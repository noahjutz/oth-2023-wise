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

# Join $\bowtie$

$R \bowtie_P S$ ist äquivalent zu $\sigma_P(R \times S)$. P ist das join-Kriterium.

# 