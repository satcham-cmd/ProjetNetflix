from models.personne import Personne

class Employe(Personne):

    def __init__(self, nom, prenom, sexe, date_embauche):
        super().__init__(nom, prenom, sexe)
        self.date_embauche = date_embauche