import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
 # Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import random
# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Interact with the Minecraft world
mc.postToChat("Hello Minecraft World")
pos = mc.player.getTilePos()
mc.setBlock(pos.x+3, pos.y, pos.z, block.STONE.id)


insults = [
    "Tontito",
    "Burro",
    "jugador del lol",
    "Avui no és el teu dia, oi?",
    "empanat"
]

while(1):
    usuari = mc.getPlayerEntityIds()
    mc.postToChat("<InsultBot>" + random.choice(insults))
    
    chat_messages = mc.events.pollChatPosts()
    for message in chat_messages:
        mc.postToChat("<InsultBot>" + random.choice(insults))






"""

# Funció principal del bot
def insult_bot():
    previous_messages = set()  # Per evitar repetir els mateixos insults pel mateix missatge
    while True:
        # Recuperar els missatges del xat
        chat_messages = mc.events.pollChatPosts()

        for message in chat_messages:
            if message.message not in previous_messages:  # Només respondre a missatges nous
                insult = random.choice(insults)  # Escollir un insult aleatori
                mc.postToChat(insult)  # Enviar l'insult al xat
                previous_messages.add(message.message)  # Marcar el missatge com gestionat

        time.sleep(1)  # Esperar un segon abans de verificar nous missatges
        
"""