import tkinter as tk
from random import randint

def generer_nombre_agents():
    nb_agents = int(entree_agents.get())
    nombre_genere = randint(0, nb_agents)
    resultat.config(text=f"Le nombre généré est : {nombre_genere}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Générateur aléatoire d'agents VALORANT")

# Cadre pour la question et la zone de texte
cadre_question = tk.Frame(fenetre)
cadre_question.pack(pady=10)

question = tk.Label(cadre_question, text="Combien d'agents VALORANT avez-vous ? : ")
question.pack(side=tk.LEFT)

entree_agents = tk.Entry(cadre_question)
entree_agents.pack(side=tk.LEFT)

# Bouton pour relancer la génération
bouton_generer = tk.Button(fenetre, text="Générer", command=generer_nombre_agents)
bouton_generer.pack()

# Affichage du résultat
resultat = tk.Label(fenetre, text="")
resultat.pack(pady=10)

# Lancement de la boucle principale
fenetre.mainloop()