import machine # Importa la librería de hardware
import utime   # Importa la librería de tiempo

# Configura el pin GPIO 5 (LED ROJO según tabla) como salida
LED_ROJO = machine.Pin(5, machine.Pin.OUT)

while True:                 # Bucle infinito
    LED_ROJO.value(1)       # Enciende el LED conectado al GPIO 5
    utime.sleep_ms(300)     # Retardo a conveniencia (300 ms)
    LED_ROJO.value(0)       # Apaga el LED conectado al GPIO 5
    utime.sleep_ms(300)     # Retardo a conveniencia (300 ms)