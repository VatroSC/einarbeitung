## Aufgabenbeschreibung

1. Erstelle aus den Json Daten eine YAML-Datei.
2. Erstelle ein XML-File aus der JSON.
3. Validiere das XML-File mittels XSD.

### Fragen:

1. Was sind die Unterschiede der Datentypen?
    YAML(YAML Ain't Markup Language); ist ein datenorientiertes Format, das auf einfache Lesbarkeit und Kürze ausgelegt ist. Wird oft für Konfigurationsdateien verwendet(z.B in Docker & Kubernetes)
        Nutzung:    Konfigurationsdateien, Datenübertragungen, API-Spezifikationen(z.B OpenAPI)
    
    XML(Extensible Markup Language); ist ein Daten/Dokumentenorientiertes Format. Es verwendet eine hierarchische Struktur mit Tag und Attributen(änlich wie HTML)
        Nutzung:    Datenübertragungen, Konfigurationsdateien, Dokumentenspeicherung

    XSD(XML Schema Definition); ist kein Datenformat, sondern eine Definition für XML-Dokumente. XSD beschreibt die Struktur, Daten-Typen und Regeln, die ein XML-Dokument erfüllen muss. Wird zu validierung von XML-Daten verwendet.
        Nutzung:    Valiedierung von XML-Dokumenten in Webservices, Datenübertragung und speicherung

2. Was sind Vor- und Nachteile der jeweiligen Dateiformate?
    YAML:   Vorteile:   Leicht lesbar, Kompakte Syntax, Einfach zu schreben und zu bearbeiten, Flexibilität, Breite Unterschtützung(Docker, Kubernetes, CI/CD-Systeme)
            Nachteile:  Fehleranfäligkeit, Fehlende Validierung, Nicht ideal für sehr komplexe Daten, Fehlende Standardisierung
    XML:    Vorteile:   Hierarchie, Validierungsmöglichkeit, Erweitbarkeit, Unterschtützt Metadaten
            Nachteile:  Größerer Speicherbedarf, Umständlich bei einfachen Daten
    XSD:    Vorteile:   Erzwingt Konsistenz, Wiederverwendbarkeit, Erweitbarkeit, Komplexe Datenmodele möglich
            Nachteile:  Nur für XML, Komplexe Sytax, Manueler Aufwand, Steile Lernkurve 

3. Wofür wird XML verwendet?
    XML wird meistens verwendet, um Daten in einem strukturierten, hierarchischen und plattformunabhängig zwischen verschiedenen Systemen oder Anwendungen auszutauschen.
        - Datenübertragung - Datenvalidierung - Konfig-Dateien - Dokumentenmanagement

4. Unterstützt XML benutzerdefinierte Tags?
    Ja XML unterschtützt benutzerdefinierte Tags. Das ist eine der Hauptschtärken von XML.

5. Wann ist welcher Datentyp von Vorteil?
    Vorteile:   YAML;   ist gut wenn, die Daten einfach, kompakt und leicht verständlich sein sollen.
                XML;    ist gut wenn, du komplexe, hierarchische Daten speichern oder übertragen möchtest und interoperabilität(datenaustausch) wichtig ist.
                XSD;    ist gut wenn, die Datenstruktur komplex ist und Validierung zwingend erforderlich ist(Webservices, Firmenstatdards)

6. Was ist eine XSD-Datei?
    XSD ist kein Datenformat, sondern eine Definition für XML-Dokumente. XSD dient zur Definition und Validierung der Struktur und Daten eines XML-Dokuments.

7. Was versteht man unter Validierung?
    Ziel der Validierung ist; Datenintegrität sicherstellen, Konsistenz, Kompatibilität

8. An was erinnert eine XML-Datei bzgl. ihres Aufbaus?
    Eine XML-Datei erinert in ihrem Aufbau an HTML und an Baustrukturen in der Informatik.

9. Was bedeutet Parsen?
    Parsen ist eher der Vorgang, um Daten aus anderen Dateiformaten (z.B. JSON) in eine für die Maschine verständliche Datenstruktur zu bringen (z.B. dict in Python)