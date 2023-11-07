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
    
    def do_damage(self, Player):
        Player.hp = Player.hp - self.damage

class Player(Enemy):
    def __init__(self, description, hp, damage, inventory,):
        super().__init__(description, hp, damage)
        self.inventory = inventory
        for i in inventory:
            if inventory[i] == "machete":
                self.damage = 3
            else:
                self.damage = damage


def start_menu():
    choice = input("Would you like to go on an adventure? (yes or no)").lower
    if choice == "yes":
        return True
    else:
        return False





if __name__ == '__main__':
    running = True
    running = start_menu()
    while running == True:
        door = Interactable("a simple door, it could be locked", ["key", "hammer"])
        bush = Interactable("just a bush", ["machete", "match"])


        scene1 = Scene("a test scene", [door, bush])
        
        player = Player("the player", 10, 1, ["key", "other thing"] )
        print("running")