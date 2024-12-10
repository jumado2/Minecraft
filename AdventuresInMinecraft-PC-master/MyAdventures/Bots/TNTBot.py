import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
 # Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import random
# Connect to the Minecraft game
mc = minecraft.Minecraft.create()
mc.postToChat("TNTBot està actiu! Escriviu 'tnt' al xat per activar-me.")


# Bucle principal
while True:
    # Recuperar missatges nous del xat
    chat_messages = mc.events.pollChatPosts()

    for message in chat_messages:
        if message.message.lower() == "tnt":
            # Obtenir la posició del jugador
            pos = mc.player.getTilePos()

            # Col·locar un bloc de TNT davant del jugador
            mc.setBlock(pos.x + 2, pos.y, pos.z, block.TNT)
            mc.postToChat("Col·locant TNT...")

            time.sleep(2)  

            mc.setBlock(pos.x + 2, pos.y+1, pos.z, block.FIRE)
            mc.postToChat("BOOM!")

