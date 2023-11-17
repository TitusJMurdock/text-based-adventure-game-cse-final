

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

class Player:
    def __init__(self, description, inventory, scene):
        self.description = description
        self.alive = True
        self.inventory = inventory
        self.scene = scene

    def in_inventory(self, item):
        if item in self.inventory:
            return True
        else:
            return False
        
    def print_inventory(self):
        print(f"You have {self.inventory}")
        



def start_menu():
    choice = (input("Would you like to go on an adventure? (yes or no) ")).lower()

    if choice == "yes":
        running = True
        return running
    elif choice == "no":
        running = False
        return running
    else:
        print("not a valid input")





if __name__ == '__main__':
    running = False
    door = Interactable("a simple door, it could be locked", ["key", "hammer"])
    bush = Interactable("just a bush", ["machete", "match"])


    scene1 = Scene("a test scene", [door, bush])
    while running == True:
        pass
        
    player = Player("description", 10, 1, ["key", "something"], scene1)