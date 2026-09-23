import re 
from datetime import datetime

def champ_obligatoire(valeur): 
    return valeur.strip() != ""

def valider_nom(nom): 
    return nom.strip() != "" and not any(c.isdigit() for c in nom)

def valider_courriel(courriel): 
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, courriel) is not None

def valider_motdepasse(password):
    return len(password) >= 8

def valider_date(date_texte): 
    try: 
        datetime.strptime(date_texte, "%Y-%m-%d")
        return True 
    except ValueError: 
        return False

def valider_nombre(valeur): 
    try: 
        int(valeur)
        return True
    except ValueError: 
        return False
if __name__ == "__main__":

     print(valider_nom("Dupont"))
     print(valider_nom("Dupont123"))

     print(valider_courriel("test@test.com"))
     print(valider_courriel("test.com"))

     print(valider_motdepasse("12345678"))
     print(valider_motdepasse("1234"))

     print(valider_date("2026-09-23"))
     print(valider_date("23/09/2026"))

     print(valider_nombre("100"))
     print(valider_nombre("abc"))

