import json

from squad import Squad
from member import Member

with open("/root/einarbeitung/base.json", "r") as file:
    data = json.load(file)

squads = []
for squad_data in data:
    squad = Squad(
        squad_data["squadName"],
        squad_data["homeTown"],
        squad_data["formed"],
        squad_data["status"],
        squad_data["secretBase"],
        squad_data["active"],
    )
    
    for member_data in squad_data["members"]:
        member = Member(
            member_data["name"],
            member_data["age"],
            member_data["secretIdentity"],
            member_data["powers"]
        )
        squad.member.append(member)
    squads.append(squad)


for squad in squads:
    print(squad)
    