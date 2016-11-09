import pygame
import random, os
pygame.init()

wide = 800
high = 600
snake_x = wide/2  # To be at the center of the screen
snake_y = high/2
apple_x = random.randint(10, wide - 10)  # Some space before border
apple_y = random.randint(10, high - 10)
print(apple_x, apple_y)

RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
YELLOW = [255, 255, 0]
D_BLUE = [52, 63, 197]

slither = pygame.image.load('photo.png')

def message(msg, color=BLACK, size=25, line=1):
    font = pygame.font.SysFont(None, size, True)
    text = font.render(msg, True, color)
    screen.blit(text, [wide/2 - len(msg)*6, high/3 + line * 25])

screen = pygame.display.set_mode((wide, high))
pygame.display.set_caption("Snake!")
clock = pygame.time.Clock()

PLAY = True
in_game = False
change_x = 0
change_y = -10
state = "UP"
screen.fill(WHITE)
while PLAY:
    pos_list = []
    pos_list.insert(0, (snake_x, snake_y))
    apple_count = 0
    screen.blit(slither, [100, 0])
    message("This is my 'Snake' game. I hope you like it.", BLACK, 30)
    message("Press any key to continue...", BLACK, 30, 2)
    pygame.display.update()
    pygame.time.delay(70)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            snake_x = wide / 2
            snake_y = high / 2
            in_game = True
        if event.type == pygame.QUIT:
            PLAY = False
            break
    while in_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PLAY = False
                in_game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and state != "RIGHT":
                    change_x = -10
                    change_y = 0
                    state = "LEFT"
                elif event.key == pygame.K_RIGHT and state != "LEFT":
                    change_x = 10
                    change_y = 0
                    state = "RIGHT"
                elif event.key == pygame.K_UP and state != "DOWN":
                    change_y = -10
                    change_x = 0
                    state = "UP"
                elif event.key == pygame.K_DOWN and state != "UP":
                    change_y = 10
                    change_x = 0
                    state = "DOWN"

        snake_x += change_x
        snake_y += change_y
        pos_list.insert(0, (snake_x, snake_y))
        pos_list.pop(-1)

        if snake_x < 0 or snake_y < 0 or snake_x > wide or snake_y > high or pos_list.count(pos_list[0]) == 2:
            message("Game Over!", RED, 35)
            pygame.display.update()
            pygame.time.delay(2000)
            in_game = False

        elif -10 < apple_x - snake_x < 10 and -10 < apple_y - snake_y < 10:
            apple_x = random.randint(10, wide - 10)
            apple_y = random.randint(10, high - 10)
            pos_list.append((snake_x - change_x, snake_y - change_y))
            apple_count += 1
            if apple_count == 10:
                message("You WIN!", GREEN, 40)
                pygame.display.update()
                pygame.time.delay(3000)
                in_game = False

        screen.fill(D_BLUE)

        pygame.draw.rect(screen, RED, [apple_x, apple_y, 9, 9])
        for cord in pos_list:
            pygame.draw.rect(screen, GREEN, [cord[0], cord[1], 10, 10])
            print(cord[0], cord[1])
        pygame.draw.rect(screen, BLACK, [0, 0, 800, 600], 2)
        pygame.display.update()
        clock.tick(10)

pygame.quit()
quit()
