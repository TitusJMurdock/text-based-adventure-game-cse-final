from interaction_parser import *
import textwrap


class Scene:
    def __init__(self, description, interactables):
        self.description = description
        self.interactables = interactables
        self.interactables_names = ()
        #for i in self.interactables:
        #    self.interactables_names[i] = interactables[i].name

    def describe(self):
        print(self.description)


def run_plane(player):
    in_scene = True
    desc = "you are in the jungle next to the crashed plane.\n On the ground you can see a bag of beef jerky, a first aid kit, and a sharp piece of shrapnel from the plane.\n Ahead you see a path through the trees. Beyond you can hear running water."
    food = Interactable('food','a bag of beef jerky')
    first_aid_kit = Interactable('first aid kit', 'a red box with a white cross, filled with medical supplies')
    shrapnel = Interactable('shrapnel', 'a sharp piece of plane hull, could be useful as a tool or weapon')
    interactables = [food, first_aid_kit, shrapnel]

    plane = Scene((textwrap.fill(desc)), interactables)
    plane.describe()
    

    while in_scene:
        interaction = parse_interaction()
        
        try:

            if interaction == 'inventory':
                player.print_inventory()

            #will run if the player wants to pick something up
            if interaction[0] == 'take' or interaction[0] == 'pick':
                #player picks up food
                if (interaction[1] == 'food' or interaction[1] == 'beef' or interaction[1] == 'jerky') and (food in plane.interactables):
                    player.inventory.append(food)
                    plane.interactables.remove(food)
                #player cannot take food twice
                elif (interaction[1] == 'food' or interaction[1] == 'beef' or interaction[1] == 'jerky') and (food not in plane.interactables):
                    print('you already have that')

                if (interaction[1] == 'first' or interaction[1] == 'kit' or interaction[1] == 'medicine' or interaction[1] == 'aid') and (first_aid_kit in plane.interactables):
                    player.inventory.append(first_aid_kit)
                    plane.interactables.remove(first_aid_kit)
                elif (interaction[1] == 'first' or interaction[1] == 'kit' or interaction[1] == 'medicine' or interaction[1] == 'aid') and (first_aid_kit not in plane.interactables):
                    print('you already have that')

                if (interaction[1] == 'shrapnel' or interaction[1] == 'debris' or interaction[1] == 'plane' or interaction[1] == 'piece') and (shrapnel in plane.interactables):
                    player.inventory.append(shrapnel)
                    plane.interactables.remove(shrapnel)
                elif (interaction[1] == 'shrapnel' or interaction[1] == 'debris' or interaction[1] == 'plane' or interaction[1] == 'piece') and (shrapnel not in plane.interactables):
                    print('you already have that')

            if interaction[0] == 'take' or interaction[0] == 'go' or interaction[0] == 'walk':
                if interaction[1] == 'path' or interaction[1] == 'road':
                    run_river(player)

        
        except IndexError:
            print("I don't know that word")
    
def run_river(player):
    pass


class Interactable:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        


    def describe(self):
        print(self.description)



class Player:
    def __init__(self, description, inventory):
        self.description = description
        self.alive = True
        self.inventory = inventory

    def in_inventory(self, item):
        if item in self.inventory:
            return True
        else:
            return False
        
    def print_inventory(self):
        print("you have: ")
        for i in range(0, len(self.inventory)):
            print(self.inventory[i].name)

        #print(f"You have {self.inventory}")