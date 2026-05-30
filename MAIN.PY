
import pygame
import random
import sys


pygame.init()

# SCREEN SETTINGS
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


clock = pygame.time.Clock()


font = pygame.font.SysFont(None, 40)


snake = [(100, 100)]

snake_direction = (CELL_SIZE, 0)

# FOOD
food_x = random.randrange(0, WIDTH, CELL_SIZE)
food_y = random.randrange(0, HEIGHT, CELL_SIZE)
food = (food_x, food_y)

score = 0



def draw_score():

    score_text = font.render(f"Score: {score}", True, WHITE)

    screen.blit(score_text, (10, 10))


while True:

    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            # MOVEMENT
            if event.key == pygame.K_UP and snake_direction != (0, CELL_SIZE):
                snake_direction = (0, -CELL_SIZE)

            elif event.key == pygame.K_DOWN and snake_direction != (0, -CELL_SIZE):
                snake_direction = (0, CELL_SIZE)

            elif event.key == pygame.K_LEFT and snake_direction != (CELL_SIZE, 0):
                snake_direction = (-CELL_SIZE, 0)

            elif event.key == pygame.K_RIGHT and snake_direction != (-CELL_SIZE, 0):
                snake_direction = (CELL_SIZE, 0)

    
    head_x, head_y = snake[0]

    new_head = (
        head_x + snake_direction[0],
        head_y + snake_direction[1]
    )

    snake.insert(0, new_head)

    
    if new_head == food:

        score += 1

        food_x = random.randrange(0, WIDTH, CELL_SIZE)
        food_y = random.randrange(0, HEIGHT, CELL_SIZE)

        food = (food_x, food_y)

    else:
        snake.pop()

    
    if (
        new_head[0] < 0 or
        new_head[0] >= WIDTH or
        new_head[1] < 0 or
        new_head[1] >= HEIGHT
    ):
        break

    # COLLISION WITH SELF
    if new_head in snake[1:]:
        break

    
    screen.fill(BLACK)

    
    for segment in snake:
        pygame.draw.rect(
            screen,
            GREEN,
            (segment[0], segment[1], CELL_SIZE, CELL_SIZE)
        )

    
    pygame.draw.rect(
        screen,
        RED,
        (food[0], food[1], CELL_SIZE, CELL_SIZE)
    )

    # DRAW SCORE
    draw_score()

    pygame.display.update()

    clock.tick(10)



screen.fill(BLACK)

game_over_text = font.render("GAME OVER", True, RED)

screen.blit(game_over_text, (220, 280))

pygame.display.update()

pygame.time.delay(3000)

pygame.quit()
