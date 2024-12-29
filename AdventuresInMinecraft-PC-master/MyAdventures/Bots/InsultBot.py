import sys
import os
import time
import OracleBot

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
 # Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import random
# Connect to the Minecraft game
mc = minecraft.Minecraft.create()
mc.postToChat("InsultBot està actiu!")

# Llista d'insults
insults = [
    "Tontito",
    "Burro",
    "Jugador del lol",
    "Avui no és el teu dia, oi?",
    "Empanat"
]

# Conjunt per emmagatzemar missatges ja gestionats
previous_messages = set()

# Bucle principal
while True:
    # Obtenir missatges nous del xat
    chat_messages = mc.events.pollChatPosts()

    for message in chat_messages:
        # Només processar missatges nous
        if message.message == "oraclebot mode 2": setattr(OracleBot, "mode", 2)
        elif message.message == "oraclebot mode 1": setattr(OracleBot, "mode", 1)
        elif message.message not in previous_messages:
            insult = random.choice(insults)  # Escollir un insult aleatori
            mc.postToChat(f"<InsultBot> {insult}")  # Enviar l'insult al xat
            previous_messages.add(message.message)  # Afegir el missatge al conjunt gestionat

    # Esperar un segon abans de verificar nous missatges
    time.sleep(1)


