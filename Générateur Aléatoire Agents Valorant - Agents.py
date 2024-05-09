import tkinter as tk
from tkinter import ttk
import random

# Liste des agents par catégorie
agents = {
    "Duellistes": ["Iso", "Jett", "Neon", "Phoenix", "Raze", "Reyna", "Yoru"],
    "Initiateurs": ["Breach", "Fade", "Gekko", "Kayo", "Skye", "Sova"],
    "Sentinelles": ["Chamber", "Cypher", "Deadlock", "Killjoy", "Sage"],
    "Contrôleurs": ["Astra", "Brimstone", "Clove", "Harbor", "Omen", "Viper"]
}

# Agents initiaux
initial_agents = ["Brimstone", "Jett", "Phoenix", "Sage", "Sova"]

class ValorantRandomizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Valorant Agent Randomizer")
        
        # Liste pour conserver les agents sélectionnés
        self.selected_agents = []
        
        # Lecture des agents sélectionnés depuis le fichier
        self.load_selected_agents()
        
        # S'assurer que les agents initiaux sont inclus par défaut
        for agent in initial_agents:
            if agent not in self.selected_agents:
                self.selected_agents.append(agent)
        
        # Création des cadres
        self.selection_frame = ttk.Frame(root)
        self.selection_frame.pack(padx=10, pady=10)
        
        # Création des cases à cocher pour chaque agent
        self.agent_checkbuttons = {}
        for category, agent_list in agents.items():
            ttk.Label(self.selection_frame, text=category).pack()
            for agent in agent_list:
                var = tk.BooleanVar(value=(agent in self.selected_agents))
                checkbutton = tk.Checkbutton(self.selection_frame, text=agent, variable=var, command=lambda a=agent, v=var: self.toggle_agent_selection(a, v))
                checkbutton.pack(anchor="w")
                self.agent_checkbuttons[agent] = (checkbutton, var)  # Ajout des checkbuttons et des variables associées
        
        # Label pour afficher l'agent sélectionné
        self.selected_agent_label = ttk.Label(root, text="", font=("Helvetica", 14))
        self.selected_agent_label.pack(pady=10)
        
        # Bouton pour lancer la sélection aléatoire
        self.select_button = ttk.Button(root, text="Sélectionner aléatoirement", command=self.animate_and_select)
        self.select_button.pack(pady=10)
        
        # Met à jour l'interface graphique
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.minsize(400, 300)  # Taille minimale de la fenêtre
        self.root.mainloop()
    
    def toggle_agent_selection(self, agent, var):
        if var.get():
            self.selected_agents.append(agent)
        else:
            self.selected_agents.remove(agent)
        self.update_selected_agents_file()  # Mettre à jour le fichier
        
    def animate_and_select(self):
        if self.selected_agents:
            self.animate_agents()
            self.root.after(1000, self.select_random_agent)  # Réduit le délai avant la sélection aléatoire
    
    def animate_agents(self):
        # Animation pour faire défiler les agents sélectionnés
        agents_cycle = self.selected_agents[:]
        for _ in range(3):  # Réduit le nombre d'itérations pour l'animation
            random.shuffle(agents_cycle)
            for agent in agents_cycle:
                self.selected_agent_label.config(text=agent)
                self.root.update()
                self.root.after(200)  # Réduit le délai entre chaque changement d'agent
    
    def select_random_agent(self):
        random_agent = random.choice(self.selected_agents)
        self.selected_agent_label.config(text=f"Agent sélectionné aléatoirement : {random_agent}")
    
    def on_close(self):
        # Enregistre les agents sélectionnés dans un fichier ou une base de données pour les retenir
        self.update_selected_agents_file()
        self.root.destroy()
    
    def load_selected_agents(self):
        try:
            with open("selected_agents.txt", "r") as file:
                self.selected_agents = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            # Crée le fichier s'il n'existe pas
            pass
    
    def update_selected_agents_file(self):
        # Met à jour le fichier avec les agents sélectionnés
        with open("selected_agents.txt", "w") as file:
            for agent in self.selected_agents:
                file.write(agent + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ValorantRandomizer(root)
