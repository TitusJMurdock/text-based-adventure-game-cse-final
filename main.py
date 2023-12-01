
from classes import *
import time

        

def start_menu():
    global running
    print("You were flying over to see your family for Thanksgiving")
    time.sleep(wait)
    print("when suddenly the plane started shaking and people started panicking.\n")
    time.sleep(wait)
    print("You passed out and woke up to see yourself")
    time.sleep(wait)
    print("surrounded by flames, dead people, luggage,")
    time.sleep(wait)
    print("and parts of the plane scattered everywhere in the jungle.\n")
    time.sleep(wait)
    print("How you survived? Who knows.")
    time.sleep(wait)
    print("Find your way out of the jungle")
    time.sleep(wait)
    print("so you can get to your family in time for Thanksgiving.\n")
    time.sleep(wait)

    choice = (input("Would you like to go on an adventure? (yes or no) ")).lower()

    if choice == "yes":
        running = True
        
    elif choice == "no":
        running = False
        
    else:
        print("not a valid input")

player = Player("player_desc", [])



if __name__ == '__main__':
    start_menu()
    while player.alive == True:
        run_plane(player)
        #run_river(player)
        
        choice = run_river(player)
        if choice == 'left':
            choice = run_snakes(player) 
            if choice == 'over':
                run_fallen_tree(player)
                
            elif choice == 'through':
                run_spider_cave(player)
                
            else:
                break
        elif choice == 'right':
            
            choice = run_quicksand(player) 
            if choice == 'left':
                run_berries(player)
                
            elif choice == 'right':
                run_panther(player)
                break
            else:
                break
        run_end(player)
        break
    