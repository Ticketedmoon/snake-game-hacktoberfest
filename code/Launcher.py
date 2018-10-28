import pygame
import time
from Snake import Snake
from Food import Food

class Launcher:
    
    # Initialise global variables for display properties
    def __init__(self):
        self.window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Hacktoberfest Snake Game")
        self.fps = pygame.time.Clock()

        self.score = 0
        self.snake = Snake()
        self.food = Food();

    def start(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.snake.changeDirectionOfSnake('RIGHT') 
                    if event.key == pygame.K_UP:
                        self.snake.changeDirectionOfSnake('UP') 
                    if event.key == pygame.K_DOWN:
                        self.snake.changeDirectionOfSnake('DOWN') 
                    if event.key == pygame.K_LEFT:
                        self.snake.changeDirectionOfSnake('LEFT') 

            foodPos = self.food.spawnFood()
            if (self.snake.move(foodPos)):
                self.score += 1
                self.food.setFoodOnScreen(False)

            self.window.fill(pygame.Color(0, 255, 0))
            for pos in self.snake.getBody():
                pygame.draw.rect(self.window, pygame.Color(255, 0, 0), pygame.Rect(pos[0], pos[1], 10, 10))
                pygame.draw.rect(self.window, pygame.Color(100, 100, 100), pygame.Rect(foodPos[0], foodPos[1], 10, 10))

            if (self.snake.checkCollision() == True):
                self.snake.gameOver()

            pygame.display.set_caption("HacktoberFest Snake Game | Score: " + str(self.score))
            pygame.display.flip()
            self.fps.tick(24)


def main():
    launcher = Launcher()
    launcher.start()
    
if __name__ == "__main__":
    main()
