import max7219
from machine import Pin, SPI
from time import sleep

# Indica cuántos módulos de 8x8 conforman la pantalla física (el manual indica un módulo de 4 en línea)
num_display = 4 

# Configura el bus SPI0 
spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))

# El pin Chip Select (CS) para la matriz es el GPIO6
cs_pin = Pin(6, Pin.OUT)

# Crea el objeto de la matriz
display = max7219.Matrix8x8(spi, cs_pin, num_display)

# Limpia completamente la pantalla (apaga todos los LEDs)
display.fill(0)

# Dibuja el texto '0' en la coordenada (x=0, y=1). El '1' final indica el color de encendido.
display.text('0', 0, 1, 1)

# Actualiza la pantalla para reflejar los cambios
display.show()

# Espera 3 segundos
sleep(3)