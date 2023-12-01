from interaction_parser import *
import textwrap
import time
import random

wait = 0

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
        self.tired = False

    def in_inventory(self, item):
        if item in self.inventory:
            return True
        else:
            return False
        
    def print_inventory(self):
        print("you have: ")
        for i in range(0, len(self.inventory)):
            print(self.inventory[i].name)



def d100(percent_chance):
    d100 = random.randint(1, 100)
    if d100 >= percent_chance:
        return 'Success!'
        
    elif d100 < percent_chance:
        return 'Failure. . .'

        
food = Interactable('food','a bag of beef jerky')
first_aid_kit = Interactable('first aid kit', 'a red box with a white cross, filled with medical supplies')
shrapnel = Interactable('shrapnel', 'a sharp piece of plane hull, could be useful as a tool or weapon')

def run_plane(player):
    desc = "you are in the jungle next to the crashed plane.\n On the ground you can see a bag of beef jerky, a first aid kit, and a sharp piece of shrapnel from the plane.\n Ahead you see a path through the trees. Beyond you can hear running water."
    
    interactables = [food, first_aid_kit, shrapnel]

    plane = Scene((textwrap.fill(desc) + '\n'), interactables)
    plane.describe()
    

    while player.alive == True:
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
                    break
                    
                

            elif interaction[0] == 'take' or interaction[0] == 'go' or interaction[0] == 'walk':
                if interaction[1] == 'path' or interaction[1] == 'road':
                    print('\n\n\n')
                    break
                    
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

        if river_crossed == True:
                print(textwrap.fill("You are on the other side of the river now. You can see two paths. To the left is a path that has absolutely no snakes. I promise! To the right is a path covered in some kind of sand."))
                interaction = parse_interaction()
                if interaction[1] == 'left':
                    return 'left'
                if interaction[1] == 'right':
                    return 'right'


        interaction = parse_interaction()

        try:

            if interaction == 'inventory':
                player.print_inventory()

            if interaction[0] == 'take' or interaction[0] == 'pick' or interaction[0] == 'drink':
                
                if (interaction[1] == 'tree'):
                    print("It's a tree. . . sorry superman, you can't lift it\n")

                if interaction[1] == 'leaf' or interaction[1] == 'boat':
                    print("It's to combersome to carry. You'll have to leave your vessel behind captain.\n")

                if (interaction[1] == 'rocks' or interaction[1] == 'stones'):
                    print("They are stuck fast in the riverbed. Good try though.\n")
                
                if (interaction[1] == 'water' or interaction[1] == 'river'):
                    print( "You died! The water was contaminated and you hallucinated to your death.\n"  )
                    input()
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
                    player.tired = True
            else:
                if (interaction[1] == 'tree'): 
                    tree.describe()
                elif interaction[1] == 'leaf' or interaction[1] == 'boat':
                    leaf_boat.describe()
                elif interaction[1] == 'rocks' or interaction[1] == 'stones' or interaction[1] == 'rock' or interaction[1] == 'stone':
                    rocks.describe()
            
            




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

        if snakes_gone == True:
                print(textwrap.fill("You manage to escape the snakes and come to a cave. The inside is dark and hard to see. You could go over the cave or brave the darkness and go through.\n"))
                interaction = parse_interaction()
                if interaction[1] == 'over':
                    return 'over'
                if interaction[1] == 'through':
                    return 'through'


        interaction = parse_interaction()

        try:

            if interaction == 'inventory':
                player.print_inventory()


            

            if interaction[0] == 'wrangle':
                print('Yeehaw')
                snakes_gone = True

            elif interaction[0] == 'take' or interaction[0] == 'pick':
                if interaction[1] == 'snake' or interaction[1] == 'snakes':
                    print("Are you crazy? No you can't pick up the snakes!\n")

            elif interaction[0] == 'hit' or interaction[0] == 'attack' or interaction[0] == 'kill' or interaction[0] == 'use' or interaction[0] == 'chop' or interaction[0] == 'cut' or interaction[0] == 'throw':
                if (interaction[1] == 'food' or interaction[1] == 'beef' or interaction[1] == 'jerky') and (food in player.inventory):
                    print('You throw your food at the snakes, distracting them for long enough to get away.\n')
                    player.inventory.remove(food)
                    snakes_gone = True
                elif (interaction[1] == 'food' or interaction[1] == 'beef' or interaction[1] == 'jerky') and (food not in player.inventory):
                    print("You throw your food at the snakes. . . oh wait. . . you don't have any food.\n")

                if (interaction[1] == 'snake' or interaction[1] == 'snakes' or interaction[1] == 'shrapnel' or interaction[1] == 'debris' or interaction[1] == 'plane' or interaction[1] == 'piece') and (shrapnel in player.inventory):
                    print("You try to fight the snakes with your shrapnel. So brave.\n")
                    time.sleep(wait)
                    print(f"Determining outcome… (50% chance of success)\n")
                    time.sleep(wait)
                    outcome = d100(50)

                    if outcome == 'Success!':
                        print(outcome)
                        print("All the snakes are gone\n")
                        snakes_gone = True
                    
                    else:
                        print(outcome)
                        time.sleep(wait)
                        if first_aid_kit in player.inventory:
                            print('Luckily you have a first aid kit!')
                            player.inventory.remove(first_aid_kit)
                        else:
                            print("You died! The snakes didn't like the taste of shrapnel so they had you for lunch. If only you had a first aid kit.\n")
                            input()
                            player.alive = False
                elif (interaction[1] == 'snake' or interaction[1] == 'snakes' or interaction[1] == 'shrapnel' or interaction[1] == 'debris' or interaction[1] == 'plane' or interaction[1] == 'piece') and (shrapnel not in player.inventory):
                    print("You don't have any weapons!")



            elif interaction[0] == 'run' or interaction[0] == 'leave' or interaction[0] == 'flee':
                if first_aid_kit in player.inventory:
                    print("A snake bit you as you ran away. Luckily you have a first aid kit!\n")
                    player.inventory.remove(first_aid_kit)
                else:
                    print("You died! You tripped over one of the snakes and got strangled to death by them.\n")
                    input()
                    player.alive = False
            else:
                if (interaction[1] == 'snake' or interaction[1] == 'snakes'): 
                    snakes.describe()
            


        except IndexError:
            print("I don't know that word. Try using at least two words, one action,\n and one object. (e.g. KILL SNAKES!!)\n")


