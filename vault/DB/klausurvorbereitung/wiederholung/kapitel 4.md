# Datentypen

| Typ | Alias | Beschreibung |
| ---- | ---- | ---- |
| `INTEGER` | `INT` | Ganze Zahl |
| `DECIMAL(p,s)` | `NUMERIC` | Kommazahl mit p stellen, davon s nach dem Komma |
| `DOUBLE` | `REAL` | Fließkommazahl |
| `CHARACTER(l)` | `CHAR` | Zeichenkette mit fixer Länge l |
| `CHARACTER VARYING(l)` | `VARCHAR` | Zeichenkette mit max. Länge l |
| `DATE` |  | Jahr-Monat-Tag |

# DDL

**CREATE TABLE**
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
```

**ALTER TABLE**
```postgresql
ALTER TABLE kunden ADD/DROP/RENAME COLUMN my_col INT;
```

**DROP TABLE**
```postgresql
DROP TABLE kunden;
```

# DML

**Insert**
```postgresql
INSERT INTO kunden(kundennummer, name) VALUES (default, 'jeff');
```

**Update**
```postgresql
UPDATE kunden SET name='jeff' WHERE kundennummer=3;
```

**Delete**
```postgresql
DELETE FROM kunden WHERE ...;
TRUNCATE TABLE kunden;
```

**Select**
```postgresql
SELECT DISTINCT H.land, COUNT(*) AS anzahl, AVG(P.preis) AS avg_preis
FROM hersteller H JOIN produkte P ON H.firma = P.hersteller
WHERE P.preis > 3
GROUP BY h.land
HAVING COUNT(*) < 5
ORDER BY COUNT(*);
```

**CTE**
```postgresql
WITH ... AS (SELECT ...) SELECT ...
```

**UNION/INTERSECT/EXCEPT**
```postgresql
SELECT ... UNION/INTERSECT/EXCEPT [ALL] SELECT ...
```

**CAST**
```postgresql
CAST(col_name AS VARCHAR(50))
```

**CASE WHEN**
```postgresql
SELECT bezeichnung, preis,
CASE preis WHEN 0 THEN 'kostenlos' ELSE preis END
FROM produkte ORDER BY preis;
```
