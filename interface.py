import serial
import tkinter as tk

limite_valeur = 50
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

# Création d'un label pour afficher l'alerte
label_led = tk.Label(root)
label_led.pack() 

# Boucle principale de l'application
while True:
    # Lit la distance mesurée du pico
    distance = read_serial()

    # Met à jour le label avec la distance lue
    label_distance.config(text="Distance : " + distance + " cm")

        # Met à jour le label avec l'alerte
    led_etat = "Pas d'alerte"
    if int(distance) > limite_valeur:
        led_etat = "Alerte"
    label_led.config(text=led_etat)

    # Actualise l'interface graphique
    root.update()