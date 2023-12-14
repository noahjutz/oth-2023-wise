# 1
https://data.deutschebahn.com/dataset/data-stationsdaten.html

# 2
|Bundesland|RB|BM|Bf. Nr.|Station|Bf DS 100Abk.|Kat. Vst|Straße|PLZ|Ort|Aufgabenträger|
|---|---|---|---|---|---|---|---|---|---|---|

# 3
```postgresql
CREATE TABLE bahnhoefe(
	bundesland VARCHAR(200) NOT NULL,
	regionalbereich VARCHAR(200) NOT NULL,
	bahnhofsmanagement VARCHAR(200) NOT NULL,
	id INT PRIMARY KEY,
	station VARCHAR(200) NOT NULL,
	betriebsstelle VARCHAR(50) NOT NULL,
	kategorie INT NOT NULL,
	strasse VARCHAR(200) NOT NULL,
	plz INT,
	ort VARCHAR(200),
	aufgabentraeger VARCHAR(200) NOT NULL
);
```

# 4
- Delimiter: `;`

# 5
```postgresql
CREATE VIEW hbf AS
SELECT id, bundesland, station, kategorie -- AS kategorie
FROM bahnhoefe
WHERE station LIKE '%Hbf'
OR station LIKE '%Hauptbahnhof'
```
