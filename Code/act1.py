import machine # Importa la librería para acceder al hardware de la Raspberry Pi Pico
import utime   # Importa la librería para manejar retardos de tiempo (delays)

# Configura el pin GPIO 0 como una salida digital y lo asigna a la variable 'LED'
LED = machine.Pin(0, machine.Pin.OUT)

while True:                 # Bucle infinito
    LED.value(1)            # Enciende el LED (pone el pin GPIO 0 en nivel alto '1')
    utime.sleep_ms(500)     # Espera 500 milisegundos (medio segundo)
    LED.value(0)            # Apaga el LED (pone el pin GPIO 0 en nivel bajo '0')
    utime.sleep_ms(500)     # Espera 500 milisegundos