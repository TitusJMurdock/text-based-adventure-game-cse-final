#funtion for parsing input
action_keywords = ['look', 'search', 'take', 'pick', 'inventory']
interactable_keywords = ['food', 'beef', 'jerky', 'first', 'aid', 'kit', 'medicine', 'shrapnel', 'debris', 'plane', 'piece']


def parse_interaction():
    #define what actions and interactables exist
    

    #take input and split into list
    text = (input("What will you do? (type 'inventory' to see your items) ")).lower()
    if text == ('inventory' or 'quit'): interaction = text; return interaction
    text = text.split()

    #returns 2 lists, one the action and two the interactable
    action = list(set(text) & set(action_keywords))
    interactable = list(set(text) & set(interactable_keywords))

    #combines action and interactale into tuple
    #action is always index 0, interactable is always index 1
    interaction = tuple(action + interactable)

    

    return interaction

    