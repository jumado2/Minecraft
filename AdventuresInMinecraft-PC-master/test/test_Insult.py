import unittest
from unittest.mock import MagicMock
from MyAdventures.Bots.InsultBotTest import run
import MyAdventures.mcpi.minecraft as minecraft

class TestInsultBot(unittest.TestCase):

    def setUp(self):
        # Crear una instància simulada de Minecraft
        self.mc = MagicMock()
        self.mc.postToChat = MagicMock()

    def test_insult_response(self):
        # Simular un missatge d'entrada
        test_message = "Hola InsultBot!"

        # Executar el bot amb el missatge simulat
        run(self.mc, test_message)

        # Comprovar que es va enviar un insult al xat
        self.mc.postToChat.assert_called()
        insult_message = self.mc.postToChat.call_args[0][0]
        self.assertTrue("<InsultBot>" in insult_message, "El bot no ha enviat un insult al xat.")

if __name__ == "__main__":
    unittest.main()
