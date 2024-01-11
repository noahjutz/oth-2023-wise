# 1

```postgresql
CREATE TABLE freundschaften (
	person1 INT,
	person2 INT,
	PRIMARY KEY(person1, person2)
);
```

# 2

Triggerfunktion

```postgresql
CREATE FUNCTION reverse_friendship() RETURNS TRIGGER AS
$$ BEGIN
	INSERT INTO freundschaften VALUES (
		NEW.person2, NEW.person1
	) ON CONFLICT DO NOTHING;
	RETURN NULL;
END $$ LANGUAGE plpgsql;
```

Trigger

```postgresql
CREATE TRIGGER reverse_friendship
AFTER INSERT
ON freundschaften
FOR EACH ROW
EXECUTE PROCEDURE reverse_friendship();
```

# 3

https://onecompiler.com/postgresql/3zz5j35vc