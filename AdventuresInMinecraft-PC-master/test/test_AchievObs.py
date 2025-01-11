import unittest
from unittest.mock import MagicMock
import MyAdventures.mcpi.block as block
from MyAdventures.Bots.AchievObs import run, logro_threshold, hit_count

class TestAchievementBot(unittest.TestCase):

    def setUp(self):
        # Crear una instància simulada de Minecraft
        self.mc = MagicMock()
        self.mc.postToChat = MagicMock()

    def test_block_hit_tracking(self):
        # Simular un esdeveniment de bloc colpejat
        mock_event = MagicMock(pos=MagicMock(), block=block.STONE.id)
        run(self.mc, mock_event)

        # Comprovar que s'ha actualitzat el recompte
        self.assertEqual(hit_count[block.STONE.id], 1)

    def test_achievement_message(self):
        # Simular que s'arriba al llindar
        global hit_count
        hit_count[block.STONE.id] = logro_threshold - 1
        mock_event = MagicMock(pos=MagicMock(), block=block.STONE.id)
        run(self.mc, mock_event)

        # Comprovar que s'ha publicat el missatge de logro
        self.mc.postToChat.assert_called_with(
            f"Felicitats! Has colpejat {logro_threshold} blocs del tipus {block.STONE.id}. 🎉"
        )

if __name__ == "__main__":
    unittest.main()
