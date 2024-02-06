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

| Typ | Erklärung |
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
| 3NF | keine transitive Abhängigkeiten | $A \to B \to C$ wird zu $A \to B$ und $\underline B \to C$ |

# 4 SQL

- `DOUBLE`/`REAL`: Fließkommazahl
- `DATE`: Jahr-Monat-Tag
- `DECIMAL(p, s)`: p Stellen, davon s Nachkommastellen

```postgresql
FOREIGN KEY (a, b) REFERENCES table(c, d) ON {DELETE|UPDATE} {RESTRICT|NO ACTION|SET NULL|SET DEFAULT|CASCADE}
```

```postgresql
CREATE TABLE kunden (
	kundennummer SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	email VARCHAR(500) CHECK (email LIKE '%@%') UNIQUE,
	passwort CHAR(32),
	land VARCHAR(100) DEFAULT 'Deutschland',
	geworben_von INT REFERENCES kunden(kundennummer)
		ON DELETE SET NULL ON UPDATE CASCADE
);
CREATE TABLE privatkunden (LIKE kunden); -- Übernimmt Attribute
CREATE TABLE privatkunden2 AS SELECT * FROM kunden -- Übernimmt Zeilen
ALTER TABLE kunden {ADD|DROP|RENAME} COLUMN my_col [INT|...];
```

```postgresql
INSERT INTO kunden(kundennummer, name) VALUES (default, 'jeff');
UPDATE kunden SET name='jeff' WHERE kundennummer=3;
DELETE FROM kunden WHERE ...;
TRUNCATE TABLE kunden;
```

```postgresql
SELECT DISTINCT H.land, COUNT(*) AS anzahl, AVG(P.preis) AS avg_preis
FROM hersteller H JOIN produkte P ON H.firma = P.hersteller
WHERE P.preis > 3
GROUP BY h.land
HAVING COUNT(*) < 5
ORDER BY COUNT(*);
WITH ... AS (SELECT ...) SELECT ...;
SELECT ... UNION/INTERSECT/EXCEPT [ALL] SELECT ...;
SELECT CASE preis WHEN 0 THEN 'kostenlos' ELSE preis END FROM ...;
```

# 5 Mehrbenutzerbetrieb

```postgresql
CREATE [MATERIALIZED] VIEW my_view AS SELECT ... WITH CHECK OPTION;
REFRESH MATERIALIZED VIEW my_mat_view;
```

```postgresql
CREATE USER noah WITH PASSWORD "abc";
CREATE ROLE cool;
GRANT cool TO noah;
```

```postgresql
GRANT {PERM} ON {ALL TABLES|...} [IN SCHEMA my_schema] TO {USER} [WITH GRANT OPTION];
REVOKE {PERM} {RESTRICT|CASCADE};
```

- **Dirty Read**: Unterschiedliche Werte
- **Lost Update**: Parallele Änderung, 1 geht verloren
- **Non-repeatable Read**: Untersch. SELECT-Erg. in einer TA
- **Phantomproblem**: Anzahl Zeilen inkonsistent

|  | S | X |
| ---- | ---- | ---- |
| S | $\checkmark$ | - |
| X | - | - |

| Isolation level | Lost Update | Dirty Read | Nonrepeatable read | Phantom read | Serialization Anomaly |
| ---- | ---- | ---- | ---- | ---- | ---- |
| Read uncommitted |  | ✅  | ✅ | ✅ | ✅ |
| Read committed |  |  | ✅ | ✅ | ✅ |
| Repeatable read |  |  |  | ✅ (❎PG) | ✅ |
| Serializable |  |  |  |  |  |

| LSN | TA | PageID | Undo | Redo | PrevLSN |
| ---- | ---- | ---- | ---- | ---- | ---- |
| Log-Sequenz-Nr | Transaktion | Page auf Festplatte | Verlierer | Gewinner | Gleiche TA, vorherige Aktion |

# 6 Anwendungsentwicklung

## JDBC

```java
String url = "jdbc://postgresql://host/db?currentSchema=schema"
Connection conn = DriverManager.getConnection(url, "user", "password");
conn.close();
```

```java
Statement st = conn.createStatement();
```

```java
PreparedStatement pst = conn.prepareStatement("SELECT * FROM t WHERE id = ?");
pst.setString(1, "id");
```

```java
ResultSet rs = st.executeQuery();

while (rs.next()) {
	String col1 = rs.getString(1);
	int my_col = rs.getInt("my_col");
}
```

```java
DatabaseMetaData data = conn.getMetaData();
ResultSet rs = data.getTables("catalog", "schema", "table");
```

```java
ResultSetMetaData data = rs.getMetaData();
data.getColumnCount();
data.getColumnName(0);
data.getColumnTypeName(0);
```

## PL/pgSQL

```postgresql
IF ... THEN ... ELSE ... END IF;
WHILE ... LOOP ... END LOOP;
LOOP ... EXIT WHEN ...; END LOOP;
FOR ... IN ... LOOP ... END LOOP;
```

```postgresql
CREATE OR REPLACE {FUNCTION|PROCEDURE} my_fun(INT) RETURNS INT AS
$$ DECLARE
-- variables
BEGIN
-- code
RETURN $1;
END $$ LANGUAGE plpgsql;
```

## B-Baum

- Zwischen 0 und 2k+1 Kindknoten
- Zwischen k und 2k Einträge pro Knoten

## B+-Baum

- Zwischen k* und 2k* Einträge pro Blatt
- Suche: $<$ links, $\ge$ rechts
- Einfügen: (1) Suchen (2) mittleren Knoten kopieren (3) linke und rechte Knoten splitten (4) bei Vater verschieben
- Löschen: (1) Suchen (2a) Aus Nachbarblatt ausgleichen und Wegweiser anpassen (2b) Mit Nachbarblatt mischen und Wegweiser entfernen

```postgresql
CREATE INDEX my_table_pkey ON my_table(pkey_col);
CREATE INDEX ON meine_tabelle(a, b, c);
VACUUM my_table;
```

## Join-Algorithmen

**Nested-Loop-Join**
```
for each row r in R:
	for each row s in S:
		if r.sId == s.id:
			emit(r, s)
```

**Sort-Merge-Join**
- Nach Join-spalte sortieren
- Von oben nach unten Join-Partner suchen

**Hash-Join**
```
hash_table = []

for each row r in R:
	hash_table.put(hash(r.sId)), r)

for each row s in S:
	r = hash_table.get(hash(s.id))
	emit(r, s)
```

**Index-Join**
```
for each row r in R:
	s = s_id_index.get(r.sId) # e.g. using B+-Tree search
	emit(r, s)
```

