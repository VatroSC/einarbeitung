# Einrichten einer Virtual Machine (VM) unter Rocky Linux

## Beschreibung
In diesem Projekt wird eine Virtual Machine (VM) unter Rocky Linux eingerichtet. Es werden verschiedene Benutzer angelegt, die Partitionierung vorgenommen und verschiedene Programme installiert.

## Anleitung
Folge der Anleitung in der KnowledgeBase, um eine VM einzurichten. Stelle sicher, dass du die Scaltel Repos für den Packetmanager hinterlegst.

### Benutzer anlegen
- `root`: Der Hauptbenutzer mit vollständigen administrativen Rechten.
- `admin`: Ein Benutzer mit sudo-Berechtigungen.
- `entwickler`: Ein Benutzer ohne sudo-Berechtigungen.

### Partitionierung
- `/`: Das Stammverzeichnis.
- `/var/`: Das Verzeichnis für variable Daten.
- `/home/`: Das Verzeichnis für Benutzerdaten.

### Installierte Programme
a) GUI  
b) IDE  
c) Git  
d) Docker  
e) Python  
f) Docker-compose  

## Fragen und Antworten
- Was ist Linux und wie unterscheidet es sich von anderen Betriebssystemen wie Windows oder macOS?
    - Der Gröste unterschied ist der das Linux Open Source ist. Linux hat extrem viele Distributionen die man benutzen kann and viele von denen werden regelmäsig geupdated. In vergleich bei Windows und Mac Ist man gezwungen nur die Neuerste
- Was sind die Vorteile der Verwendung von Linux im Vergleich zu anderen Betriebssystemen?
    Im vergleich kann man Linux beser an die harware anpassen. Wo man bei Win oder macOS bestimmte hradware requirements hat kann man bei Linux eine Distro auswählen die mir passen. Dadurch ereichen wir mit Linux eine bessere preformance und energieefizienz.
- Was ist Virtualisierung und welche Vorteile bieten VMs?
    Virtualisierung ermöglicht die Aufteilung der Harware Ressourcen eines einzigen Computers (CPU, RAM, SSD usw) in mehrere virtuelle Computer. Vorteile von einer VM sind; Effizientere verwendung der Hardware, Erleichterte Simulations möglichkeiten, höhere sicherheit von ausenangriffen. 
- Was sind yum und dnf?
    Yum und Dnf sind packet manager für RPM(Redhat Packet Manager) basierte Linux distributionen. Dnf hat yum ersetzt als standard packet manager, yum wird noch in "Legacy" systemen benutzt.
- Was ist eine IDE und wie unterscheidet sie sich von einem Texteditor?
    IDE(Integrated Development Environment) ist ein Texteditor mit allen wichtigsten "Tools" für einen entwickler. Tools wie syntax highlighter, debugger, compiler, und vieles mehr. Mit einem Text editor können wir auch code schreiben, aber die IDE umgebung hat viele Tools die uns die Arbeit extrem erleichtern.
- Was ist der Unterschied zwischen einem LSP und einem Texteditor?
    LSP ist ein Protokol (Language Server Protocol) der ermöglicht die kommunikation zwischen IDEs und Schprach speziefischen Servern. Viele IDEs kommen mit einer LSP funktion z.B vscode, neovim usw.
- Wie kann man Programme im Hintergrund laufen lassen und Prozesse verwalten?
    Diese Frage verstehe ich nicht. Ich mach Youtube in einem Fenster auf und arbeite in vscode  
- Wie kann man Skripte unter Linux erstellen und ausführen?
    Man erstellt eine Datei und mit hilfe eines texteditors bearbeiten wir die. Den Script starten wir mit einem "shebang" um den Interpreter zu specifizieren z.B #!/bin/bash das sagt dem System Bash shell zu benutzen. Danach schreiben wir die commanden wie z.B echo "PoE2 ist mega gut". Nachdem wir unsere scripte geschrieben haben können wir die schpeichern ihr execution erlaubnis geben. danach können wir die scripte ausführen.
