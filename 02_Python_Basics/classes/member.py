
class Member:
    def __init__(self, name: str, age: int, identity: str, powers: list[str], member_id: str):
        self.name = name
        self.age = age
        self.identity = identity
        self.powers = powers
        self.member_id = member_id

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nSecret Identity: {self.identity}\nPowers; {','.join(self.powers)}\nID; {self.member_id}\n"