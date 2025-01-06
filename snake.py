import pygame # type: ignore
import random
import os
pygame.init()

pygame.mixer.init()



# Colors
white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)

# Display Window
Window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")
pygame.display.update()

# Background Image
img = pygame.image.load("ground.png")
img = pygame.transform.scale(img, (600, 600)).convert_alpha()

# Time
clock = pygame.time.Clock()
fps = 30

# Functions
font = pygame.font.SysFont(None, 25)
def screen_score(text, color, x, y):
        screen_text = font.render(text, True, color)
        Window.blit(screen_text, [x, y])

def plot_snake(Window, color, list, size):
        for x, y in list:
            pygame.draw.rect(Window, color, [x, y, size, size])

# Home Screen
def Welcome():
    exit_game = False
    while not exit_game:
        Window.fill(green)
        screen_score("Welcome to SNAX", black, 220, 275)
        screen_score("Press Space Bar to play", black, 200, 300)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()

        pygame.display.update()
        clock.tick(fps)

# Game Begins
def game_loop():
    # Game Specific Variables
    exit_game = False
    game_over = False
    snake_x = 5
    snake_y = 50
    snake_size = 10
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    food_x = random.randint(0, 600)
    food_y = random.randint(0, 600)
    score = 0
    
    
    snake_list = []
    snake_length = 0
    while not exit_game:
        if game_over:
            Window.fill(green)
            screen_score("Game Over!", black, 250, 275)
            screen_score("Return to restart the game..", black, 200, 300)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Welcome()
            
        else:
            head = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        velocity_y = +init_velocity
                        velocity_x = 0
            snake_x+=velocity_x
            snake_y+=velocity_y

            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6: 
                score+=1
                food_x = random.randint(0, 600)
                food_y = random.randint(0, 600)
                snake_length+=1
            Window.fill(green)
            Window.blit(img, (0, 0))
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if snake_x>600 or snake_x<0 or snake_y>600 or snake_y<0:
                game_over = True

            if head in snake_list[:-1]:
                game_over = True
            
            screen_score(f"score: {score}", black, 5, 5)
            # pygame.draw.rect(Window, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(Window, black, snake_list, snake_size)
            if len(snake_list)>snake_length:
                del snake_list[0]
            pygame.draw.rect(Window, red, [food_x, food_y, snake_size, snake_size])
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

Welcome()