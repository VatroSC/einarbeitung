## Aufgabenbeschreibung
Die Daten(base.json) sollen in einer Datenbank gespeichert werden.

1. **DB aufsetzen**: Die Datenbank wird eingerichtet, um Daten zu speichern.
2. **Struktur der Datenbank mittels semantisches ER-Diagramm**: Das semantische ER-Diagramm wird erstellt, um die Struktur der Datenbank zu visualisieren.
3. **Datenbank aufsetzen und Daten einfügen**: Die Datenbank wird erstellt und Daten werden eingefügt.
4. **Daten mittels SQL-Querys bearbeiten (nicht über xampp-oberfläche)**:
      (a) **Hinzufügen**: Neue Daten werden der Datenbank hinzugefügt.
      (b) **Löschen**: Daten werden aus der Datenbank gelöscht.
      (c) **Bearbeiten**: Bestehende Daten werden in der Datenbank bearbeitet.
      (d) **Auslesen**: Daten werden aus der Datenbank abgerufen.

### Fragen:

- **Welche Datenbanken gibt es? SQL, SQLite**
      Es gitbt Rationale Datenbanken vie: SQL, MySQL, SQLite, PostgreSQL
                           und NoSQL vie: MongoDB, Cassandra   
- **Wann macht welcher Typ Sinn? SQL bei gleichbleibenden Attributen.**
      SQL db machen Sin bei strukturierten Daten mit festen Attributen,
      NoSQL db wie MongoDB bei unstrukturieten Daten, Graph-db wie Neo4j für komplexe Beziehungen (z.B. soziale Netzwerke) 
- **Was ist ein Primary Key und was ein Foreign Key?**
      Primary Key:   ist ein eindeutiger Indentifikator für eine Zeile in einer Tabele (z.B. ID)
      Foreign Key:   ist ein Attribut, das au einen Primary Key einer anderen Tabelle verweist, um eine Bezihung zwischen den Tabellen herzustellen. 
- **Was ist ein nativer und was ein künstlicher Primary Key?**
      Nativer PK:       verwendet ein natürlich vorhandened Attribut der Daten (z.B ISBN für Bücher)
      Künstlicher PK:   ein zusätzlich generiertes Attribut (z.B ID mit AUTO-INCREMENT), das unabhängig von den Daten existiert. 
- **Welche Beziehungstypen zwischen Tabellen gibt es?**
      1:1   (One to One)   Jede Zeile in Tabelle A hat genau eine zugehörige Zeile in Tabelle B
      1:n   (One to Many)  Eine Zeile in Tabelle A kann mit mehreren Zeilen in Tabelle B verknüpft sein
      n:m   (Many to Many) Mehrere Zeilen in Tabelle A können mit mehreren Zeilen in Tabelle B verknüpft sein
- **Welche Wildcards gibt es in MySQL und was bedeuten sie?**
      %     (Prozenzeichen)         Steht für beliebig viele Zeichen (z.B WHERE name LIKE 'V%' findet alle Namen, die mit "V" beginnen).
      _     (Unterstrich)         Steht für genau ein beliebiges Zeichen (z.B WHERE name LIKE 'V_' findet alle Namen mit zwei Buchstaben, die mit "V" beginnen)
      []    (Zeichenbereich)        Steht für ein Zeichen aus einer definierten auswahl (z.B WHERE name LIKE '[A-C]%' findet alle Namen, die mit A, B oder C beginnen). 
                                    (Nicht in MySQL direkt unterstützt)
      [^]   (Negation (caret(^)))   Steht für ein Zeichen, das **nicht** in einer definierten Auswahl enthalten ist (z.B WHERE name LIKE '[^A-C]%' findet Namen die **nicht** mit A, B oder C beginnen)
                                    (Nicht in MySQL direkt unterstützt)
- **Was ist ein Join?**
      JOIN in SQL verbindet Daten aus zwei oder mehreren Tabellen basiert auf einer definierten Beziehung (z.B. über FK)
- **Was ist ein left- und was ein right-Join?**
      LEFT JOIN   liefert alle Zeilen aus der linken Tabelle und ergänzt passende Daten aus der rechten Tabelle.
      RIGHT JOIN  liefert alle Zeilen aus der rechten Tabelle und ergänzt passende Daten aus der linken Tabelle.
- **Was ist das kartesische Produkt zweier Tabellen?**
      Das **kartesische Produkt** ist das Ergebnis einer Verknüpfung ohne Bedingung, bei der jede Zeile der ersten Tabelle mit jeder Zeile der zweiten Tabelle kombiniert wird (n*m). 
- **Was ist Kaskadierung?**
      Kaskadierung beschreibt das automatische Weitergeben von Aktionen wie **Löschen** oder **Ändern** von Daten entlang von Tabellen, die über FK miteinander verknüpft sind.
- **Wann werden Gruppierungen benötigt?**
      **Gruppierungen** in SQL werden benötigt, wenn Daten auf der Basis eines gemeinsamen Attributs zusammengefasst werden sollen. (z.B Summe, Durchschnit, etc.) Dies geschiet mit der GROUP BY
- **Was ist ein DBMS?**
      **DBMS** (Database Management System) ist eine Software, die zur **Erstellung**, **Verwaltung** und **Nutzung** von DB dient. (z.B. Scpeichern, Abrufen, Bearbeiten und Löschen)
- **Was versteht man unter Datenintegrität?**
      **Datenintegrität** bezeichnet die Korrekte, Konsistenz und Vollschtändigkeit von Daten in einer DB.
      Arten der Datenintegrität: Entity, Referenzielle, Domänen und Benutzerdefinierte Integrität    
- **Was ist Normalisierung?**
      **Normalisierung** ist der Prozess, Daten in einer DB in mehrere Tabellen aufzuteilen und Beziehungen zwischen ihnen zu definieren, um Redundanz und die Datenintegrität zu verbessern.
      **Normalisierungsformen(NF)**  Normalform; 1NF, 2NF, 3NF. Höhere Normalformen; BCNF(Boyce-Codd-NF), 4NF und 5NF 
- **Was sind Aggregationsfunktionen und welche gibt es? (3 Beispiele)**
      **Aggregationsfunktionen** sind SQL funktionen, die mehrere Zeilen einer Tabelle zusammenfassen, um einen einzigen Wert zurückzugeben(z.B. Summen, Durchschnitte oder Zählungen). <!--GROUP BY--> 
         Beispiele:  SUM()    SELECT SUM (Verkäufe) FROM (Bestellungen);
                     AVG()    SELECT AVG (Lohn) FROM (Mitarbeiter);
                     COUNT()  SELECT COUNT (*) FROM (Kunden);
<!--
 (Kartesisch bezieht sich auf den französischen Philosophen René Descartes (lateinisch: Cartesius) 
 bezeichnet in der Mathematik und Geometrie ein Bezugssystem oder Konzepte, die auf seinen Arbeiten basieren. 
 
 Kartesisches Produkt: Die Menge aller möglichen Paare aus zwei Mengen, z. B. 𝐴×𝐵={(𝑎,𝑏)∣𝑎∈𝐴,𝑏∈𝐵})
 -->
 <!-- DB == Datenbank -->