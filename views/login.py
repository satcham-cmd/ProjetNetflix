import tkinter as tk 
from tkinter import messagebox


def connexion(): 
    code = entry_code.get()
    password = entry_password.get()

    if code == "admin" and password == "12345678":
        messagebox.showinfo("Succès", "Connexion réussie")
    else: 
        messagebox.showerror("Erreur", "Code utilisateur ou mot de passe invalide")

        
fenetre = tk.Tk ()
fenetre.title ("Connexion Netflix")
fenetre.geometry ("300x200")

label_code = tk.Label (fenetre, text="Code utilisateur")
label_code.pack()

entry_code = tk.Entry(fenetre)
entry_code.pack()

label_password = tk.Label(fenetre, text="Mot de passe")
label_password.pack()

entry_password = tk.Entry(fenetre, show="*")
entry_password.pack()

bouton_connexion = tk.Button(fenetre, text="Connexion", 
                             command=connexion
)
bouton_connexion.pack(pady=10)

fenetre.mainloop()