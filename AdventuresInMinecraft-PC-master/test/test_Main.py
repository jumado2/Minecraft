import unittest
import sys
import os

# Afegir el directori base del projecte al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Llistat de fitxers de test
TEST_MODULES = [
    "testsInd.test_TNT",
    "testsInd.test_Oracle",
    "testsInd.test_Insult"
    #,"test_AchievObs"
    
]

#def main():
loader = unittest.TestLoader()
suite = unittest.TestSuite()

for module in TEST_MODULES:
    suite.addTests(loader.loadTestsFromName(module))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

if result.wasSuccessful():
    print("\nTots els tests han passat correctament! 🚀")
else:
    print("\nAlguns tests han fallat. Revisa els errors.")

#if __name__ == "__main__":
#    main()
