from models.film import Film
from models.categorie import Categorie
from models.acteur import Acteur

film1 = Film(
"Avatar",
162,
"Films avec beaucoup d'action"
)
categorie1 = Categorie(
    "Action",
    "Films avec beaucoup d'action"
)

acteur1 = Acteur(
    "Parker",
    "Peter",
    "M",
    "Spider-Man",
    "2020-01-01",
    "2020-12-31",
    "500000"
)

film1.ajouter_categorie(categorie1)
film1.ajouter_acteur(acteur1)

print(film1.nom)
print(film1.duree)
print(film1.description)

print(film1.categories[0].nom)
print(film1.acteurs[0].nom_personnage)


