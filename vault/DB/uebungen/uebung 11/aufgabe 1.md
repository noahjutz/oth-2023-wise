# 1

## CREATE TABLE

```postgresql
create table pixels(
	id SERIAL PRIMARY KEY,
	x INT NOT NULL,
	y INT NOT NULL,
	c CHAR NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT NOW()
)
```

## INSERT

```postgresql
INSERT INTO pixels (x, y, c, created_at) VALUES (1, 1, '.', NOW())
```
