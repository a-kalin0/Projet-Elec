import serial
import tkinter as tk
<<<<<<< HEAD
import time

limite_valeur = 50
# Initialise la communication série avec le port COM4 à une vitesse de 9600 bauds
=======

limite_valeur = 50
# Initialise la communication avec le port 
>>>>>>> 693965c88e9c0189e2ec6422cb88d71a247b6bfb
ser = serial.Serial('COM12', 9600)

# Fonction pour lire une ligne de données depuis le port série
def read_serial():
    line = ser.readline().decode().strip()
    return line

<<<<<<< HEAD
# Fonction pour envoyer la nouvelle valeur limite au Pico
def envoi_limite(limite_valeur):
    x = str(limite_valeur)
    y = f"{x}\r\n"
    ser.write(y.encode())
    time.sleep(0.1)

# Fonction pour changer la valeur limite
def nouvelle_limite():
    global limite_entree, limite_valeur, label_limite
    limite_valeur = limite_entree.get()
    label_limite.config(text="Limite : " + str(limite_valeur) + " cm")
    envoi_limite(limite_valeur)

# Fonction pour mettre à jour l'interface graphique avec les nouvelles données
def update_interface(distance):
    global label_distance, label_led, limite_valeur

    # Met à jour le label avec la distance lue
    label_distance.config(text="Distance : " + distance + " cm")

    # Met à jour le label avec l'alerte
    led_etat = "Pas d'alerte"
    if int(distance) > int(limite_valeur):
        led_etat = "Alerte"
    label_led.config(text=led_etat)

=======
>>>>>>> 693965c88e9c0189e2ec6422cb88d71a247b6bfb
# Création de l'interface graphique
root = tk.Tk()

# Création d'un label pour afficher les données
label_distance = tk.Label(root)
label_distance.pack()

# Création d'un label pour afficher l'alerte
label_led = tk.Label(root)
<<<<<<< HEAD
label_led.pack()

# Création d'un label pour afficher la valeur limite
label_limite = tk.Label(root, text="Limite : " + str(limite_valeur) + " cm")
label_limite.pack()

# Création d'un champ d'entrée de texte pour la valeur limite
limite_entree = tk.Entry(root)
limite_entree.pack()

# Création d'un bouton pour changer la valeur limite
limite_boutton = tk.Button(root, text="Changer limite", command=nouvelle_limite)
limite_boutton.pack()
=======
label_led.pack() 
>>>>>>> 693965c88e9c0189e2ec6422cb88d71a247b6bfb

# Boucle principale de l'application
while True:
    # Lit la distance mesurée du pico
    distance = read_serial()

<<<<<<< HEAD
    # Met à jour l'interface graphique
    update_interface(distance)
=======
    # Met à jour le label avec la distance lue
    label_distance.config(text="Distance : " + distance + " cm")

        # Met à jour le label avec l'alerte
    led_etat = "Pas d'alerte"
    if int(distance) > limite_valeur:
        led_etat = "Alerte"
    label_led.config(text=led_etat)
>>>>>>> 693965c88e9c0189e2ec6422cb88d71a247b6bfb

    # Actualise l'interface graphique
    root.update()