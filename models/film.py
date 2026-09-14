class Film: 

    def __init__(self, nom, duree, description):
        self.nom = nom
        self.duree = duree
        self.description = description 


        self.categories = []
        self.acteurs = []
    def ajouter_categorie(self, categorie):
        self.categories.append(categorie)


    def ajouter_acteur(self, acteur):
            self.acteurs.append(acteur)