def run_quicksand(player):
    desc = "The path ahead of you has a large pit of sand blocking you from the other side. There is a vine tangled around a tree, you could probably swing across if you could get it untangled. But it's just a bunch of sand, probably safe to just walk across, right?"
    quicksand = Interactable("quicksand", "A large pit of sand in the jungle. It doesn't seem suspicious.")
    vine = Interactable("vine", "A vine wrapped around a tree. You wonder if you could untie it. . .")
    interactables = [quicksand, vine]
    sand_crossed = False

    quicksand = Scene((textwrap.fill(desc) + '\n'), interactables)
    quicksand.describe()

    while player.alive == True:    

        if sand_crossed == True:
            print(textwrap.fill("You crossed the quicksand and see two more paths. The right path is overgrown and dark. The left path leads to a thicket of berry bushes.\n"))
            interaction = parse_interaction()
            if interaction[1] == 'left':
                return 'left'
            if interaction[1] == 'right':
                return 'right'
            
        interaction = parse_interaction()



        try:

            if interaction == 'inventory':
                player.print_inventory()


            if (interaction[0] == 'chop' or interaction[0] == 'cut' or interaction[0] == 'use') and (shrapnel in player.inventory):
                if interaction[1] == 'vine' or interaction[1] == 'shrapnel' or interaction[1] == 'debris' or interaction[1] == 'plane' or interaction[1] == 'piece':
                    
                    print("You try to cut the vine with your plane shrapnel.\n")
                    time.sleep(wait)
                    print(f"Determining outcome… (75% chance of success)\n")
                    time.sleep(wait)
                    outcome = d100(25)
                    if outcome == 'Success!':
                        print(outcome)
                        print("You cut the vine and use it to swing across!\n")
                        sand_crossed = True
                    
                    else:
                        print(outcome)
                        time.sleep(wait)
                        print("You managed to cut the vine and get across, but your shrapnel is rendered useless.")
                        player.inventory.remove(shrapnel)
                        sand_crossed = True

            elif interaction[0] == 'take' or interaction[0] == 'pick' or interaction[0] == 'get' or interaction[0] == 'touch':
                if interaction[1] == 'vine':
                    print("You can't get it down from the tree.\n")
                if interaction[1] == 'sand' or interaction[1] == 'quicksand':
                    print("You try to take some of the sand, but you notice something strange about it. . . it's quicksand! Good thing you checked")


            elif interaction[0] == 'cross' or interaction[0] == 'go' or interaction[0] == 'use' or interaction[0] == 'sail' or interaction[0] == 'jump' or interaction[0] == 'hop':
                if interaction[1] == 'sand' or interaction[1] == 'quicksand':
                    print("You try to walk through the sand and sink up to your knees immediately. It's quicksand.")

                    time.sleep(wait)
                    print(f"Determining outcome… (10% chance of success)\n")
                    time.sleep(wait)
                    outcome = d100(90)
                    if outcome == 'Success!':
                        if player.tired == True:
                            print('Failure. . .')
                            time.sleep(wait)
                            print("You died! You are already tired and don't have enough energy to make it.\n")
                            input()
                            player.alive = False
                        else:
                            print(outcome)
                            print("You somehow make it across the quicksand. You must be lucky!\n")
                            sand_crossed = True
                    elif outcome == 'Failure. . .':
                        print(outcome)
                        time.sleep(wait)
                        print("You died! You sank into the quicksand and trying to escape you died from exhaustion.")
                        player.alive = False
                        

            

                    
                else:
                    print(outcome)
                    time.sleep(wait)
                    print("You died! You sank into the quicksand and trying to escape you died from exhaustion.")
                    input()
                    player.alive = False

            elif interaction[1] == 'sand' or interaction[1] == 'quicksand':
                quicksand.describe()


        except IndexError:
            print("I don't know that word. Try using at least two words, one action,\n and one object. (e.g. take jerky)\n")



