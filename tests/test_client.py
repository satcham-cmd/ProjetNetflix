import unittest

class TestClient(unittest.TestCase):

    def test_nom_non_vide (self): 
        nom = "Maldonado"
        self.assertNotEqual(nom, "")

    def test_prenom_non_vide(self):
        prenom = "Sacha"
        self.assertNotEqual(prenom, "")

    def test_motdepasse_valide(self): 
        motdepasse = "12345678"
        self.assertGreaterEqual(len(motdepasse), 8)

if __name__ == "__main__":
    unittest.main()
