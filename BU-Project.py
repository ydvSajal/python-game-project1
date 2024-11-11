import pygame
import time
import random

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

questions = [
    {"question": "What does CPU stand for?", "answer": "central processing unit"},
    {"question": "What does GPU stand for?", "answer": "graphics processing unit"},
    {"question": "What does RAM stand for?", "answer": "random access memory"},
    {"question": "What does PSU stand for?", "answer": "power supply unit"}
]

for question in questions:
    answer = input(question["question"] + " ")
    if answer.lower() == question["answer"]:
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

print("You got " + str(score) + " questions correct!")

# If the score is greater than or equal to 1, run the Snake game
if score >= 1:
    # Initialize Pygame
    pygame.init()

    # Colors
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    # Screen dimensions
    width = 600
    height = 400

    # Create the display
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game')

    # Clock
    clock = pygame.time.Clock()

    # Snake settings
    snake_block = 10
    snake_speed = 15

    # Font
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)

    def display_score(score):
        value = score_font.render("Score: " + str(score), True, black)
        screen.blit(value, [0, 0])

    def draw_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

    def display_message(msg, color):
        mesg = font_style.render(msg, True, color)
        screen.blit(mesg, [width / 6, height / 3])

    def game_loop():
        game_over = False
        game_close = False

        x1 = width / 2
        y1 = height / 2

        x1_change = 0
        y1_change = 0

        snake_list = []
        length_of_snake = 1

        # Generate initial food position
        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close:
                screen.fill(blue)
                display_message("You Lost! Press C-Continue or Q-Quit", red)
                display_score(length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            game_loop()  # Restart the game loop

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            # Check for boundary
            if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
                game_close = True

            x1 += x1_change
            y1 += y1_change
            screen.fill(blue)
            pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            draw_snake(snake_block, snake_list)
            display_score(length_of_snake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
                length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()

    game_loop()