import time
from neopixel import Neopixel

# Configuración: 8 LEDs, estado 0, pin físico GPIO 4, formato de color GRB
pixels = Neopixel(8, 0, 4, "GRB")
brightness = 0.1 # Limita el brillo al 10% para proteger el puerto USB

# Tuplas de color (Rojo, Verde, Azul)
red = (255, 0, 0)
black = (0, 0, 0)

while True:
    pixels.set_pixel(0, red)   # Enciende el primer LED en rojo
    pixels.show()              # Ejecuta la actualización física
    time.sleep(1)              
    
    pixels.set_pixel(0, black) # Apaga el primer LED
    pixels.show()              
    time.sleep(1)