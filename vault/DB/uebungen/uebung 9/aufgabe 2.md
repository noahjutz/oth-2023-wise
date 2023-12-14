# 1
```postgresql
CREATE VIEW grosser_hbf AS
SELECT * FROM hbf
WHERE kategorie=1
WITH LOCAL CHECK OPTION;
```

# 2
## a
Nicht in `grosser_hbf` zu finden, da `kategorie=2`.
```postgresql
SELECT * FROM hbf
WHERE station LIKE '%egensburg%';
```

## b

> [!NOTE]- DROP NOT NULL
> Für diesen Insert müssen einige `NOT NULL`-Constraints entfernt werden.
>```postgresql
>ALTER TABLE bahnhoefe ALTER regionalbereich DROP NOT NULL;
>ALTER TABLE bahnhoefe ALTER bahnhofsmanagement DROP NOT NULL;
>ALTER TABLE bahnhoefe ALTER betriebsstelle DROP NOT NULL;
>ALTER TABLE bahnhoefe ALTER strasse DROP NOT NULL;
>ALTER TABLE bahnhoefe ALTER aufgabentraeger DROP NOT NULL;
>```

```postgresql
INSERT INTO hbf (station, bundesland, id, kategorie)
VALUES ('Teststadt Nord', 'Hessen', 9999, 5);
```

## c

```postgresql
SELECT * FROM hbf WHERE id=9999; -- (0 rows)
```
Nein, wegen `WHERE station LIKE '%Hbf'`.

## d

```postgresql
DELETE FROM hbf WHERE id=9999; -- DELETE 0 (macht nichts)
DELETE FROM bahnhoefe WHERE id=9999; -- DELETE 1 (funktioniert)
```

## e

```postgresql
INSERT INTO grosser_hbf (station, bundesland, id, kategorie)
VALUES ('Teststadt Nord', 'Hessen', 9999, 5);
```

>[!fail] Error
>```
>ERROR:  new row violates check option for view "grosser_hbf"
>DETAIL:  Failing row contains (Hessen, null, null, 9999, Teststadt Nord, null, 5, null, null, null, null).
>```

## f

```postgresql
INSERT INTO grosser_hbf (station, bundesland, id, kategorie)
VALUES ('Teststadt Nord', 'Hessen', 9999, 1); -- funktioniert
```

## g

```postgresql
SELECT * FROM grosser_hbf WHERE id=9999; -- (0 rows)
```
Nein, wegen `WHERE station LIKE '%Hbf'`.

## h

```postgresql
DROP VIEW grosser_hbf;
```

```postgresql
CREATE VIEW grosser_hbf AS
SELECT * FROM hbf
WHERE kategorie=1
WITH CHECK OPTION; -- CASCADED is default
```

```postgresql
INSERT INTO grosser_hbf (station, bundesland, id, kategorie)
VALUES ('Teststadt Nord', 'Hessen', 9999, 1); -- funktioniert
```

> [!fail] Error
>```
>ERROR:  new row violates check option for view "hbf"
>DETAIL:  Failing row contains (Hessen, null, null, 9999, Teststadt Nord, null, 1, null, null, null, null).
>```


# 3

```postgresql
CREATE MATERIALIZED VIEW bahnhof_statistik AS
SELECT bundesland, COUNT(*) FROM bahnhoefe
GROUP BY bundesland;
```

```postgresql
SELECT * FROM bahnhof_statistik;
DELETE FROM bahnhoefe WHERE id=9999;
REFRESH MATERIALIZED VIEW bahnhof_statistik;
SELECT * FROM bahnhof_statistik;
```

431 $\to$ 430

# 4

## a

```postgresql
SELECT DISTINCT bundesland FROM bahnhoefe;
```

## b

```postgresql
SELECT ort, COUNT(*) FROM bahnhoefe
GROUP BY ort
HAVING COUNT(*) > 10;
```

## c

```postgresql
SELECT B.* FROM bahnhoefe U
JOIN bahnhoefe B USING(kategorie)
WHERE U.station='Ulm Hbf';
```

## d

```postgresql
WITH orte AS (
	SELECT bundesland, ort, COUNT(*) AS anzahl
	FROM bahnhoefe
	GROUP BY ort, bundesland
) -- Anzahl Stationen pro Ort
SELECT bundesland, AVG(anzahl) FROM orte
GROUP BY bundesland
```

