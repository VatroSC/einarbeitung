# dbms == Datenbank Management System
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user =  "root",
    password = "2scalte18#",
    database = "secret_intel"
)

mc = mydb.cursor() # mc == mycursor

# Daten hinzufügen
in_squad = """
INSERT INTO Squad (squadName, homeTown, formed, amigood, secretBase, active)
Values (%s, %s, %s, %s, %s, %s)
"""
member = """
INSERT INTO Member (name, age, secretIdentity, sid)
VALUE (%s, %s, %s, %s)
"""
power = """
INSERT INTO Power (powerName, mid)
VALUE (%s, %s)
"""
# Daten Löschen
del_squad = """
DELETE FROM Squad WHERE squadName="%s" OR homeTown="%s" OR formed="%s" OR amigood="%s" OR secretBase="%s" OR active="1" OR active="0";
"""
del_member = """
DELETE FROM Member WHERE name="%s" OR age="%s" OR secretIdentity="%s"
"""
del_power = """
DELETE FROM Power WHERE powerName="%s"
"""
# Daten bearbeiten ch == change
ch_squad = """
UPDATE Squad
SET
    squadName ="%s", 
    homeTown ="%s",
    formed ="%s",
    amigood ="%s",
    secretBase ="%s",
    active ="1", 
    active ="0"
"""
# Daten auslesen

