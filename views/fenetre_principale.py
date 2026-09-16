import subprocess
import tkinter as tk 
from tkinter import messagebox

with open("clients.txt", "r") as fichier:
    clients = fichier.readlines()
def creer_client():
    subprocess.Popen(
        ["python3", "views/creer_client.py"]
    )
def supprimer_client():
    selection = liste_clients.curselection()

    if not selection: 
        messagebox.showwarning(
            "Attention",
            "Sélectionnez un client"
        )
        return

    index = selection[0]

    confirmation = messagebox.askyesno(
        "Confirmation",
        "Voulez-vous supprimer ce client ?"
    )

    if confirmation: 
        liste_clients.delete(index)

        del clients[index]

        with open("clients.txt", "w") as fichier:
            fichier.writelines(clients)

def modifier_client(): 
    selection = liste_clients.curselection()

    if not selection: 
        messagebox.showwarning(
             "Attention",
            "Sélectionnez un client" 
        )
        return

    index = selection[0]

    fenetre_modif = tk.Toplevel(fenetre)
    fenetre_modif.title("Modifier client")
    fenetre_modif.geometry("300x150")

    tk.Label(
        fenetre_modif, 
        text="Nouveau nom"
    ).pack(pady=5)

    entree_nom = tk.Entry(fenetre_modif)
    entree_nom.pack(pady=5)

    def enregistrer_modification():
        nouveau_nom = entree_nom.get()

        if nouveau_nom == "":
            messagebox.showerror(
                "Erreur",
                "Le nom est obligatoire"
            )
            return
        liste_clients.delete(index)
        liste_clients.insert(index, nouveau_nom)

        clients[index] = nouveau_nom + "\n"

        with open("clients.txt", "w") as fichier:
            fichier.writelines (clients)

        messagebox.showinfo(
            "Succès",
            "Client modifié"
            )

        fenetre_modif.destroy()

    tk.Button(
        fenetre_modif,
        text="Enregistrer",
        command=enregistrer_modification
        ).pack(pady=10)


            
fenetre = tk.Tk()
fenetre.title("Netflix")
fenetre.geometry("600x400")

label_clients = tk.Label(
fenetre,
text="Liste des clients"
)
label_clients.pack()

liste_clients = tk.Listbox(
fenetre,
width=40,
height=8
)
liste_clients.pack()

for client in clients:
    liste_clients.insert(tk.END, client.strip())

label_films = tk.Label(
fenetre,
text="Liste des films"
)
label_films.pack()

liste_films = tk.Listbox(
fenetre,
width=40,
height=8
)
liste_films.pack()

liste_films.insert(tk.END, "Avatar")
liste_films.insert(tk.END, "Titanic")

btn_creer = tk.Button(
fenetre,
text="Créer", 
command=creer_client
)
btn_creer.pack(side="left", padx=10)

btn_modifier = tk.Button(
fenetre,
text="Modifier", 
command=modifier_client
)
btn_modifier.pack(side="left", padx=10)

btn_supprimer = tk.Button(
fenetre,
text="Supprimer", 
command=supprimer_client
)
btn_supprimer.pack(side="left", padx=10)

fenetre.mainloop()