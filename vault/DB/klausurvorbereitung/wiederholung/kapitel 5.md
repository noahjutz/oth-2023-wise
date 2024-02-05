# Views

```postgresql
CREATE VIEW my_view AS SELECT ... WITH CHECK OPTION;
```

- Datenunabhängigkeit
- Datenschutz
- `WITH CHECK OPTION`: INSERT muss WHERE-Prädikat erfüllen

# Materialized Views

```postgresql
CREATE MATERIALIZED VIEW my_mat_view AS SELECT ... ;
REFRESH MATERIALIZED VIEW my_mat_view;
```

# Benutzer und Rollen

```postgresql
CREATE USER noah WITH PASSWORD "abc";
CREATE ROLE cool;
GRANT cool TO noah;
```

# Berechtigungen

```postgresql
GRANT [PERM] ON [ALL TABLES] IN [SCHEMA name] TO [USER] <WITH GRANT OPTION>;
REVOKE [PERM] [RESTRICT|CASCADE]
```

# Mehrbenutzeranomalien

**Dirty Read**
- 2 Nutzer sehen unterschiedliche Werte

**Lost Update**
- Parallele Änderung -> Eine geht verloren

**Non-repeatable Read**
- Unterschiedliche SELECT-Ergebnisse innerhalb einer TA

**Phantomproblem**
- Non-repeatable Read, aber nicht der Inhalt, sondern die Menge an Zeilen ist nicht konsistent

# Serialisierbarkeit

- Serialisierbarkeitsgraph
- Konflikt: $w \to r, w \to w, r \to w$ auf gleiche Tabelle

# SX-Sperrverfahren

| $\swarrow$ Existiert \| Will $\nearrow$ | S | X |
| ---- | ---- | ---- |
| keine | $\checkmark$ | $\checkmark$ |
| S | $\checkmark$ | - |
| X | - | - |
- Hat eine TA selbst eine S-Sperre, kann sie sie zur X-Sperre upgraden.
- Ein Deadlock entsteht, wenn zwei TAs aufeinander warten

# Isolation levels

| Isolation level | Lost Update | Dirty Read | Nonrepeatable read | Phantom read | Serialization Anomaly |
| ---- | ---- | ---- | ---- | ---- | ---- |
| Read uncommitted | ❎ | ✅  | ✅ | ✅ | ✅ |
| Read committed | ❎ | ❎ | ✅ | ✅ | ✅ |
| Repeatable read | ❎ | ❎ | ❎ | ✅ (❎PG) | ✅ |
| Serializable | ❎ | ❎ | ❎ | ❎ | ❎ |
- ✅ Allowed
- ❎ Not allowed
- In PostgreSQL gibt es kein Read uncommitted.

# MVCC

- Alternative zur SX-Sperre
- Objekte haben mehrere Versionen (z.B. tabellen: $w_1(x) \mapsto x'$)
- Wird mit diffs realisiert

# Journaling

| LSN | TA | PageID | Undo | Redo | PrevLSN |
| ---- | ---- | ---- | ---- | ---- | ---- |
| Log-Sequenz-Nr | Transaktion | Page auf Festplatte | Verlierer | Gewinner | Gleiche TA, vorherige Aktion |

- Verlierer: TA hat im log noch nicht committed
- Gewinner: TA hat committed