def run_fallen_tree(player):
    desc = "You see a fallen tree in your path. You could walk around it, but wouldn't it be cooler to jump over?"
    fallen_tree = Interactable("fallen_tree", "A tree fallen in the jungle. You didn't hear it; you wonder if it made a sound.")
    interactables = [fallen_tree]
    tree_crossed = False

    fallen_tree = Scene((textwrap.fill(desc) + '\n'), interactables)
    fallen_tree.describe()

    while player.alive == True:

        if tree_crossed == True:
            break

        interaction = parse_interaction()

        try:

            if interaction == 'inventory':
                player.print_inventory()

            if (interaction[0] == 'jump' or interaction[0] == 'hop' or interaction[0] == 'go'):
                if interaction[1] == 'tree':
                    print("You try to jump over the small tree.\n")
                    time.sleep(wait)
                    print(f"Determining outcome… (95% chance of success)\n")
                    time.sleep(wait)
                    outcome = d100(5)
                    if outcome == 'Success!':
                        print(outcome)
                        print("You jumped over the small tree. It would have been embarrassing to fail that one.\n")
                        tree_crossed = True
                    
                    else:
                        print(outcome)
                        time.sleep(wait)
                        print("You died! You fell and hit your head on a mysteriously sharp rock that sat on the ground. That's embarassing.")
                        input()
                        player.alave = False
                        tree_crossed = False
                
            if interaction[1] == 'path' or interaction[1] == 'around'  or interaction[1] == 'continue':
                print("You go around the tree and make it to the other side.")
                tree_crossed = True


        except IndexError:
            print("I don't know that word. Try using at least two words, one action,\n and one object. (e.g. take jerky)\n")


