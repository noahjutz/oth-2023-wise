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
	result INT := 1;
BEGIN
	IF n < 0 THEN
		RAISE 'n must be a non-negative integer.';
	END IF;
	FOR i in 1..n LOOP
		result = result * i;
	END LOOP;
	RETURN result;
END $$ LANGUAGE plpgsql;
```
# Größtmögliche Zahl

```postgresql
DO $$ BEGIN
	FOR i in 1..100 LOOP
	  RAISE NOTICE '%', i;
	  PERFORM fac(i);
	END LOOP;
END $$
```

Die größtmögliche Zahl n ist 13. 

## Warum?

Der INT-Typ hat 4 byte = 32 bit.  Die Grenzen sind also wie folgt:

$$
-2^{31} = -2\ 147\ 483\ 648
\tag*{untere Grenze}
$$

$$
\begin{align*}
	\sum_{k=0}^{30} 2^k &= \frac{1-2^{31}}{1-2} \\
	&= 2^{31} - 1 \\
	&= 2\ 147\ 483\ 647
\end{align*}
\tag*{obere Grenze}
$$

> [!NOTE] Wie kommt man auf die Grenzen?
> Die einzelnen bits haben einen Wert von $2^0$ bis $2^{31}$. Wegen 2er-Komplement ist der größte Wert negativ ($-2^{31}$). Der größte positive Wert ist also $2^{30}$.


Die Fakultäten von 0 bis 13 sind:

| n | n! |
| ---- | ---- |
| 0 | 1 |
| 1 | 1 |
| 2 | 2 |
| 3 | 6 |
| 4 | 24 |
| 5 | 120 |
| 6 | 720 |
| 7 | 5 040 |
| 8 | 40 320 |
| 9 | 362 880 |
| 10 | 3 628 800 |
| 11 | 39 916 800 |
| 12 | 479 001 600 |
| 13 | 6 227 020 800 |

Da $12! < (2^{31}-1) < 13!$ ist 12 die größte Zahl, die keinen Überlauf erzeugt.
