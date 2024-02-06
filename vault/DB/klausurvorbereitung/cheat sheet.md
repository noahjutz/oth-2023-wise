# 0 Inhaltsverzeichnis

1. Grundlagen
- OLTP/OLAP
- ACID
- DB/DBMS/DBS
- DDL/DML/DCL
2. ER-Modelle
- Kochrezept ER-Diagramme
3. Relationenmodell
- ERD -> Relationenschema
- Generalisierung Methoden
- Join (outer/semi/...)
- Division
- Anfrageoptimierung
- Funktionale Abhängigkeit
- Superschlüssel, Schlüsselkandidat
- 1NF, 2NF, 3NF Überführung
4. SQL
- Datentypen
- CREATE , ALTER, DROP TABLE
- INSERT, UPDATE, DELETE, SELECT
- UNION, INTERSECT, EXCEPT, CASE WHEN
5. Mehrnutzerbetrieb
- Views
- Users, Roles, Permissions
- Mehrbenutzeranomalien
- SX-Matrix
- Isolation levels
- Journaling
6. Anwendungsentwicklung
- JDBC Connection, (Prepared)Statement, ResultSet, Metadata
- PL/pgSQL Procedures, Functions, Trigger
- Clustered Index, B-Baum, B+-Baum
- Join-Algorithmen

# 1 Grundlagen

| OLTP | OLAP |
| ---- | ---- |
| OnLine Transaction Processing | OnLine Analytical Processing |
| Viele schnelle Anfragen | Komplexe Anfragen |
| Database | Data Warehouse |

- **A**tomicity (Alles oder nichts)
- **C**onsistency (Nur erlaubte Zustände)
- **I**solation (Kein gleichzeitiger Zugriff)
- **D**urability (Systemcrash-Schutz)

| DB | DBMS | DBS |
| ---- | ---- | ---- |
| Datenbank | Datenbank-Managementsystem | Datenbanksystem |
| Daten | PostgreSQL | DB + DBMS |

| DDL | DML | DCL |
| ---- | ---- | ---- |
| Data Definition Language | Data Manipulation Language | Data Control Language |
| Metadaten/Datenbankschema | CRUD | Benutzerverwaltung |

# 2 ER-Modelle

- Sind alle Kardinalitäten an Beziehungen?
- Kardinalitäten richtig herum?
- Gibt es überflüssige Entitätstypen?
- Hat jeder Entitätstyp einen Primärschlüssel?
- Müssen manche Entitätstypen schwach sein?
- Ist die entsprechende Beziehung doppelt umrahmt?
- Sind erweiternde Primärschlüssel unterstrichelt?
- Sind Generalisierungen korrekt modelliert?

# 3 Relationenmodelle

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

| Generalisierungsmethode | Erklärung |
| ---- | ---- |
| Volle Redundanz | Jede Entität wird zu einer Tabelle mit allen Spalten, führt zu Redundanz |
| Hausklassenmodell | Wie volle Redundanz, aber es wird nur in eine Tabelle eingefügt |
| Vertikale Partitionierung | Bei Subentitäten nur spezielle Spalten übernehmen |
| Hierarchierelation | Nur eine Tabelle mit allen Spalten, + type tag |

## Joins

![[3 joins.png]]

| Outer Join | ⟕ ⟖ ⟗ |
| ---- | ---- |
| Equi-Join | Nur $=$ |
| Theta-Join | $<\ \le\ =\ \ne\ \ge\ >$ |
| Natural Join | Equi-Join mit gleich heißenden Attributen |
| Semi-Join | R⋉S bzw. R⋊S: $\pi_{R.*}$ bzw. $\pi_{S.*}$ |

## Division

![[3 division.png|400]]

$$
(R \times S) \div S = R
$$

## Heuristiken

- Selektion, Projektion früh und zusammengefasst
- Kleine Zwischenergebnisse
- Selektion statt Mengenoperation

## Kardinalitätsschätzung

- $|\sigma_{R.a=x}(R)| = \frac{|R|}{|R.a|}$
- $sf_P = \frac{|\sigma_PR|}{|R|}$
- $|R \times S| = |R| \cdot |S|$
- $0 \le |R \Join S| \le |R| \cdot |S|$
- $|R \Join_{R.a=S.a} S| = |R|$ bzw. $|S|$

## Abhängigkeit

$A \Rightarrow B$ falls $A \to B$ und $\nexists A' \subsetneq A: A' \to B$

## Schlüssel

- Superschlüssel: $A \to R$
- Schlüsselkandidat: $A \Rightarrow R$

## Normalformen

| NF | Eigenschaften | Überführung |
| ---- | ---- | ---- |
| 1NF | Attribute sind atomar | Attribute flachklopfen |
| 2NF | nicht-Schlüsselattribute hängen voll vom ganzen Schlüssel ab | Zerlegung in Tabellen |
| 3NF | keine transitive Abhängigkeiten |  |