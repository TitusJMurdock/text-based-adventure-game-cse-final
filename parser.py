#funtion for parsing input
def parse():
    #define what actions and interactables exist
    action_keywords = ['look', 'open', 'attack']
    interactable_keywords = ['painting', 'door', 'python']

    #take input and split into list
    text = (input()).lower()
    text = text.split()

    #returns 2 lists, one the action and two the interactable
    action = list(set(text) & set(action_keywords))
    interactable = list(set(text) & set(interactable_keywords))

    #combines action and interactale into tuple
    #action is always index 0, interactable is always index 1
    interaction = tuple(action + interactable)

    return interaction

    