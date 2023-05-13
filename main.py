from machine import Pin, Timer
import utime
import time
import math
 
 
trigger_pin = Pin(27, Pin.OUT)
echo_pin = Pin(26, Pin.IN)

led_red = Pin(17, Pin.OUT)
led_green = Pin(16, Pin.OUT)

limite = 50
valeur = 1

# Initialisation de la broche pour l'afficheur 7 segments (des dizaines = celui à gauche)
pins_dizaine = [
    Pin(0, Pin.OUT), #top 
    Pin(1, Pin.OUT), #top right 
    Pin(2, Pin.OUT), #bot right
    Pin(3, Pin.OUT), #bot
    Pin(4, Pin.OUT), #bot left
    Pin(5, Pin.OUT), #top left
    Pin(6, Pin.OUT), #middle (malheureusement pas dans le circuit ...)
    Pin(7, Pin.OUT)  #Dot Point 
]

# Initialisation de la broche pour l'afficheur 7 segments (des Unités = celui à droite)
pins_unite = [
    Pin(9, Pin.OUT),  #top 
    Pin(10, Pin.OUT), #top right
    Pin(11, Pin.OUT), #bot right
    Pin(12, Pin.OUT), #bot
    Pin(13, Pin.OUT), #bot left
    Pin(14, Pin.OUT), #top left
    Pin(15, Pin.OUT) #middle
]

#common anode 7 segment
chars_unite = [
    [0, 0, 0, 0, 0, 0, 1], #0
    [1, 0, 0, 1, 1, 1, 1], #1
    [0, 0, 1, 0, 0, 1, 0], #2
    [0, 0, 0, 0, 1, 1, 0], #3
    [1, 0, 0, 1, 1, 0, 0], #4
    [0, 1, 0, 0, 1, 0, 0], #5
    [0, 1, 0, 0, 0, 0, 0], #6
    [0, 0, 0, 1, 1, 1, 1], #7
    [0, 0, 0, 0, 0, 0, 0], #8
    [0, 0, 0, 0, 1, 0, 0] #9
]

chars_dizaine = [
    [0, 0, 0, 0, 0, 0, 1, 1], #0
    [1, 0, 0, 1, 1, 1, 1, 1], #1
    [0, 0, 1, 0, 0, 1, 1, 1], #2
    [0, 0, 0, 0, 1, 1, 1, 1], #3
    [1, 0, 0, 1, 1, 0, 1, 1], #4
    [0, 1, 0, 0, 1, 0, 1, 1], #5
    [0, 1, 0, 0, 0, 0, 1, 1], #6
    [0, 0, 0, 1, 1, 1, 1, 1], #7
    [0, 0, 0, 0, 0, 0, 1, 1], #8
    [0, 0, 0, 0, 1, 0, 1, 1] #9
]



def count(display, number):
    if display == pins_dizaine:
        for i in range(len(pins_dizaine)):
            pins_dizaine[i].value(chars_dizaine[number][i])
    if display == pins_unite:
        for j in range(len(pins_unite)):
            pins_unite[j].value(chars_unite[number][j])

def clear():
    for i in pins_dizaine:
        i.value(1)
    for j in pins_unite:
        j.value(1)

def check(timer1):
    global valeur
    valeur = max(min(valeur, 999), 0)
    if valeur < 10:
        count(pins_unite, valeur)
    elif valeur >= 10 and valeur < 100:
        count(pins_dizaine, valeur//10)
        count(pins_unite, valeur%10)
    elif valeur >= 100:
        count(pins_dizaine, valeur//100)
        pins_dizaine[6].value(0)
        count(pins_unite, (valeur%100)//10)


def init_timer():
    timer1 = Timer()
    timer1.init(freq=100.0,mode=Timer.PERIODIC,callback=check)

def init():
    init_timer()

def main_loop():
    global valeur
    trigger_pin.low()
    utime.sleep_us(2)
    trigger_pin.high()
    utime.sleep_us(5)
    trigger_pin.low()
    pulse_start = 0
    pulse_end = 0
    while echo_pin.value()==0:
        pulse_start = time.ticks_us()
    while echo_pin.value()==1:
        pulse_end = time.ticks_us()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17165 / 1000000
    distance = int(round(distance, 0))

    print("Distance: %.2f cm" % distance)
    valeur = distance
    if distance <= limite:
        led_red.value(0)
        led_green.value(1)
    else:
        led_red.value(1)
        led_green.value(0)
    utime.sleep_ms(500)
    return distance


init()
while True:
    main_loop()
    clear()