from models.personne import Personne

class Client (Personne):

    def __init__(self, nom, prenom, sexe,  date_inscription, courriel, password):


        super().__init__(nom, prenom, sexe)
        self.date_inscription = date_inscription
        self.courriel = courriel
        self.password= password