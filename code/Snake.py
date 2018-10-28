import pygame
import sys

class Snake():
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"
        self.changeDirectionTo = self.direction

    def changeDirectionOfSnake(self, dir):
        if dir == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if dir == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if dir == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if dir == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    def move(self, foodPos):
        if self.direction == "RIGHT":
            self.position[0] += 10
        if self.direction == "LEFT":
            self.position[0] -= 10
        if self.direction == "UP":
            self.position[1] -= 10
        if self.direction == "DOWN":
            self.position[1] += 10

        self.body.insert(0, list(self.position))
        if self.position == foodPos:
            return True
        else:
            self.body.pop()
            return False

    def checkCollision(self):
        if self.position[0] > 490 or self.position[0] < 0:
            return True
        elif self.position[1] > 490 or self.position[1] < 0:
            return True

        # For body part in tail
        for bodyPart in self.body[1:]:
            if self.position == bodyPart:
                return True
        return False    
    
    def getHeadPos(self):
        return self.position
    
    def getBody(self):
        return self.body

    def gameOver(self):
        print("Ouch!, Game Over!")
        pygame.quit()
        sys.exit()
