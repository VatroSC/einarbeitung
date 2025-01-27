# dbms == Datenbank Management System
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user =  "root",
    password = "2scalte18#",
    database = "secret_intel"
)
mc = mydb.cursor() # mc == mycursor

# Funktionen ---------------------------------------------------------------------------
    #User adds  
        #? def add() und in add andere def wie addsquad, add member und addpower nesten?
def addsquad():
    in_squad = """
    INSERT INTO Squad (squadName, homeTown, formed, amigood, secretBase, active)
    Values (%s, %s, %s, %s, %s, %s)
    """
    print("Bitte geben sie die Details für den Squad ein:")
    squadName = input("Squad Name:\t")
    homeTown = input("Heimatstadt:\t")        
    formed = int(input("Gründungsjahr:\t"))
    amigood = input("Status wie z.B. 'gut', 'neutral', 'böse'\n\t+")
    secretBase = input("Geheinbase:\t")
    active = bool(int(input("Aktiv? (1 = JA oder 0 = Nein)"))) 
    mc.execute(in_squad, (squadName, homeTown, formed, amigood, secretBase, active)) #? was mit squd id? suto generiert mit AUTO_INCREMENT?
    mydb.commit()
    print(f"Du hast {squadName} hinzugefügt.")
def addmember():
    in_member = """
    INSERT INTO Member (name, age, secretIdentity, sid)
    VALUE (%s, %s, %s, %s)
    """
    print("Bitte geben sie die Details für den Member ein:")
    name = input("Helden Name:\t")
    age = input("Alter:\t")
    secretIdentity = input("Was ist seine geheime Identität:\t")
    mc.execute(in_member, (name, age, secretIdentity))
    mydb.commit()
    print(f"Du hast {name} hinzugefügt.")
def addpower():
    in_power = """
    INSERT INTO Power (powerName, mid)
    VALUE (%s, %s)
    """
    print("Bitte geben sie Powers die der Member hat ein:")
    powerName = input(f"Geb die Powers ein (mit , endet eine power und fängt die nächste an):\n\n\t")
    powerName = powerName.split(",")
    for power in powerName:
        mc.execute(in_power, (power, in_power.mid))
    #mc.execute(in_power, (powerName))
    mydb.commit()

    # User deletes
def delsquad():
    del_squad = """
    DELETE FROM Squad WHERE squadName=%s OR homeTown=%s OR formed=%s OR amigood=%s OR secretBase=%s OR active="1" OR active="0";
    """
    mc.execute("SELECT squadName FROM Squad")
    squads = mc.fetchall()
    for squad in squads:
        print(f"Welchen Squad möchtest do löschen?\n\n{squad}")
    squadName = input("Squad Name:\t")
    mc.execute(del_squad, (squadName))
    mydb.commit()
    print(f"{squadName} wude für immer gelöscht")
def delmember():
    del_member = """
    DELETE FROM Member WHERE name=%s OR age=%s OR secretIdentity=%s
    """
    mc.execute("SELECT name FROM Member")
    members = mc.fetchall()
    for member in members:
        print(f"Welchen Member Möchtest du löschen?\n\n {member}")
    name = input("Member Name:\t")
    mc.execute(del_member, (name))
    mydb.commit()
def delpower():
    del_power = """
    DELETE FROM Power WHERE powerName=%s
    """
    mc.execute("SELECT Member.name, Power.powerName FROM Member INNER JOIN Power ON Member.mid = Power.mid") #? Will eigentlich member und deren powers anzeigen
    powers = mc.fetchall()
    for power in powers:
        print(f"Welche powers möchtest du löschen?\n\n {power}") 
    powerName = input(f"Powers (mit , endet eine power und fängt die nächste an):\n\t")
    powerName = powerName.split(",")
    mc.execute(del_power, (powerName))
    mydb.commit()

    # User updates/changes
def upsquad():
    up_squad = """
    UPDATE Squad
    SET
        squadName =%s, 
        homeTown =%s,
        formed =%s,
        amigood =%s,
        secretBase =%s,
        active ="%s"
    """
    mc.execute("SELECT squadName FROM Squad")
    squads = mc.fetchall()
    for squad in squads:
        print(f"Welchen Squad möchtest do umbenenen?\n\n{squad}")
    squadName = input("Squad Name:\t")
    mc.execute(up_squad, (squadName))
    mydb.commit()
