from machine import Pin
import time

# Configura GPIO 0 como salida
LED = Pin(0, Pin.OUT)
# Configura GPIO 12 como entrada habilitando la resistencia PULL_DOWN interna
push_S2 = Pin(12, Pin.IN, Pin.PULL_DOWN)

while True:
    # Si la lectura es 0, el botón está suelto (por el pull-down)
    if push_S2.value() == 0:
        LED.value(0) # Apaga el LED
        print("Push Button S2 en espera; lectura: '0'")
        time.sleep(0.5)
    # Si la lectura es 1, el botón fue presionado (cierra circuito a 3.3V)
    else:
        LED.value(1) # Enciende el LED
        print("Push Button S2 presionado; lectura: '1'")
        time.sleep(0.5)