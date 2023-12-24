# 1

```postgresql
create table asciiplace.pixels(
	id SERIAL PRIMARY KEY,
	x INT NOT NULL,
	y INT NOT NULL,
	c CHAR NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
```
