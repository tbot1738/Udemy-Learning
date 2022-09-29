# OOP
class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def ru(self):
        print("run")


player1 = PlayerCharacter(name="Tbot")
player1.attack = 51
print(player1.attack)
