import unittest
from unittest.mock import MagicMock, call
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MyAdventures.InsultBot import run
import mcpi.block as block
import unittest
import mcpi.minecraft as minecraft
import time

class TestInsultBot(unittest.TestCase):

    def setUp(self):
        # Mock Minecraft connection
        self.mc = MagicMock()
        
        # Configurar un mètode simulat per `postToChat`
        self.mc.postToChat = MagicMock()
        
        # Mock per a `pollChatPosts`
        self.mc.events.pollChatPosts = MagicMock()

    def test_bot_responses(self):
        # Simular missatges del xat
        mock_messages = [
            MagicMock(message="Hola InsultBot!"),
            MagicMock(message="Un altre missatge"),
        ]
        self.mc.events.pollChatPosts.return_value = mock_messages

        # Executar el bot durant un període curt
        start_time = time.time()
        while time.time() - start_time < 2:  # 2 segons
            run()

        # Comprovar que `postToChat` ha estat cridat almenys una vegada
        self.mc.postToChat.assert_called()

    def test_no_repeated_responses(self):
        # Simular missatges repetits del xat
        mock_messages = [
            MagicMock(message="Hola InsultBot!"),
            MagicMock(message="Hola InsultBot!"),
        ]
        self.mc.events.pollChatPosts.return_value = mock_messages

        # Executar el bot durant un període curt
        start_time = time.time()
        while time.time() - start_time < 2:  # 2 segons
            run()

        # Assegurar que el bot només contesti una vegada al missatge repetit
        self.mc.postToChat.assert_called_once_with("<InsultBot> Tontito")  # Exemple de resposta

if __name__ == "__main__":
    unittest.main()
