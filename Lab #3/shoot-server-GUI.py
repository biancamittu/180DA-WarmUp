import paho.mqtt.client as mqtt
import random

# Function to determine winner
def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
         (player1_choice == 'paper' and player2_choice == 'rock') or \
         (player1_choice == 'scissors' and player2_choice == 'paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    client.subscribe("game/player1")
    client.subscribe("game/player2")

def on_message(client, userdata, message):
    global player1_choice, player2_choice
    if message.topic == "game/player1":
        player1_choice = message.payload.decode()
    elif message.topic == "game/player2":
        player2_choice = message.payload.decode()
    if player1_choice and player2_choice:
        result = determine_winner(player1_choice, player2_choice)
        client.publish("game/result", result)

# Initialize MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("mqtt.eclipseprojects.io")

# Initialize player choices
player1_choice = None
player2_choice = None

# Start MQTT loop
client.loop_forever()