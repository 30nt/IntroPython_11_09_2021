class UnitGame:

    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self.power = 1
        self.dexterity = 1
        self.intellect = 1

    def __str__(self):
        return f"name: {self.name}, " \
               f"clan: {self.clan}, " \
               f"health: {self.health}, " \
               f"power: {self.power}, " \
               f"dexterity: {self.dexterity}, " \
               f"intellect: {self.intellect}"

    def __repr__(self):
        return f"{self.name} - {self.health}"

    def treatment_unit(self):
        self.health += 10
        if self.health > 100:
            self.health = 100
        # elif self.health == 0:
        #     return "Game over"
        # else:
        #     return "Full health"

    def power_unit(self):
        self.power += 1
        if self.power > 10:
            self.power = 10

    def dexterity_unit(self):
        self.dexterity += 1 if self.dexterity < 10 else 0

    def intellect_unit(self):
        self.intellect += 1 if 0 < self.intellect < 10 else print("Check your intellect")

    def clan_unit(self):
        if self.clan:
            return f"{self.name} - {self.clan}"
        # if self.clan == "standart" or self.clan == "soldier" or self.clan == "scientist":
        #     return f"{self.name} - {self.clan}"
        else:
            return "Set your clan"