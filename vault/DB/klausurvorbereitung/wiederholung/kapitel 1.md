# OLTP/OLAP

| OLTP | OLAP |
| ---- | ---- |
| OnLine Transaction Processing | OnLine Analytical Processing |
| Viele schnelle Anfragen | Komplexe Anfragen |
| Database | Data Warehouse |

# ACID

- **A**tomicity (Alles oder nichts)
- **C**onsistency (Nur erlaubte Zustände)
- **I**solation (Kein gleichzeitiger Zugriff)
- **D**urability (Systemcrash-Schutz)

# DB/DBMS/DBS

| DB | DBMS | DBS |
| ---- | ---- | ---- |
| Datenbank | Datenbank-Managementsystem | Datenbanksystem |
| Daten | PostgreSQL | DB + DBMS |

# DDL/DML/DCL

| DDL | DML | DCL |
| ---- | ---- | ---- |
| Data Definition Language | Data Manipulation Language | Data Control Language |
| Metadaten/Datenbankschema | CRUD | Benutzerverwaltung |

# Metadaten/Daten

| Metadaten | Daten |
| --- | --- |
| Spalten, Datentypen, ... | z. B. bei Wörterbuch: Wörter und Definitionen |

# Datenmodellierung

| Konzeptionell | Logisch | Physisch |
| ---- | ---- | ---- |
| ER-Diagramm | Relationenmodell | Interne Speicherung |

# Ebenen

| Extern | Logisch | Physisch |
| ---- | ---- | ---- |
| Views | Tables | Internes Schema |

# Architektur

| Datensystem | Zugriffssystem | Speichersystem |
| ---- | ---- | ---- |
| SQL | Daten, Indexe | Blocks, Caching |
