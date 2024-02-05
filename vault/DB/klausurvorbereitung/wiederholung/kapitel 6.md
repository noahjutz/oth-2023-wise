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

# PL/pgSQL

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
END $$ LANGUAGE plpgsql
```

**Funktionen**
```postgresql
CREATE OR REPLACE FUNCTION my_fun() RETURNS INT AS
$$ BEGIN
-- code
RETURN 128;
END $$ LANGUAGE plpgsql
```

| Volatile | Standard | Immutable |
| ---- | ---- | ---- |
|  |  |  |