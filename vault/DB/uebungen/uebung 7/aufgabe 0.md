[SQLisland](http://wwwlgis.informatik.uni-kl.de/cms/courses/informationssysteme/sqlisland/)

```postgresql
SELECT * FROM dorf

SELECT * FROM BEWOHNER

SELECT * FROM bewohner WHERE beruf = 'Metzger'

SELECT * FROM BEWOHNER WHERE status='friedlich'

SELECT * FROM BEWOHNER WHERE status='friedlich' AND beruf='Waffenschmied'

SELECT * FROM BEWOHNER WHERE status='friedlich' AND beruf LIKE '%schmied'

INSERT INTO bewohner (name, dorfnr, geschlecht, beruf, gold, status) VALUES ('Fremder', 1, '?', '?', 0, '?')

SELECT bewohnernr FROM BEWOHNER WHERE name='Fremder'

SELECT gold FROM BEWOHNER WHERE name='Fremder'

SELECT * FROM GEGENSTAND WHERE besitzer IS NULL

UPDATE gegenstand SET besitzer = 20 WHERE gegenstand = 'Kaffeetasse'

UPDATE GEGENSTAND SET besitzer=20 WHERE besitzer IS NULL

SELECT * FROM GEGENSTAND WHERE besitzer=20

SELECT * FROM BEWOHNER WHERE status='friedlich' AND (beruf='Haendler' OR beruf='Kaufmann')

UPDATE GEGENSTAND SET besitzer=15 WHERE gegenstand='Teekanne' OR gegenstand='Ring'

UPDATE bewohner SET gold = gold + 120 WHERE bewohnernr = 20

UPDATE bewohner SET name='Noah' WHERE bewohnernr=20

SELECT * FROM BEWOHNER WHERE beruf='Baecker' ORDER BY gold DESC

UPDATE bewohner SET gold = gold + 100 - 150 WHERE bewohnernr = 20

INSERT INTO gegenstand (gegenstand, besitzer) VALUES ('Schwert', 20)

SELECT * FROM BEWOHNER WHERE beruf='Pilot' ORDER BY gold DESC

SELECT dorf.name FROM dorf, bewohner WHERE dorf.dorfnr = bewohner.dorfnr AND bewohner.name = 'Dirty Dieter'

SELECT name FROM bewohner WHERE bewohnernr=(SELECT haeuptling FROM dorf WHERE name='Zwiebelhausen')

SELECT COUNT(*) FROM bewohner, dorf WHERE dorf.dorfnr = bewohner.dorfnr AND dorf.name = 'Zwiebelhausen'

SELECT COUNT(name) FROM bewohner WHERE geschlecht='w'AND dorfnr=3

SELECT name FROM bewohner WHERE geschlecht='w'AND dorfnr=3

SELECT SUM(bewohner.gold) FROM bewohner, dorf WHERE dorf.dorfnr = bewohner.dorfnr AND dorf.name = 'Gurkendorf'

SELECT SUM(gold) FROM bewohner, dorf WHERE dorf.dorfnr = bewohner.dorfnr AND (beruf='Haendler' or beruf='Baecker' OR beruf='Kaufmann')

SELECT beruf, SUM(bewohner.gold), AVG(bewohner.gold) FROM bewohner GROUP BY beruf ORDER BY AVG(bewohner.gold)

SELECT status, AVG(bewohner.gold) FROM bewohner GROUP BY status ORDER BY AVG(bewohner.gold)

DELETE FROM bewohner WHERE name = 'Dirty Dieter'

DELETE FROM bewohner WHERE bewohnernr=11

UPDATE bewohner SET status='friedlich' WHERE bewohnernr=8

UPDATE bewohner SET status = 'ausgewandert' WHERE bewohnernr = 20
```
