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
    "Ets del madrid"
]

while(1):
    chat_messages = mc.events.pollChatPosts()
    for message in chat_messages:
 