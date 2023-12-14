# 1
```postgresql
SELECT COUNT(*) FROM Professoren WHERE rang='C4'
```

# 2
```postgresql
SELECT name FROM vorlesungen
JOIN hoeren ON vorlesungen.vorlnr = hoeren.vorlnr
JOIN studenten ON hoeren.matrnr = studenten.matrnr
WHERE titel='Grundzüge'
```

# 3
```postgresql
SELECT name, SUM(sws) FROM professoren
JOIN vorlesungen ON professoren.persnr=vorlesungen.gelesenvon
WHERE persnr IN (
 	SELECT gelesenvon FROM vorlesungen
	GROUP BY gelesenvon
	HAVING COUNT(*) >= 2
)
GROUP BY name
```

# 4
```postgresql
SELECT DISTINCT name FROM studenten
JOIN hoeren ON hoeren.matrnr=studenten.matrnr
WHERE vorlnr IN (
	SELECT vorlnr FROM studenten
	JOIN hoeren ON studenten.matrnr=hoeren.matrnr
	WHERE name='Feuerbach'
) AND name !='Feuerbach'
```

## Mit Joins
### Komponenten
#### (1) matrnr von Feuerbach
```postgresql
SELECT * FROM studenten WHERE name="Feuerbach"
```

|matrnr|name|
|-|-|
|29555|Feuerbach|

#### (2) vorlnr von 29555
```postgresql
SELECT * FROM hoeren WHERE matrnr=29555
```

|matrnr|vorlnr|
|-|-|
|29555|5022|
|29555|5001|

#### (3) matrnr von Mitstudierenden von 29555
```postgresql
-- HA: hoeren alle
-- HF: hoeren Feuerbach
SELECT HF.vorlnr, HA.matrnr FROM hoeren HF
JOIN hoeren H2 ON HF.vorlnr=HA.vorlnr
WHERE HF.matrnr=29555
```

|vorlnr|matrnr|
|-|-|
|5001|26120|
|5001|27550|
|5001|29120|
|5022|29555|
|5022|25403|
|5001|29555|

#### (4) name von hoeren
```postgresql
SELECT hoeren.matrnr, name FROM hoeren
JOIN studenten ON hoeren.matrnr=studenten.matrnr
```

|matrnr|name|
|---|---|
|26120|Fichte|
|27550|Schopenhauer|
|27550|Schopenhauer|
|28106|Carnap|
|...|...|

### Zusammengesetzt
#### (A) = (1) + (2)
```postgresql
SELECT vorlnr
FROM studenten
JOIN hoeren ON hoeren.matrnr=studenten.matrnr
WHERE name='Feuerbach'
```

|vorlnr|
|-|
|5022|
|5001|

#### (B) = (A) + (3)

```postgresql
SELECT H_A.matrnr
FROM studenten S_F
JOIN hoeren H_F ON H_F.matrnr=S_F.matrnr
JOIN hoeren H_A ON H_F.vorlnr=H_A.vorlnr -- !
WHERE S_F.name='Feuerbach'
```

|matrnr|
|---|
|26120|
|27550|
|29120|
|29555|
|25403|
|29555|

#### (C) = (B) + (4)

```postgresql
SELECT H_A.matrnr, S_A.name
FROM studenten S_F
JOIN hoeren H_F ON H_F.matrnr=S_F.matrnr
JOIN hoeren H_A ON H_F.vorlnr=H_A.vorlnr
JOIN studenten S_A ON H_A.matrnr=S_A.matrnr -- !
WHERE S_F.name='Feuerbach'
```

|matrnr|name|
|---|---|
|26120|Fichte|
|27550|Schopenhauer|
|29120|Theophrastos|
|29555|Feuerbach|
|25403|Jonas|
|29555|Feuerbach|

### Antwort

```postgresql
SELECT DISTINCT S_A.name
FROM studenten S_F
JOIN hoeren H_F ON H_F.matrnr=S_F.matrnr
JOIN hoeren H_A ON H_F.vorlnr=H_A.vorlnr
JOIN studenten S_A ON H_A.matrnr=S_A.matrnr -- !
WHERE S_F.name='Feuerbach'
AND S_A.name != 'Feuerbach'
```

|name|
|---|
|Schopenhauer|
|Jonas|
|Fichte|
|Theophrastos|
