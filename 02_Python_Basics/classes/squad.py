#import uuid
from member import Member

class Squad:
    def __init__(self, name: str, town: str, formed: int, status: str, base: str, active=True):
        self.name = name
        self.town = town
        self.formed = formed
        self.status = status
        self.base = base
        self.active = active
        self.member = []
        

    def __str__(self):
        members_detail = "\n".join(
            ["\t" + line for member in self.member for line in str(member).split("\n")])
        return (f"{'-'* 50}\n\n"
                f"Squad Name:\t{self.name}\n"
                f"Home Town:\t{self.town}\n"
                f"Formed in:\t{self.formed}\n"
                f"Status:\t\t{self.status}\n"
                f"Secret Base at:\t{self.base}\n"
                f"Stil Active?\t{self.active}\n\n"
                f"Members:\n{members_detail}")
                
    def add_member(self, name: str, age: int, identity: str, powers: list[str], member_id: str):
        #random_id = str(uuid.uuid4())
        new_member = Member(
            name = name,
            age = age,
            identity = identity,
            powers = powers,
            member_id = member_id
        )

        self.member.append(new_member)
        
    def remove_member(self, member_id: str):
        for member in self.member:
            if member_id == member.member_id:
                self.member.remove(member)
                return
        

'''        
# Test code
squad = Squad("Edge", "WTH", 1991, "active", "Hauptsitz")
squad.add_member("Ibo", 19, "Der coole", ["stabil", "gutaussehend", "schnell"], "1")
squad.add_member("Vatro", 33, "Rvat", ["Kaffe", "Musik", "Katzen"], "2")
print(squad.member[0])

squad.remove_member("1")
squad.remove_member("2")

if squad.member:
    print("Mitglieder im Squad sind:\n")
    for member in squad.member:
        print(member)
else:
    print("Keine weitere Mitglieder in diesem Squad (╥﹏╥)")
'''