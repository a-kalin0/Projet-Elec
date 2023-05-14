mport serial
import tkinter as tk

# Initialise la communication avec le port 
ser = serial.Serial('COM12', 9600)

# Fonction pour lire une ligne de données depuis le port série
def read_serial():
    line = ser.readline().decode().strip()
    return line

# Création de l'interface graphique
root = tk.Tk()

# Création d'un label pour afficher les données
label_distance = tk.Label(root)
label_distance.pack()

# Boucle principale de l'application
while True:
    # Lit la distance mesurée du pico
    distance = read_serial()

    # Met à jour le label avec la distance lue
    label_distance.config(text="Distance : " + distance + " cm")

    # Actualise l'interface graphique
    root.update()