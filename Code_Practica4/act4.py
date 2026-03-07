from machine import Pin
import time

# Configura GPIO 11 como entrada con resistencia PULL_UP interna
# El botón lee '1' cuando está suelto y '0' cuando se presiona hacia tierra.
S1 = Pin(11, Pin.IN, Pin.PULL_UP)

# Configura pines de salida
LED4 = Pin(4, Pin.OUT)
LED5 = Pin(5, Pin.OUT)
LED6 = Pin(6, Pin.OUT)
LED7 = Pin(7, Pin.OUT)
ZUMBADOR = Pin(22, Pin.OUT)

while True:
    if S1.value() == 1:
        # Push button liberado -> Apaga todas las salidas
        LED4.value(0)
        LED5.value(0)
        LED6.value(0)
        LED7.value(0)
        ZUMBADOR.value(0)
        print("Push button S1 liberado, '1'")
    else:
        # Push button presionado -> Enciende todas las salidas
        LED4.value(1)
        LED5.value(1)
        LED6.value(1)
        LED7.value(1)
        ZUMBADOR.value(1)
        print("Push button S1 presionado, '0'")
        
    time.sleep(0.2) # Retardo para evitar lecturas saturadas en la consola