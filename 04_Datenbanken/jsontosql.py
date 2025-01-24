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

...
 
mycursor.executemany()
mydb.commit()

'''
for squad_data in json_data:
    squad = [
        squad_data["squadName"],
        squad_data["homeTown"],
        squad_data["formed"],
        squad_data["status"],
        squad_data["active"]
    ]

    for member_data in squad_data["members"]:
        member = [
            member_data["name"],
            member_data["age"],
            member_data["secretIdentity"]
        ]
        

        for power_list in member_data["powers"]:
            power = [str]
'''

     
# print()
# print()