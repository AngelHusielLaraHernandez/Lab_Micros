import select
import sys
import time
from machine import Pin

# Configura el LED interno de la Raspberry Pi Pico 
led = Pin(25, Pin.OUT) 
poll_obj = select.poll()
poll_obj.register(sys.stdin, 1)

print("Control de LED (GPIO25). Envíe '1' para ON, '0' para OFF")

while True:
    if poll_obj.poll(0):
        # Lee el carácter ingresado 
        ch = sys.stdin.read(1) 
        if ch == '1':
            led.value(1) # Enciende el LED 
            print("Acción: GPIO25 = ON") [cite: 351]
        elif ch == '0':
            led.value(0) # Apaga el LED 
            print("Acción: GPIO25 = OFF") [cite: 351]
    time.sleep(0.1)