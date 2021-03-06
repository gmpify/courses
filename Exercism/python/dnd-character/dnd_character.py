from random import randint

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        dice = [randint(1, 6) for i in range(4)]
        return sum(dice) - min(dice)

def modifier(value):
    return (value - 10) // 2