def run_spider_cave(player):
    print("You enter the dark cave, and the walls begin to move. You suddenly realize that it's filled with spiders!\n")
    if first_aid_kit in player.inventory:
        print("The spider bites hurt, but luckily your first aid kit has antivenom!")
    
    else:
        print("You died! You walked into the spiders' web and got fed to their spider babies. If only you had a first aid kit.")
        input()
        return
    

def run_berries(player):
    desc = "You come across a berry bush. Its fruit looks sweet, but you aren't sure how safe they are. You are getting very hungry. . ."
    berries = Interactable("berries", "A bush full of delicious looking berries.")
    interactables = [berries]
    

    berries = Scene((textwrap.fill(desc) + '\n'), interactables)
    berries.describe()

    while player.alive == True:

        interaction = parse_interaction()

        try:

            if interaction == 'inventory':
                player.print_inventory()
            

            if (interaction[0] == 'eat' or interaction[0] == 'take' or interaction[0] == 'go' or interaction[0] == 'get' or interaction[0] == 'walk'):
                if interaction[1] == 'berries' and berries in berries.interactables:
                    print("You eat the berries. They taste pretty good.\n")
                    time.sleep(wait)
                    print(f"Determining outcome… (50% chance of success)\n")
                    time.sleep(wait)
                    outcome = d100(50)
                    if outcome == 'Success!':
                        print(outcome)
                        print("The berries were perfectly safe. Good intuition!\n")
                        berries.interactables.remove(berries)
                    
                    else:
                        print(outcome)
                        time.sleep(wait)
                        if first_aid_kit in player.inventory:
                            print("Those berries were definitely poisonous. . . but luckily you had your first aid kit!")
                            berries.interactables.remove(berries)
                        else:
                            print("You died! The berries were poisonous and time started slowing down until it stopped (For you at least).")
                            input()
                            player.alive = False

                if interaction[1] == 'berries' and berries not in berries.interactables:
                    print("You already ate those.")
            
            if interaction[0] == 'cross' or interaction[0] == 'walk' or interaction[0] == 'go' or interaction[0] == 'take':
                if interaction[1] == 'path' or interaction[1] == 'road' or interaction[1] == 'around':
                    if food in player.inventory:
                        print("You pass the bush and decide to eat your food instead of risking it with the berries.")
                        return
                    elif food not in player.inventory:
                        print("You died! Although you are hungry, you decide to walk past the bush. You have no other food so you starve in the jungle.")
                        input()
                        player.alive = False





        except IndexError:
            print("I don't know that word. Try using at least two words, one action,\n and one object. (e.g. take jerky)\n")


def run_panther(player):
    print("You approach the overgrown path. You realize that you have stumbled into a panther's territory, and it looks big!")
    parse_interaction()
    print("You died! The panther was bored so it killed you for entertainment.")
    return



    


def run_end(player):

    textwrap.fill("After your perilous journey, you finally make it back to civilization. You see a classic middle-of-the-jungle airport! We all know about those! Hopefully you can get a ticket on such short notice.")
    print('\n\n\n\n')
    print(' __   __  _______  __   __    _     _  ___   __    _  __   __   __   __  ')
    print('|  | |  ||       ||  | |  |  | | _ | ||   | |  |  | ||  | |  | |  | |  | ')
    print('|  |_|  ||   _   ||  | |  |  | || || ||   | |   |_| ||  | |  | |  | |  | ')
    print('|       ||  | |  ||  |_|  |  |       ||   | |       ||  | |  | |  | |  | ')
    print('|_     _||  |_|  ||       |  |       ||   | |  _    ||__| |__| |__| |__| ')
    print('  |   |  |       ||       |  |   _   ||   | | | |   | __   __   __   __  ')
    print('  |___|  |_______||_______|  |__| |__||___| |_|  |__||__| |__| |__| |__| ')
    return
