from machine import Pin
import time

# Configura el pin GPIO 8 como entrada digital
sw1_1 = Pin(8, Pin.IN)

while True:
    # Si el valor leído es 1 (Alto), el interruptor está cerrado
    if sw1_1.value() == 1:
        print("Interruptor cerrado, '1'")
        time.sleep(0.5)
    # Si el valor leído es 0 (Bajo), el interruptor está abierto
    else:
        print("Interruptor abierto, '0'")
        time.sleep(0.5)