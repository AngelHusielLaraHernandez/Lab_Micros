from machine import Pin
import time

# Configura el GPIO 8 como una entrada digital (Pin.IN)
sw1_1 = Pin(8, Pin.IN)

while True:
    # Lee el valor del interruptor
    if sw1_1.value() == 1:
        # Si el valor es 1, el interruptor está enviando voltaje (cerrado)
        print("Interruptor cerrado, '1'")
        time.sleep(0.5) # Retardo de medio segundo
    else:
        # Si el valor es 0, el interruptor no envía voltaje (abierto)
        print("Interruptor abierto, '0'")
        time.sleep(0.5) # Retardo de medio segundo