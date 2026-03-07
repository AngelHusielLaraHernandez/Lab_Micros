from machine import Pin
import time

# Configura GPIO 8 como entrada (Interruptor)
sw1_1 = Pin(8, Pin.IN)
# Configura GPIO 0 como salida (LED Verde)
led_verde = Pin(0, Pin.OUT)

while True:
    if sw1_1.value() == 1:
        led_verde.value(1) # Enciende el LED
        print("Interruptor cerrado, '1'")
        time.sleep(0.5)
    else:
        led_verde.value(0) # Apaga el LED
        print("Interruptor abierto, '0'")
        time.sleep(0.5)