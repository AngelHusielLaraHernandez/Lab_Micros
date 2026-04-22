import time
from neopixel import Neopixel

# Configuración en el GPIO 4 para la tira de 8 LEDs Neopixel
pixels = Neopixel(8, 0, 4, "GRB")

# Definimos una lista con 3 colores distintos: Rojo, Verde y Azul
colores = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

while True:
    for color in colores:
        # Bucle de llenado: Enciende los LEDs uno a uno
        for i in range(8):
            pixels.set_pixel(i, color)
            pixels.show()
            time.sleep(0.5) # Retardo de 100ms entre cada LED para efecto de barrido
            
        # Bucle de apagado (limpieza) para notar el cambio de color
        for i in range(8):
            pixels.set_pixel(8 - i - 1, (0, 0, 0))
            pixels.show()
            time.sleep(0.5)