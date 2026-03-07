from machine import Pin
import time

# Configuración de pines
sw1_1 = Pin(8, Pin.IN)      # GPIO 8 como entrada (Interruptor)
LED = Pin(0, Pin.OUT)       # GPIO 0 como salida (LED Verde)

while True:
    # Evalúa el estado del interruptor
    if sw1_1.value() == 1:
        LED.value(1)        # Enciende el LED asignando un nivel alto (1)
        print("Interruptor cerrado, '1'")
        time.sleep(0.5)
    else:
        LED.value(0)        # Apaga el LED asignando un nivel bajo (0)
        print("Interruptor abierto, '0'")
        time.sleep(0.5)