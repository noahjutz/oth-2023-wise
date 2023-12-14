# 1
[[DB/uebungen/uebung 7/aufgabe 1|aufgabe 1]]

# 2
```postgresql
INSERT INTO Benutzer VALUES (1, 'Olivia');
INSERT INTO Benutzer VALUES (2, 'Yvonne');
```

# 3
```postgresql
SELECT * FROM Benutzer;
```

# 4
```postgresql
UPDATE Benutzer SET Name='Olivia von Opel' WHERE benutzernr=1;
```

# 5
```postgresql
SELECT COUNT(*) FROM benutzer;
```

# 6
```postgresql
SELECT * FROM benutzer WHERE Name LIKE '% von %';
```

# 7
```postgresql
DELETE FROM benutzer WHERE Benutzernr=1;
```
