[SQLFiddle](http://sqlfiddle.com/)

```postgresql
CREATE TABLE Benutzer(
  Benutzernr INT PRIMARY KEY,
  Name VARCHAR(200)
);

CREATE TABLE Beitrag (
  BeitragsID SERIAL PRIMARY KEY,
  gepostet_am DATE NOT NULL,
  Beitragstext VARCHAR(200),
  Benutzernr INT REFERENCES Benutzer(Benutzernr) NOT NULL
);

CREATE TABLE Sponsored_Post(
  BeitragsID INT PRIMARY KEY REFERENCES Beitrag(BeitragsID),
  Tagesbudget DECIMAL(9,2) CHECK(Tagesbudget >= 1) DEFAULT 1 NOT NULL
);

CREATE TABLE Foto(
  BeitragsID INT PRIMARY KEY REFERENCES Beitrag(BeitragsID),
  Dateiname CHAR(32) CHECK(char_length(Dateiname) = 32) NOT NULL
);

CREATE TABLE verlinkt(
  Benutzernr INT REFERENCES Benutzer(Benutzernr),
  BeitragsID INT REFERENCES Foto(BeitragsID),
  pos_x INT,
  pos_y INT,
  PRIMARY KEY(Benutzernr, BeitragsID)
);
```
