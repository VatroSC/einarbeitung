import json 
import mysql.connector
#import os


with open("base.json", "r") as file:
    json_data = json.load(file)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "2scalte18#",
    database = "secret_intel"
)

mycursor = mydb.cursor()

# SQL queries
squad_query = """
INSERT INTO Squad (squadName, homeTown, formed, amigood, secretBase, active)
VALUES (%s, %s, %s, %s, %s, %s)
"""
member_query = """
INSERT INTO Member (name, age, secretIdentity, sid)
VALUE (%s, %s, %s, %s)
"""
power_query = """
INSERT INTO Power (powerName, mid)
VALUE (%s, %s)
"""

for squad_data in json_data:
    squad = [
        squad_data["squadName"],
        squad_data["homeTown"],
        squad_data["formed"],
        squad_data["status"],
        squad_data["secretBase"],
        squad_data["active"]
    ]
    mycursor.execute(squad_query, tuple(squad))
    squad_id = mycursor.lastrowid #sid

    for member_data in squad_data["members"]:
        member = [
            member_data["name"],
            member_data["age"],
            member_data["secretIdentity"],
            squad_id
        ]
        mycursor.execute(member_query, tuple(member))
        member_id = mycursor.lastrowid

        for power_name in member_data["powers"]:
            power = (
                power_name, 
                member_id
                )
            mycursor.execute(power_query, power)

#mycursor.executemany()
mydb.commit()
mycursor.close()
mydb.close()     
# print()