import pygame
import random

size = 10
window = 500

pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((window, window))
pygame.display.set_caption("Snake")


class Snake:
    def __init__(self):
        self.x = size*(window//size)/2
        self.y = size*(window//size)/2

        self.alive = True
        self.xdir = 1
        self.ydir = 0
        self.lenght = 5
        self.poshistory = []
        self.pause = 0

    def __del__(self):
        pass


class Food():
    def __init__(self, color=(0, 255, 0)):
        self.color = color
        self.x = size*random.randrange(window//size)
        self.y = size*random.randrange(window//size)

    def newpos(self):
        self.x = size*random.randrange(window//size)
        self.y = size*random.randrange(window//size)


def drawline():
    pygame.draw.line(surface, (255, 255, 255), (0, 0), (0, window), 2)
    pygame.draw.line(surface, (255, 255, 255), (0, 0), (window, 0), 2)
    pygame.draw.line(surface, (255, 255, 255), (0, window-2), (window, window-2), 2)
    pygame.draw.line(surface, (255, 255, 255), (window-2, window), (window-2, 0), 2)

def updatedir(snake):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.KEYDOWN:
                snake.pause = 0
                if event.key == pygame.K_LEFT:
                    snake.xdir = -1
                    snake.ydir = 0
                if event.key == pygame.K_RIGHT:
                    snake.xdir = 1
                    snake.ydir = 0
                if event.key == pygame.K_DOWN:
                    snake.ydir = +1
                    snake.xdir = 0
                if event.key == pygame.K_UP:
                    snake.ydir = -1
                    snake.xdir = 0
                if event.key == pygame.K_p:
                    snake.ydir = 0
                    snake.xdir = 0
                    snake.pause = 1
                if event.key == pygame.K_ESCAPE:
                    return 1
    return 0

def main():
    snake = Snake()
    food = Food()
    while snake.alive:
        surface.fill((0, 0, 0))
        pygame.draw.rect(surface, (255, 0, 0), (snake.x, snake.y, size, size))
        for pos in snake.poshistory:
            pygame.draw.rect(surface, (255, 0, 0), (pos[0], pos[1], size, size))

        pygame.draw.rect(surface, (0, 255, 0), (food.x, food.y, size, size))
        drawline()
        if updatedir(snake):
            return 0

        if snake.pause == 0:
            snake.poshistory.insert(0, [snake.x, snake.y])

        if len(snake.poshistory) > snake.lenght:
            snake.poshistory.pop()
        snake.x = snake.x + size*snake.xdir
        snake.y = snake.y + size*snake.ydir

        if snake.x > window-size:
            snake.alive = False
        if snake.y > window-size:
            snake.alive = False
        if snake.x < 0:
            snake.alive = False
        if snake.y < 0:
            snake.alive = False

        if (snake.x, snake.y) == (food.x, food.y):
            food.newpos()
            snake.lenght += 1

        if [snake.x, snake.y] in snake.poshistory:
            snake.alive = False

        if not snake.alive:
            snake.__del__()
            snake = Snake()
        clock.tick(10)
        pygame.display.update()
        if __name__ == "__main__":
            print(snake.poshistory)
    
    

main()
pygame.quit()