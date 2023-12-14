# 1
```postgresql
CREATE TABLE bahnhoefe (
  BID SERIAL PRIMARY KEY,
  Ort VARCHAR(200) NOT NULL,
  Bahnhof VARCHAR(200) NOT NULL,
  UNIQUE(Ort, Bahnhof)
);

CREATE TABLE Fahrten (
  ZugNr SERIAL PRIMARY KEY,
  Start INT REFERENCES bahnhoefe(BID) NOT NULL,
  Ziel INT REFERENCES bahnhoefe(BID) NOT NULL,
  CHECK(Start != Ziel)
);
```

# 2
```postgresql
INSERT INTO Bahnhoefe VALUES
  (1, 'Regensburg', 'Hbf'),
  (2, 'München', 'Flughafen'),
  (3, 'München', 'Hbf');
  
INSERT INTO Fahrten VALUES
  (101, 1, 2),
  (102, 1, 3),
  (103, 3, 2);
```

# 3
```postgresql
SELECT Ort, COUNT(*) FROM Bahnhoefe
GROUP BY Ort;
```

# 4
```postgresql
SELECT Ort, COUNT(*) FROM Bahnhoefe
JOIN Fahrten ON Fahrten.Start=Bahnhoefe.BID
GROUP BY Ort;
```

# 5
```postgresql
SELECT ZugNr,
  S.Ort AS Start_Ort, S.Bahnhof AS Start_Bahnhof,
  Z.Ort AS Ziel_Ort, Z.Bahnhof AS Ziel_Bahnhof
FROM Fahrten
JOIN Bahnhoefe S ON S.BID=Fahrten.Start
JOIN Bahnhoefe Z ON Z.BID=Fahrten.Ziel;
```

# 6
```postgresql
SELECT Z.Ort, Z.Bahnhof FROM Fahrten
JOIN Bahnhoefe S ON Fahrten.Start=S.BID
JOIN Bahnhoefe Z ON Fahrten.Ziel=Z.BID
WHERE S.Ort='Regensburg'
```
