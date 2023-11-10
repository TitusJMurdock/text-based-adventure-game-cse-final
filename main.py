#creating scene object

class Scene:
    def __init__(self, description, interactables):
        self.description = description
        self.interactables = interactables

    def describe(self):
        print(self.description)

class Interactable:
    def __init__(self, description, interaction_items):
        self.description = description
        self.interaction_items = interaction_items

    def describe(self):
        print(self.description)

class Enemy:
    def __init__(self, description, hp, damage):
        self.description = description
        self.hp = hp
        self.damage = damage
        self.alive = True
        
    
    def do_damage(self, Player):
        Player.hp = Player.hp - self.damage
    
    def update(self):
        if self.hp == 0:
            self.alive = False


class Player(Enemy):
    def __init__(self, description, hp, damage, inventory,):
        super().__init__(description, hp, damage)
        self.inventory = inventory
        

    def update(self):
        if self.hp == 0:
            self.alive = False

        if "machete" in self.inventory:
            self.damage = 3


def start_menu():
    choice = (input("Would you like to go on an adventure? (yes or no) ")).lower()

    if choice == "yes":
        return True
    elif choice == "no":
        return False
    else:
        print("not a valid input")





if __name__ == '__main__':
    running = False
    door = Interactable("a simple door, it could be locked", ["key", "hammer"])
    bush = Interactable("just a bush", ["machete", "match"])


    scene1 = Scene("a test scene", [door, bush])
    while running == True:
        pass
        
    player = Player("description", 10, 1, ["key", "something"])
    python = Enemy("a scary snake", 5, 10)
    print(player.hp)
    print(player.alive)
    python.do_damage(player)
    player.update()
    print(player.hp)
    print(player.alive)