import paho.mqtt.client as mqtt

def get_user_choice():
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    client.subscribe("game/result")

def on_message(client, userdata, message):
    print("Result received: " + message.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io")

player1_choice = get_user_choice()
client.publish("game/choice", player1_choice)

player2_choice = get_user_choice()
client.publish("game/choice", player2_choice)

client.loop_forever()