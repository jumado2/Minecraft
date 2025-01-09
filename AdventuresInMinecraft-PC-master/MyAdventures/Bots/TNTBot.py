import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
 # Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import random

def run(m):
    # Connect to the Minecraft game
    mc = m
    # Obtenir la posició del jugador
    pos = mc.player.getTilePos()

    # Col·locar un bloc de TNT davant del jugador
    mc.setBlock(pos.x + 2, pos.y, pos.z, block.TNT)
    mc.postToChat("Col·locant TNT...")

    time.sleep(2)  

    mc.setBlock(pos.x + 2, pos.y+1, pos.z, block.FIRE)
    mc.postToChat("BOOM!")

