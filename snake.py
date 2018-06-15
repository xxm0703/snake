import pygame
import random

pygame.init()

wide = 800
high = 600
snake_x = wide / 2  # To be at the center of the screen
snake_y = high / 2
apple_x = random.randint(10, wide - 10)  # Some space before border
apple_y = random.randint(20, high - 10)
wall_x = 0
wall_y = 0

RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
YELLOW = [255, 255, 0]
D_BLUE = [52, 63, 197]
D_GREEN = [0, 128, 0]
T_BLACK = [0, 0, 0, 50]

slither = pygame.image.load('photo.png')


def message(msg, color=BLACK, size=25, line=1, msg_x=wide / 2, msg_y=high / 3):
    font = pygame.font.SysFont(None, size, True)
    text = font.render(msg, True, color)
    screen.blit(text, [msg_x - len(msg) * 6, msg_y + line * 25])


def eyes(direction, x, y):
    if direction is "UP":
        return [[x + 2, y + 2], [x + 6, y + 2]]
    elif direction is "LEFT":
        return [[x + 2, y + 6], [x + 2, y + 2]]
    elif direction is "DOWN":
        return [[x + 6, y + 6], [x + 2, y + 6]]
    elif direction is "RIGHT":
        return [[x + 6, y + 2], [x + 6, y + 6]]


def bump_into_wall(head, walls):
    for x, y in walls:
        if x % 2:  # horizontal
            if abs(x + 20 - head[0]) < 20 and abs(head[1] - y) < 5:
                return True
        elif abs(y + 20 - head[1]) < 20 and abs(head[0] - x) < 5:
            return True


screen = pygame.display.set_mode((wide, high))
pygame.display.set_caption("Snake!")
clock = pygame.time.Clock()
apple_sound = pygame.mixer.music.load('sound.mp3')
PAUSE = False
PLAY = True
in_game = False
change_x = 0
change_y = -10
state = "UP"
screen.fill(WHITE)
while PLAY:
    pos_list = []
    wall_list = []
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
                if event.key == pygame.K_p:
                    message('PAUSED', BLACK, 35, 2)
                    pygame.display.update()
                    PAUSE = True
                elif event.key == pygame.K_LEFT and state != "RIGHT":
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
        while PAUSE:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        PAUSE = False
                if event.type == pygame.QUIT:
                    PLAY = False
                    in_game = False
                    PAUSE = False

        snake_x += change_x
        snake_y += change_y
        pos_list.insert(0, (snake_x, snake_y))
        pos_list.pop(-1)

        if snake_x < 0 or snake_y < 0 or snake_x > wide or snake_y > high or bump_into_wall(pos_list[0],
                                                                                            wall_list) or pos_list.count(
            pos_list[0]) == 2:
            message("Game Over!", RED, 35)
            pygame.display.update()
            pygame.time.delay(2000)
            in_game = False

        elif -10 < apple_x - snake_x < 10 and -10 < apple_y - snake_y < 10:
            pygame.mixer.music.play()
            apple_x = random.randint(10, wide - 10)
            apple_y = random.randint(20, high - 10)
            wall_x = random.randint(10, wide - 10)
            wall_y = random.randint(20, high - 10)
            wall_list.append((wall_x, wall_y))
            pos_list.append((snake_x - change_x, snake_y - change_y))
            apple_count += 1
            if apple_count == 10:
                message("You WIN!", GREEN, 40)
                pygame.display.update()
                pygame.time.delay(3000)
                in_game = False

        screen.fill(D_BLUE)

        message("P for pause", T_BLACK, 15, 1, 70, -20)
        pygame.draw.rect(screen, RED, [apple_x, apple_y, 9, 9])
        for (wall_x, wall_y) in wall_list:
            if wall_x % 2:
                pygame.draw.line(screen, YELLOW, (wall_x, wall_y), (wall_x + 40, wall_y), 10)
            else:
                pygame.draw.line(screen, YELLOW, (wall_x, wall_y), (wall_x, wall_y + 40), 10)
        for cord in pos_list:
            if cord is not pos_list[0]:
                pygame.draw.rect(screen, D_GREEN, [cord[0], cord[1], 10, 10])
            else:
                pygame.draw.rect(screen, GREEN, [cord[0], cord[1], 10, 10])
                for eye_cord in eyes(state, cord[0], cord[1]):
                    pygame.draw.rect(screen, BLACK, [eye_cord[0], eye_cord[1], 2, 2])
        pygame.draw.rect(screen, BLACK, [0, 0, 800, 600], 2)
        pygame.display.update()
        clock.tick(10)
    screen.fill(WHITE)

pygame.quit()
quit()
