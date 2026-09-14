class Personne:

    def __init__(self, nom, prenom, sexe): 
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe

    def afficher_infos(self):
            print("Nom :", self.nom)
            print("Prénom :", self.prenom)
            print("Sexe :", self.sexe)