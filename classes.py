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





class Interactable:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        


    def describe(self):
        print(self.description + '\n')



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

        
food = Interactable('food','a bag of beef jerky')
first_aid_kit = Interactable('first aid kit', 'a red box with a white cross, filled with medical supplies')
shrapnel = Interactable('shrapnel', 'a sharp piece of plane hull, could be useful as a tool or weapon')

def run_plane(player):
    desc = "you are in the jungle next to the crashed plane.\n On the ground you can see a bag of beef jerky, a first aid kit, and a sharp piece of shrapnel from the plane.\n Ahead you see a path through the trees. Beyond you can hear running water."
    
    interactables = [food, first_aid_kit, shrapnel]

    plane = Scene((textwrap.fill(desc) + '\n'), interactables)
    plane.describe()
    

    while player.alive:
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
                    print('Took food\n')
                #player cannot take food twice
                elif (interaction[1] == 'food' or interaction[1] == 'beef' or interaction[1] == 'jerky') and (food not in plane.interactables):
                    print('you already have that\n')

                if (interaction[1] == 'first' or interaction[1] == 'kit' or interaction[1] == 'medicine' or interaction[1] == 'aid') and (first_aid_kit in plane.interactables):
                    player.inventory.append(first_aid_kit)
                    plane.interactables.remove(first_aid_kit)
                    print('Took first aid kit\n')
                elif (interaction[1] == 'first' or interaction[1] == 'kit' or interaction[1] == 'medicine' or interaction[1] == 'aid') and (first_aid_kit not in plane.interactables):
                    print('you already have that\n')

                if (interaction[1] == 'shrapnel' or interaction[1] == 'debris' or interaction[1] == 'plane' or interaction[1] == 'piece') and (shrapnel in plane.interactables):
                    player.inventory.append(shrapnel)
                    plane.interactables.remove(shrapnel)
                    print('Took shrapnel\n')
                elif (interaction[1] == 'shrapnel' or interaction[1] == 'debris' or interaction[1] == 'plane' or interaction[1] == 'piece') and (shrapnel not in plane.interactables):
                    print('you already have that\n')
                
                if (interaction[1] == 'path' or interaction[1] == 'road'):
                    print('\n\n\n')
                    run_river(player)
                

            elif interaction[0] == 'take' or interaction[0] == 'go' or interaction[0] == 'walk':
                if interaction[1] == 'path' or interaction[1] == 'road':
                    print('\n\n\n')
                    run_river(player)
            else:
                if (interaction[1] == 'food' or interaction[1] == 'beef' or interaction[1] == 'jerky'):
                    food.describe()
                elif (interaction[1] == 'first' or interaction[1] == 'kit' or interaction[1] == 'medicine' or interaction[1] == 'aid'):
                    first_aid_kit.describe()
                elif (interaction[1] == 'shrapnel' or interaction[1] == 'debris' or interaction[1] == 'plane' or interaction[1] == 'piece'):
                    shrapnel.describe()

        
        except IndexError:
            print("I don't know that word. Try using at least two words, one action,\n and one object. (e.g. take jerky)\n")
    
def run_river(player):

    desc = 'You come across a river in the jungle. The paths ahead lie on the other side. There is a small tree nearby that you may be able to chop down to make a bridge, although you aren’t sure how. There are a few rocks jutting out from the surface, you could jump across, but it would take some effort. There is a large fallen leaf near the shore, it is big enough to hold you. Now that you are thinking about it, you are a little thirsty. . .'
    tree = Interactable('tree', 'A small tree. You could probably cut it down if you had something sharp. . .')
    leaf_boat = Interactable('leaf boat', 'A really big leaf! Maybe you could try to float across?')
    rocks = Interactable('rocks', 'A series of rocks you could jump across, but maybe you should conserve energy?')
    interactables = [tree, leaf_boat, rocks]
    river_crossed = False

    river = Scene((textwrap.fill(desc) + '\n'), interactables)
    river.describe()

    while player.alive == True:
        interaction = parse_interaction()

        try:
            if interaction[0] == 'take' or interaction[0] == 'pick' or interaction[0] == 'drink':
                
                if (interaction[1] == 'tree'):
                    print("It's a tree. . . sorry superman, you can't lift it\n")

                if interaction[1] == 'leaf' or interaction[1] == 'boat':
                    print("It's to combersome to carry. You'll have to leave your vessel behind captain.\n")

                if (interaction[1] == 'rocks' or interaction[1] == 'stones'):
                    print("They are stuck fast in the riverbed. Good try though.\n")
                
                if (interaction[1] == 'water' or interaction[1] == 'river'):
                    print( "You died! The water was contaminated and you hallucinated to your death.\n"  )
                    player.alive = False
            
            elif interaction[0] == 'chop' or interaction[0] == 'cut':
                if (interaction[1] == 'tree') and (shrapnel in player.inventory):
                    print("You use your shrapnel to chop down the tree. It isn't a sturdy tool though so it breaks.\n")
                    player.inventory.remove(shrapnel)
                    river_crossed = True
                elif (interaction[1] == 'tree') and (river_crossed == True):
                    print("You already have a way across the river.\n")
                elif (interaction[1] == 'tree') and (shrapnel not in player.inventory):
                    print("You try to chop the tree. . . with what, your hands? The tree remains standing.\n")
            elif interaction[0] == 'cross' or interaction[0] == 'go' or interaction[0] == 'use' or interaction[0] == 'sail' or interaction[0] == 'jump' or interaction[0] == 'hop':
                if river_crossed == True:
                    print("You already have a way across the river.\n")
                elif interaction[1] == 'leaf' or interaction[1] == 'boat':
                    print("You died! The leaf wasn't buoyant so you fell into the water and got eaten by piranhas.\n")
                    player.alive = False
                elif interaction[1] == 'rocks' or interaction[1] == 'stones' or interaction[1] == 'rock' or interaction[1] == 'stone':
                    print("You managed to jump across with the rocks. You feel tired now, but at least you made it.\n")
                    river_crossed = True
            else:
                if (interaction[1] == 'tree'): 
                    tree.describe()
                elif interaction[1] == 'leaf' or interaction[1] == 'boat':
                    leaf_boat.describe()
                elif interaction[1] == 'rocks' or interaction[1] == 'stones' or interaction[1] == 'rock' or interaction[1] == 'stone':
                    rocks.describe()
            
            if river_crossed == True:
                print(textwrap.fill("You are on the other side of the river now. You can see two paths. To the left is a path that has absolutely no snakes. I promise! To the right is a path covered in some kind of sand."))
                interaction = parse_interaction()
                if interaction[1] == 'left':
                    run_snakes(player)
                if interaction[1] == 'right':
                    run_quicksand(player)




        except IndexError:
            print("I don't know that word. Try using at least two words, one action,\n and one object. (e.g. take jerky)\n")


def run_snakes(player):
    desc = 'You approach the seemingly snake-less path to discover your folly. SNAKES!!! They are rapidly approaching.'
    snakes = Interactable('snakes', 'A pack of angry snakes')
    interactables = [snakes]
    snakes_gone = False

    snakes_scene = Scene((textwrap.fill(desc) + '\n'), interactables)
    snakes_scene.describe()

    while player.alive == True:
        interaction = parse_interaction()

        try:
            if interaction[0] == 'take' or interaction[0] == 'pick':
                if interaction[1] == 'snake' or interaction[1] == 'snakes':
                    print("Are you crazy? No you can't pick up the snakes!")

        except IndexError:
            print("I don't know that word. Try using at least two words, one action,\n and one object. (e.g. KILL SNAKES!!)\n")

