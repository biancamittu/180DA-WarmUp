import paho.mqtt.client as mqtt
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    client.subscribe("game/choice")

def on_message(client, userdata, message):
    # Process the message and determine the result
    player_choice = message.payload.decode()
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)

    # Publish the result back to the players
    client.publish("game/result", result)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io")

client.loop_forever()