import time
from neopixel import Neopixel

# Inicializa la tira Neopixel.
# Parámetros: 8 LEDs, estado de la máquina (0), pin físico (GPIO 4), formato "GRB"
pixels = Neopixel(8, 0, 4, "GRB")
brightness = 0.1 # Establece el brillo al 10% para no saturar la vista

# Definición de colores usando tuplas RGB (Rojo, Verde, Azul) de 0 a 255
red = (255, 0, 0)
black = (0, 0, 0) # El negro equivale a LED apagado

while True:
    pixels.set_pixel(0, red)   # Carga el color rojo al LED en la posición 0
    pixels.show()              # Ejecuta la instrucción y muestra el color físicamente
    time.sleep(1)              # Espera 1 segundo
    
    pixels.set_pixel(0, black) # Carga el color negro al LED en la posición 0
    pixels.show()              # Actualiza la tira
    time.sleep(1)              # Espera 1 segundo