def upmember():
    up_member = """
    UPDATE Member
    SET
       name =%s,
       age =%s,
       secretIdentity =%s 
    WHERE mid=%s
    """
    mc.execute("SELECT Squad.squadName, Member.name FROM Member INNER JOIN Squad ON Member.sid = Squad.sid") #? I do not know if this is good
    members = mc.fetchall() 
    for member in members:
        print(f"Welchen Member möchtest do umbenenen?\n\n{member}")
    name = input("Member Name:\t")
    mc.execute(up_member, (name))
    mydb.commit()
def uppower():
    up_power = """
    SET
        powerName =%s
    WHERE pid=%s
    """
    mc.execute("SELECT Member.name, Power.powerName FROM Member INNER JOIN Power ON Member.mid = Power.mid")
    powers = mc.fetchall() 
    for power in powers:
        print(f"Welchen Power möchtest do umbenenen?\n\n{power}")
    name = input("Power Name:\t")
    mc.execute(up_power, (power))
    mydb.commit()

# Benutzer eingabe ---------------------------------------------------------------
while True:
    wahl = input(f"Möchtest du:\n\tHinzufügen (1)\tLöschen (2)\tÄndern (3)\tAnzeige (4)\tProgram beenden (0)\n\n")
    if wahl == "0":
        break 
    # Hinzufügen
    if wahl == "1":
        hinzu = input(f"Was willst du hinzufügen:\n\tSquad (1)\n\tMember (2)\n\tPower (3)\n\n")
        if hinzu == "1":
            try:
                addsquad()
            except mysql.connector.Error as err:
                print(f"Etwas passt mit Squad nicht:\t{err}") # Error catch
        elif hinzu == "2":
            try:
                addmember()
            except mysql.connector.Error as err:
                print(f"Etwas passt mit Member nicht:\t{err}")
        elif hinzu == "3":
            try:
                addpower()
            except mysql.connector.Error as err:
                print(f"Etwas passt mit Power nicht:\t{err}")
        else:
            print(f"hmm... WUT!!! *add() geht nicht")   
    
    # Löschen
    if wahl == "2":
        loeschen = input(f"Was willst du löschen:\n\tSquad (1)\n\tMember (2)\n\tPower (3)\n\n")
        if loeschen == "1":
            try:
                delsquad()
            except mysql.connector.Error as err:
                print(f"Etwas passt mit Squad nicht:\t{err}")
        elif loeschen == "2":
            try:
                delmember()
            except mysql.connector.Error as err:
                print(f"Etwas passt mit Member nicht:\t{err}")
        elif loeschen == "3":
            try:
                delpower()
            except mysql.connector.Error as err:
                print(f"Etwas passt mit Power nicht:\t{err}")
        else:
            print(f"hmm... WUT!!! *del() geht nicht")     

    # Ändern
    if wahl == "3":
        change = input(f"Was willst du Ändern:\n\tSquad (1)\n\tMember (2)\n\tPower (3)\n\n")
        if change == "1":
            try:
                upsquad()
            except mysql.connector.Error as err:
                print(f"Etwas passt mit Squad nicht:\t{err}")
        elif change == "2":
            try:
                upmember()
            except mysql.connector.Error as err:
                print(f"Etwas passt mit Member nicht:\t{err}")
        elif change == "3":
            try:
                uppower()
            except mysql.connector.Error as err:
                print(f"Etwas passt mit Power nicht:\t{err}")
        else:
            print(f"hmm... WUT!!! *up() geht nicht")   

        # Anzeigen
    if wahl == "4":
        alldata = """
        SELECT Squad.squadName, Member.name AS memberName, Power.powerName 
        FROM Squad 
        INNER JOIN Member 
        ON Squad.sid = Member.sid 
        INNER JOIN Power 
        ON Member.mid = Power.mid
        """
        mc.execute(alldata)
        
#todo ( ˘▽˘)っ♨ヘ(￣ω￣ヘ)