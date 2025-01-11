import unittest
from unittest.mock import MagicMock, call
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
import mcpi.block as block
from MyAdventures.Bot.TNTBot.py import run  

class TestTNTBot(unittest.TestCase):

    def setUp(self):
        # Connectar amb Minecraft
        self.mc = minecraft.Minecraft.create()
        self.start_pos = self.mc.player.getTilePos()

    def test_tnt_placement(self):
        # Executar el bot
        run(self.mc)

        # Verificar si el TNT s'ha col·locat correctament
        tnt_pos = self.start_pos.clone()
        tnt_pos.x += 2
        tnt_block = self.mc.getBlock(tnt_pos.x, tnt_pos.y, tnt_pos.z)

        self.assertEqual(tnt_block, block.TNT.id, "El bloc TNT no s'ha col·locat correctament.")

    def test_fire_placement(self):
        # Esperar uns segons perquè el foc es col·loqui
        time.sleep(2)
        fire_pos = self.start_pos.clone()
        fire_pos.x += 2
        fire_pos.y += 1
        fire_block = self.mc.getBlock(fire_pos.x, fire_pos.y, fire_pos.z)

        self.assertEqual(fire_block, block.FIRE.id, "El bloc de foc no s'ha col·locat correctament.")

if __name__ == "__main__":
    unittest.main()
