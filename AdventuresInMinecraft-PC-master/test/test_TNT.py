import unittest
from unittest.mock import MagicMock, call
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
import MyAdventures.mcpi.block as block
from MyAdventures.Bots.TNTBot import run as tnt_run

class TestTNTBot(unittest.TestCase):

    def setUp(self):
        # Crear una instància simulada de Minecraft
        self.mc = MagicMock()
        self.mc.postToChat = MagicMock()
        self.mc.player.getPos = MagicMock(return_value=MagicMock(x=0, y=0, z=0))
        self.mc.setBlock = MagicMock()

    def test_tnt_placement(self):
        # Executar TNTBot
        tnt_run(self.mc)

        # Comprovar que TNT i foc s'han col·locat correctament
        self.mc.setBlock.assert_any_call(2, 0, 0, block.TNT)
        self.mc.setBlock.assert_any_call(2, 1, 0, block.FIRE)
        self.mc.postToChat.assert_called_with("BOOM!")

if __name__ == "__main__":
    unittest.main()