- Was ist ein Linux-Kernel und wie kann man ihn aktualisieren?
    Kernel ist eine schicht in linux OS die direkt mit dem Hardware Kommuniziert. erstens sollte man die repositories updaten, danach kann man die neueste wesion die in dem repo verfügbar ist instalieren. Nach der instalations sollte man das system neustarten und am schlus kann man überprüfen welche version der Kernel aktuell läuft um sicherzustellen das alles passt.
- Was sind symbolische Links und wie unterscheiden sie sich von Hardlinks?
    Ein Symlink zeigt den Pfad zu einer Datei an, wie eine Verknüpfung auf einem Desktop. Bei symlink wen die original Datei gelöscht wird funktioniert der symlink nicht mehr. Im gegensatz ein hardlink is in Prinzip eine weitere "Originaldatei" mit intentischen inhalt. 
- Welche Vorteile bietet die Nutzung von LTS (Long Term Support) Versionen einer Linux-Distribution?
    LTS versionen von distributionen werden länger unterschtüzt. Sind stabiler, oder anders gesagt haben nicht die "edge cutting" tehnologie sondern gut getestete komponenten die weniger Bugs haben. Ist sehr praktisch für individuen oder Unternehmen die so lang wie möglich eine stabile version benutzen wollen.
- Wie schreibt man Kommentare in Bash?
    Es gibt zwei möglichkeiten; Single line Kommentar benutzt man ein # und um ein Multy line Kommentar zu simulieren benutzt man : <<'EOF' 
- Was ist vim?
    Vim ist ein sehr Kompizierter text editor. vim ist eine verbesserte version von Vi und ist designet für Effiziente bearbeitung/bedienung.

### Linux-Befehle
Was bewirken folgende Befehle:
- `history`                 = zeigt eine liste von allen kommanden die gemacht wurden
- `chmod`                   = ändert die erlaubnise wer die Datei/Verzeichnis bearbeiten sehen oder ausfühern kann. nach 'chmod' müsst man noch definieren welches erlaubis und welche datei z.B 'chmod 755 beispiel.txt'
- `chown`                   = änder den eigentumer der Datei/Verceichnises. Z.B 'chown benutzer:gruppe beispiel.txt'
- `mv test.txt abc`         = mv schiebt oder übernent die Datei, test.txt ist datei tie betroffen ist, abc ist die destination wenn abc ein Verzeichnis ist wird test.txt in das Verzeichnis reingeschoben, sonst wird test.txt in abc unbenant.
- `ll | grep test`          = ll zeigt eine detalierte liste von Verzeichnisen und Dateien wie ls -l, | gibt den output von ll weiter and die nächste kommande und grep test filtert den output und zeigt nur den inhalt der test in Namen hat
- `find . -name cisco`      = find sucht nach Dateien/Verzeichnisen, . speziefiziert den Verzeichnis in den wir uns befinden als anfangspunkt für die suche, -name cisco sucht nach Dateien/Verceichnisen mit genauen namen cisco.
- `find / -name cisco`      = in diefem fall fängt die suche in dem root Verzeichniss an und sucht alle sub Verceicnise duch. Für so einen befehl ist es gut sudo zu benutzen um zugriff auf alle dateien zu haben.
- `tar -xvf archive.tar.gz` = tar erstellt oder extrachiert .tar archiven, -xvf sagt tar was er mit archive.tar.gz machen soll.
- `df -h`                   = df macht ein report von Disk space usage und -h(human) macht es für den menschen lesbar
- `du -sh directory`        = zeigt die gröse der Datei/Verzeichnises an. -sh, -s schaut nur die Verzeichnise und nicht sub Verzeichnise an und -h human readable
- `ps aux`                  = ps zeigt ein snapshot von aktuellen prozesen, aux a= zeigt alle prozesse an wen benutzt in kombination mit x, u= user oriented format
- `grep pattern file`       = in diesem beispiel sucht grep nach "pattern" in einer Datei namens file
- `top`                     = zeigt in echt Zeit ne übersicht von laufenden Programm
- `netstat -tuln`           = netstat zeigt die Information über Linux networking subsystemen. -tuln -t TCP -u UDP -l listening sockets -n numerical addresses and ports
- `ifconfig`                = ohne gegebenen argumenten ifconfig zeigt den status zuzeit aktiven "interfaces"
- `ping host`               = ping schickt ICMP echo request and spezifiezierte addresse(host)


