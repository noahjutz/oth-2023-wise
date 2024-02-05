# Embedded SQL

```java
ProdukteIterator iter;
#sql iter = { SELECT bezeichnung, preis FROM produkte };
do {
	#sql { FETCH :iter INTO :bezeichnung, :preis };
	System.out.println(bezeichnung+" kostet "+preis+" EUR");
} while (!iter.endFetch());
iter.close();
```

- Java mit preprocessor (Zeilen, die mit `#sql` beginnen)

# JDBC

**Connection**
```java
String url = "jdbc://postgresql://host/db?currentSchema=schema"
Connection conn = DriverManager.getConnection(url, "user", "password");
conn.close();
```

**Statement**
```java
Statement st = conn.createStatement();
```

**PreparedStatement**
```java
PreparedStatement pst = conn.prepareStatement("SELECT * FROM t WHERE id = ?");
pst.setString(1, "id");
```

**ResultSet**
```java
ResultSet rs = st.executeQuery();
// or: int n = st.executeUpdate();

while (rs.next()) {
	String col1 = rs.getString(1);
	int my_col = rs.getInt("my_col");
}
```

**DatabaseMetaData**
```java
DatabaseMetaData data = conn.getMetaData();
ResultSet rs = data.getTables("catalog", "schema", "table");
```

**ResultSetMetaData**
```java
ResultSetMetaData data = rs.getMetaData();
data.getColumnCount();
data.getColumnName(0);
data.getColumnTypeName(0);
```

# PL/pgSQL Routinen

**Block**
```postgresql
DECLARE
-- variables
BEGIN
-- code
END
```

**Kontrollstrukturen**
```postgresql
IF ... THEN ... ELSE ... END IF;
WHILE ... LOOP ... END LOOP;
LOOP ... EXIT WHEN ...; END LOOP;
FOR ... IN ... LOOP ... END LOOP;
```

**Stored Procedures**
```postgresql
CREATE OR REPLACE FUNCTION my_proc() RETURNS void AS 
$$ BEGIN
-- code
END $$ LANGUAGE plpgsql;
```
oder
```postgresql
CREATE OR REPLACE PROCEDURE my_proc() AS
$$ BEGIN
-- code
END $$ LANGUAGE plpgsql;
```

**Funktionen**
```postgresql
CREATE OR REPLACE FUNCTION my_fun(INT) RETURNS INT AS
$$ BEGIN
-- code
RETURN $1;
END $$ LANGUAGE plpgsql;
```

| Volatile | Stable | Immutable |
| ---- | ---- | ---- |
| darf alles | in-situ und innerhalb Statement idempotent | in-situ und idempotent |

**Tabellenfunktionen**
```postgresql
CREATE FUNCTION my_fun() RETURNS TABLE (col_1 INT, ...) AS ...
```

# PL/pgSQL Trigger

**Triggerfunktion**
```postgresql
CREATE FUNCTION my_fun() RETURNS TRIGGER AS
$$ BEGIN
-- NEW: update/insert new table
-- OLD: update/delete old table
END $$ LANGUAGE plpgsql;
```

**Trigger einschalten**
```postgresql
CREATE TRIGGER my_trigger
{BEFORE|AFTER|INSTEAD OF} {INSERT|UPDATE|DELETE}
ON my_table
FOR EACH {ROW|STATEMENT}
EXECUTE PROCEDURE my_fun();
```

# Indexe

**Clustered Index**
```postgresql
CLUSTER my_table USING pkey_col
```
- Binäre Suche
- Re-Cluster nach jeder Manipulation der Tabelle

**B-Baum**
Eigenschaften
- Selbst-balancierend
- Daten sind im gesamten Baum verteilt
- Jeder Knoten hat zwischen 0 und 2k+1 Kindknoten (Grad)
- Jeder Knoten hat zwischen k und 2k Einträge (Wurzel nur mind. 1)

 Suche
- Startet in Wurzel
- eintrag $<$ gesucht: nach links
- eintrag $>$ gesucht: nach rechts

**B+-Baum**
Eigenschaften
- Daten sind auf Blatt-ebene
- Jeder Knoten hat zwischen 0 und 2k+1 Kindknoten (Grad)
- Jeder Knoten hat zwischen k und 2k Einträge
- Jeder Blattknoten hat zwischen k* und 2k* Einträge
- Typischerweise k > k*
- Blattknoten sind doppelt verkettet

Suche
- Startet in Wurzel
- eintrag $<$ gesucht: nach links
- eintrag $\ge$ gesucht: nach rechts

Einfügen
- Suche Blatt, in dem der neue Schlüssel sein sollte
- Wenn Einträge im Blatt weniger als 2k*, einfach einfügen
- Sonst: Überlauf -> Split
	- Es gibt 2k*+1 Einträge
	- Es gibt einen mittleren Eintrag k*+1. Diesen zum Vaterknoten **kopieren**.
	- Es gibt k linke ($<$) und k+1 rechte ($\ge$) Knoten.
	- Vaterknoten rekursiv splitten
		- jetzt **nicht kopieren, sondern verschieben**.
		- Es gibt k linke ($<$) und k rechte ($>$) knoten.

Löschen
- Suche Blatt, in dem der zu löschende Knoten ist
- Wenn Einträge im Blatt mehr als k*, einfach löschen
- Sonst: Unterlauf -> Ausgleich/Mischen
	- Es gibt k*-1 Einträge
	- Falls existiert Nachbarblatt mit mehr als k* Einträgen, **ausgleich**:
		- Nimm 1 Eintrag aus Nachbarblatt
		- Passe Wegweiser im Vaterknoten an
	- Sonst, **mischen**:
		- Es gibt k*-1 Einträge im Blatt
		- Es gibt k* Einträge im Nachbarblatt
		- Nach mischen gibt es k* + k*-1 Einträge im gemischten Blatt
		- 

PostgreSQL
- `VACUUM [my_table]`