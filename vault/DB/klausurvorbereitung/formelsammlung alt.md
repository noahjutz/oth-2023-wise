 >[!Zugelassene Hilfsmittel] 
 >Ein handschriftlich doppelseitig beschriebenes Blatt

# Relationale Algebra


| Relationale Algebra | SQL |
| ---- | ---- |
| Tupel | Zeilen |
| Attribute | Spalten |

# SQL
## CREATE TABLE
```postgresql
CREATE TABLE kunden (
	kundennummer INT PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	email VARCHAR(500) CHECK (email LIKE '%@%') UNIQUE,
	passwort CHAR(32),
	land VARCHAR(100) DEFAULT 'Deutschland',
	geworben_von INT REFERENCES kunden(kundennummer)
);
```

## TRUNCATE TABLE
```postgresql
TRUNCATE [ONLY] <name> [, ...] [RESTART IDENTITY]
```

## CREATE VIEW
```postgresql
CREATE VIEW my_view AS SELECT ...;
DROP VIEW my_view;
```

```postgresql
CREATE MATERIALIZED VIEW my_mat_view AS SELECT ...;
REFRESH MATERIALIZED VIEW my_mat_view;
DROP MATERIALIZED VIEW my_mat_view;
```

## SELECT
```postgresql
SELECT * FROM tabelle1 t1
FULL JOIN tabelle2 t2 ON t1.id1 = t2.id1 -- outer
LEFT JOIN tabelle3 t3 USING(id2) -- outer
JOIN tabelle1 u1 ON t1.preis < u1.preis -- inner
WHERE t1.name='Peter';
```

## INSERT

```postgresql
INSERT INTO table (col1, col2) VALUES (col1, col2)
```