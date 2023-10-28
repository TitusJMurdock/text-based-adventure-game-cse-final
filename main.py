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


if __name__ == '__main__':

    door = Interactable("a simple door, it could be locked", ["key", "hammer"])
    bush = Interactable("just a bush", ["machete", "match"])


    scene1 = Scene("a test scene", [door, bush])
    scene1.describe()
    print(scene1.interactables)