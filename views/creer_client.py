import tkinter as tk
from tkinter import messagebox

def enregistrer():
    nom = nom_entry.get()
    prenom = prenom_entry.get()
    courriel = courriel_entry.get()
    motdepasse = motdepasse_entry.get()

    if nom == "" or prenom == "" or courriel == "" or motdepasse == "":
        messagebox.showerror(
            "Erreur",
            "Tous les champs sont obligatoires"
        )
        return

    if len(motdepasse) < 8:
        messagebox.showerror(
            "Erreur",
            "Le mot de passe doit contenir au moins 8 caractères"
        )
        return
    with open("clients.txt", "a") as fichier:
        fichier.write(f"{prenom} {nom}\n")

    print("Client ajouté")

    messagebox.showinfo(
        "Succès",
        f"Client enregistré : {prenom} {nom}"
    )

fenetre = tk.Tk()
fenetre.title("Créer un client")
fenetre.geometry("400x300")

tk.Label(fenetre, text="Nom").pack()
nom_entry = tk.Entry(fenetre)
nom_entry.pack()

tk.Label(fenetre, text="Prénom").pack()
prenom_entry = tk.Entry(fenetre)
prenom_entry.pack()

tk.Label(fenetre, text="Courriel").pack()
courriel_entry = tk.Entry(fenetre)
courriel_entry.pack()

tk.Label(fenetre, text="Mot de passe").pack()
motdepasse_entry = tk.Entry(fenetre, show="*")
motdepasse_entry.pack()

tk.Button(
fenetre,
text="Enregistrer",
command=enregistrer
).pack(pady=10)

fenetre.mainloop()