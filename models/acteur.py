from models.personne import Personne

class Acteur(Personne): 

    def __init__(self, nom, prenom, sexe,
                 nom_personnage,
                 debut_emploi, 
                 fin_emploi,
                 cachet): 

        super().__init__(nom, prenom, sexe)

        self.nom_personnage = nom_personnage
        self.debut_emploi = debut_emploi
        self.fin_emploi = fin_emploi
        self.cachet = cachet