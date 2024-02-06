# 0 Inhaltsverzeichnis

1. Grundlagen
- OLTP/OLAP
- ACID
- DB/DBMS/DBS
- DDL/DML/DCL
2. ER-Modelle
- Kochrezept ER-Diagramme
3. Relationenmodell
- ERD -> Relationenschema
- Generalisierung Methoden
- Join (outer/semi/...)
- Division
- Anfrageoptimierung
- Funktionale Abhängigkeit
- Superschlüssel, Schlüsselkandidat
- 1NF, 2NF, 3NF Überführung
4. SQL
- Datentypen
- CREATE , ALTER, DROP TABLE
- INSERT, UPDATE, DELETE, SELECT
- UNION, INTERSECT, EXCEPT, CASE WHEN
5. Mehrnutzerbetrieb
- Views
- Users, Roles, Permissions
- Mehrbenutzeranomalien
- SX-Matrix
- Isolation levels
- Journaling
6. Anwendungsentwicklung
- JDBC Connection, (Prepared)Statement, ResultSet, Metadata
- PL/pgSQL Procedures, Functions, Trigger
- Clustered Index, B-Baum, B+-Baum
- Join-Algorithmen

# 1 Grundlagen

| OLTP | OLAP |
| ---- | ---- |
| OnLine Transaction Processing | OnLine Analytical Processing |
| Viele schnelle Anfragen | Komplexe Anfragen |
| Database | Data Warehouse |

- **A**tomicity (Alles oder nichts)
- **C**onsistency (Nur erlaubte Zustände)
- **I**solation (Kein gleichzeitiger Zugriff)
- **D**urability (Systemcrash-Schutz)

| DB | DBMS | DBS |
| ---- | ---- | ---- |
| Datenbank | Datenbank-Managementsystem | Datenbanksystem |
| Daten | PostgreSQL | DB + DBMS |

| DDL | DML | DCL |
| ---- | ---- | ---- |
| Data Definition Language | Data Manipulation Language | Data Control Language |
| Metadaten/Datenbankschema | CRUD | Benutzerverwaltung |

