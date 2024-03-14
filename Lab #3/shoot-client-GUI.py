# Import necessary libraries
import pygame
import paho.mqtt.client as mqtt
import sys

# Initialize PyGame
pygame.init()

# Set up the screen
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Rock-Paper-Scissors")

# Initialize MQTT client
client = mqtt.Client()
client.connect("mqtt.eclipseprojects.io")

# Font setup
font = pygame.font.Font(None, 36)

# Function to display text on screen
def displayText(text, position):

    textSurface = font.render(text, True, (0, 0, 0))
    screen.blit(textSurface, position)

# Game loop
def main():

    global client
    running = True

    while running:

        # Fill the screen with white
        screen.fill((255, 255, 255))
        
        # Display text
        displayText("Please make a selection", (screenWidth // 2 - 150, 50))
        
        # Draw buttons for rock, paper, scissors
        rockButton = pygame.draw.rect(screen, (0, 255, 0), (100, 200, 150, 50))
        paperButton = pygame.draw.rect(screen, (0, 255, 0), (300, 200, 150, 50))
        scissorsButton = pygame.draw.rect(screen, (0, 255, 0), (500, 200, 150, 50))
        
        displayText("Rock", (130, 210))
        displayText("Paper", (330, 210))
        displayText("Scissors", (520, 210))
        
        pygame.display.update()
        
        # Process events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                x, y = pygame.mouse.get_pos()

                if rockButton.collidepoint(x, y):
                    client.publish("game/playerOne", "rock")

                elif paperButton.collidepoint(x, y):
                    client.publish("game/playerOne", "paper")

                elif scissorsButton.collidepoint(x, y):
                    client.publish("game/playerOne", "scissors")

        # Receive result from server
        client.subscribe("game/result")
        client.onMessage = onMessage
        client.loop()

# MQTT callback to receive result
def onMessage(client, userdata, message):

    result = message.payload.decode()
    displayText(result, (screenWidth // 2 - 100, 400))
    pygame.display.update()

if __name__ == "__main__":
    main()

# Quit PyGame
pygame.quit()
sys.exit()