## Aufgabenbeschreibung

### 1. Erstellen eines UML-Klassendiagramms basierend auf den gegebenen Daten:
- **Analysiere die Struktur des JSON-Dokuments** und identifiziere die relevanten Klassen und ihre Attribute sowie Beziehungen zueinander.
- **Zeichne ein UML-Klassendiagramm**, das die Klassen, ihre Attribute und Methoden sowie die Beziehungen zwischen den Klassen (z.B. Assoziationen, Vererbungen) darstellt.

### 2. Implementierung der Klasse in Python:
- **Erstelle eine Python-Klasse oder Klassen**, die die Struktur des UML-Klassendiagramms widerspiegeln.
- **Definiere die Attribute und Methoden** entsprechend den Daten und Anforderungen aus dem JSON-Dokument.

### 3. Einlesen der JSON-Daten als Objekte der erstellten Klasse(n):
- **Schreibe ein Python-Skript**, das die JSON-Daten einliest.
- **Erstelle Instanzen der zuvor definierten Klasse(n)** und initialisiere sie mit den Daten aus dem JSON-Dokument.

### 4. Methode zum Hinzufügen eines Members:
- **Implementiere eine Methode in der entsprechenden Klasse**, die ein neues Mitglied zum Team hinzufügt.
- Die Methode sollte die benötigten Informationen (z.B. Name, ID) als Parameter entgegennehmen und ein neues Mitgliedsobjekt erstellen und zur entsprechenden Liste hinzufügen.

### 5. Methode zur Ausgabe des Teams mit den jeweiligen Mitgliedern:
- **Implementiere eine Methode in der entsprechenden Klasse**, die das gesamte Team und deren Mitglieder auf eine lesbare Weise ausgibt.
- Die Methode sollte durch die Mitglieder des Teams iterieren und deren Details anzeigen.

### 6. Methode zum Löschen eines Members anhand der ID:
- **Implementiere eine Methode in der entsprechenden Klasse**, die ein Mitglied anhand seiner ID löscht.
- Die Methode sollte die Liste der Mitglieder durchsuchen, das Mitglied mit der passenden ID finden und es aus der Liste entfernen.




## Fragen zur Objektorientierung

1. Warum verwendet man Objektorientierung?
    Objektorientierung wird hauptsächlich verwendet, um die Komlexität der entstehenden Programme zu verringern, große Programme einfacher zu gestalten durch die Unterteilung von Funktionen. Diese vorteile sind; Wiederverwendbarkeit von Code, Modularität, erleichterte Wartung sowie Lesbarkeit und Verständlichkeit des Codes

2. Welche weiteren Vorgehensweisen gibt es?
    Neben oop gibt es noch; 
        Procedurales(Basiert auf einer Abfolge oder Schritten), 
        Funktionales(Schwerpunkt auf reiner, Unverändlichkeit und der Vermeidung von Seiteneffekten),
        Deklaratives(Beschreibt "was" das Programm tun soll, anstat "wie" es dies tun soll.),
        Logisches(Basiert auf formaler Logik; Regeln & Fakten),

3. Was ist ein Objekt und was eine Klasse?
    Klasse; ist wie eine Schablone/ Bauplan, der beschreibt, welche Eigenschaften(Attribute) und Werchaltensweisen(Methoden) Objekte haben sollen.
    Objekt; ist eine Instanz einer Klasse(ein konkretes Exemplar), das auf der Schablone der Klasse basiert. Es hat alle eigenschaften und Verhaltensweisen der Klasse(mit spezifischen werten)

4. Was versteht man unter Kapselung?
    Encapsulation verhindert direkten zugriff auf die Componenten(Attribute & Methoden) des Objektes.
    # Beispiel
    def __init__(self, kontostand):
        self.__kontostand = kontostand

5. Was ist Vererbung?
    Inheritance; ist ein Prinzip der oop, bei dem eine Klasse die eigenschaften einer anderen Klasse etbt(Kinklasse erbt von Elternklasse). Die "Kinderklasse" kann die geerbten Elemente erweitern oder überschreiben.

6. Was versteht man unter Refactoring?
    Refactoring bezeichnet den Prozess der Verbesserung des Quellcodes, ohne das Verhalten der Software zu verändern. Ziel ist es, den Code lesbarer, wartbarer und effizienter zu machen.

7. Welche Rolle spielt das Refactoring bzgl. der Wiederverwendung von Code?
    Refactoring; hilft den Code wiedervewenbar zu machen, indem es die Struktur verbessert und redudante Teile eliminiert.
    DRY: Vermeidung von Duplikaten
    Modularisierung; Zerlege den langen(molithischen) Code in kleinere, spezialisierte Module, Klassen oder Funktionen.

8. Für was gibt es die `__init__`-Funktion in einer Klasse?
    Die __init__ funktion ist ein Konstruktor in Python. Sie dient zur initialiesierung von Attributen und zur vorbereitung des Objektes für die Nutzung.

9. Für was braucht man den `self` Parameter?
    Der .self Parameter verweist auf das aktuelle Objekt(Instanz), das die Methode aufruft, und ermöglicht den Zugriff auf die Attribute und Methoden dieses spezifischen Objektes.

10. Wie schreibt man einzeilige und mehrzeilige Kommentare in Python?
    Einzeiliger Kommentar:      # This is the way
    Mehrzeiliger Kommentar:     '''
                                May
                                the Force be with
                                You
                                '''

11. Welche weiteren objektorientierten Programmiersprachen neben Python gibt es? (3 Beispiele)
    Java; verwenden wir in der Berufsschule
    C++; verwende ich im versuch ein Spiel zu schreiben
    C#; Modern und stark in der Windows-entwicklung(sagt das Internet)

12. Korrigiere die Fehlerhaften Skripte.

### Code 1
```python
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}")

obj = MyClass("Alice")
obj.greet()
```


### Code 2
```python
def say_hello():
    print("Hello, World!")  

say_hello()
```


### Code 3 
```python
x = 5
if x == 5:   
    print("x is 5")
```


### Code 4
```python
numbers = [1, 2, 3, 4, 5] 
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
```


### Code 5
```python
values = [1, 2, 3, 4, 5]
a, b, c = values[:3] # oder a, b, c = valuses[0], valuses[1], valuses[2],
```
