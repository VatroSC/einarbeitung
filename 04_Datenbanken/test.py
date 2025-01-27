import mysql.connector
#! DEBUG DATEI
mydb = mysql.connector.connect(
    host = "localhost",
    user =  "root",
    password = "2scalte18#",
    database = "secret_intel"
)
mc = mydb.cursor() # mc == mycursor

def addmember():
    in_member = """
    INSERT INTO Member (name, age, secretIdentity, sid)
    VALUE (%s, %s, %s, %s)
    """
    print("Bitte geben sie die Details für den Member ein:")
    name = input("Helden Name:\t")
    age = input("Alter:\t")
    #mid = 
    secretIdentity = input("Was ist seine geheime Identität:\t")
    mc.execute(in_member, (name, age, secretIdentity))
    mydb.commit()
    print(f"Du hast {name} hinzugefügt.")

    # Display available squads to select `sid`
    mc.execute("SELECT sid, squadName FROM Squad")
    squads = mc.fetchall()
    print("Wählen Sie einen Squad für diesen Member:")
    for squad in squads:
        print(f"ID: {squad[0]}, Name: {squad[1]}")
    sid = int(input("Geben Sie die Squad-ID ein:\t"))

    # Insert the member into the database
    mc.execute(in_member, (name, age, secretIdentity, sid))
    mydb.commit()
    print(f"Du hast {name} dem Squad mit der ID {sid} hinzugefügt.")


addmember()