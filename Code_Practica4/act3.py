from machine import Pin
import time

# Configuración de pines
LED = Pin(0, Pin.OUT)       # GPIO 0 como salida (LED)

# GPIO 12 como entrada con resistencia PULL_DOWN interna activada
# Por defecto leerá 0. Al presionarlo (si está conectado a 3.3V) leerá 1.
push_S2 = Pin(12, Pin.IN, Pin.PULL_DOWN) 

while True:
    # Evalúa el estado del botón S2
    if push_S2.value() == 0:
        LED.value(0)        # Apaga el LED
        print("Push Button S2 en espera; lectura: '0'")
        time.sleep(0.5)
    else:
        LED.value(1)        # Enciende el LED
        print("Push Button S2 presionado; lectura: '1'")
        time.sleep(0.5)