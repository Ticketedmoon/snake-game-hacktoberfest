import random

class Food():
    def __init__(self):
        self.position = [random.randrange(1, 50)*10,
             random.randrange(1, 50)*10]
        self.isFoodOnScreen = True

    def spawnFood(self):
        if (self.isFoodOnScreen == False):
            self.position = [random.randrange(1, 50)*10,
             random.randrange(1, 50)*10]
            self.isFoodOnScreen = True
        return self.position

    def setFoodOnScreen(self, boolean):
        self.isFoodOnScreen = boolean;

