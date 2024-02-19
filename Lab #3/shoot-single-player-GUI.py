import pygame
import random
import time
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rock-Paper-Scissors")

# Load images and scale them
rock_img = pygame.image.load("/Users/biancamittu/Documents/GitHub/180DA-WarmUp/Lab #3/rock.png")
paper_img = pygame.image.load("/Users/biancamittu/Documents/GitHub/180DA-WarmUp/Lab #3/paper.png")
scissors_img = pygame.image.load("/Users/biancamittu/Documents/GitHub/180DA-WarmUp/Lab #3/scissors.png")

# Scale images to fit the screen
img_height = 150
rock_img = pygame.transform.scale(rock_img, (img_height, img_height))
paper_img = pygame.transform.scale(paper_img, (img_height, img_height))
scissors_img = pygame.transform.scale(scissors_img, (img_height, img_height))

# Define the choices
choices = ["rock", "paper", "scissors"]

# Game loop
running = True
clock = pygame.time.Clock()
round_duration = 5  # Increase the round duration to 5 seconds

while running:
    screen.fill((255, 255, 255))  # Fill the screen with white
    
    # Display text
    font = pygame.font.Font(None, 36)
    text = font.render("Please make a selection", True, (0, 0, 0))
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, 50))
    
    # Center the images horizontally and vertically
    img_width = rock_img.get_width()
    img_spacing = 50
    total_width = 3 * img_width + 2 * img_spacing
    start_x = (screen_width - total_width) // 2
    y = (screen_height - img_height) // 2
    screen.blit(rock_img, (start_x, y))
    screen.blit(paper_img, (start_x + img_width + img_spacing, y))
    screen.blit(scissors_img, (start_x + 2 * (img_width + img_spacing), y))
    
    pygame.display.update()
    
    # Wait for player input
    player_choice = None
    while player_choice is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game if the window is closed
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, _ = pygame.mouse.get_pos()
                if start_x <= x <= start_x + img_width:
                    player_choice = "rock"
                elif start_x + img_width + img_spacing <= x <= start_x + 2 * (img_width + img_spacing):
                    player_choice = "paper"
                elif start_x + 2 * (img_width + img_spacing) <= x <= start_x + 3 * (img_width + img_spacing):
                    player_choice = "scissors"
    
    if not running:
        break
    
    # Computer randomly chooses
    computer_choice = random.choice(choices)
    
    # Determine the winner
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    # Display the player's and computer's choices and the game outcome
    player_text = font.render("Player chose: " + player_choice, True, (0, 0, 0))
    computer_text = font.render("Computer chose: " + computer_choice, True, (0, 0, 0))
    result_text = font.render(result, True, (0, 0, 0))
    
    screen.blit(player_text, (screen_width // 2 - player_text.get_width() // 2, y + img_height + 20))
    screen.blit(computer_text, (screen_width // 2 - computer_text.get_width() // 2, y + img_height + 60))
    screen.blit(result_text, (screen_width // 2 - result_text.get_width() // 2, y + img_height + 100))
    
    pygame.display.update()
    
    # Pause for a moment before clearing the screen
    time.sleep(2)
    
# Quit Pygame
pygame.quit()
sys.exit()