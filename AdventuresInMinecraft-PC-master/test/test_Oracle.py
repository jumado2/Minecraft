import unittest
from unittest.mock import MagicMock
from MyAdventures.Bots.OracleBot import run as oracle_run, existent, mode
import MyAdventures.mcpi.minecraft as minecraft

class TestOracleBot(unittest.TestCase):

    def setUp(self):
        # Crear una instància simulada de Minecraft
        self.mc = MagicMock()
        self.mc.postToChat = MagicMock()

    def test_oracle_existent(self):
        # Comprovar que una pregunta coneguda existeix
        self.assertTrue(existent("Com es fa una taula de crafteig?"))

        # Comprovar que una pregunta desconeguda no existeix
        self.assertFalse(existent("Pregunta desconeguda"))

    def test_oracle_response(self):
        # Configurar una entrada coneguda
        input_message = "Com es fa una taula de crafteig?"
        oracle_run(self.mc, input_message)

        # Comprovar que es respon correctament
        expected_response = (
            "OracleBot: Necessites 4 blocs de fusta processada. Col\u00b7loca'ls en un quadrat 2x2 al teu inventari."
            if mode == 1
            else "OracleBot: De deb\u00f2 no saps aix\u00f2? Nom\u00e9s agafa 4 blocs de fusta processada i posa'ls en un quadrat 2x2. Ni que fos f\u00edsica qu\u00e0ntica!"
        )
        self.mc.postToChat.assert_called_with(expected_response)

if __name__ == "__main__":
    unittest.main()
