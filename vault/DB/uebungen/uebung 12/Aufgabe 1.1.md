https://onecompiler.com/postgresql/

# Fakultät

## Rekursive definition

$$
n! := \left\{
	\begin{align*}
		&n \cdot (n - 1) && \text{falls } n \ne 0 \\
		&1 && \text{sonst}
	\end{align*}
\right.
$$

## Explizite definition

$$
n! := \prod_{k=1}^n k
$$

## Pseudocode

```
def factorial(n):
	result = 1
	for i from 1 to n inclusive:
		result = result * i
	return result
```

# PL/pgSQL

## UDF Definieren

```postgresql
CREATE [ OR REPLACE ] FUNCTION fun(param INT, ...) RETURNS INT AS
$$ DECLARE
	x INT := ...;
BEGIN
	-- ...
END $$ LANGUAGE plpgsql;
```

## Loop

```postgresql
FOR i IN 1..10 LOOP
	-- ...
END LOOP;
```

## Return value

```postgresql
RETURN ...;
```

## Raise exception

```postgresql
RAISE "message";
```

## Conditional expressions

```postgresql
IF ... THEN
	-- ...
END IF;
```

## Call function

```
SELECT fun(n);
```

# UDF

```postgresql
CREATE OR REPLACE FUNCTION fac(n INT) RETURNS INT AS
$$ DECLARE
	result INT := 1
BEGIN
	IF n < 0 THEN
		RAISE "n must be a non-negative integer.";
	END IF;
	FOR i in 1..n LOOP
		result = result * i;
	END LOOP;
	RETURN result;
END $$ LANGUAGE plpgsql;
```

n must be a non-negative integer