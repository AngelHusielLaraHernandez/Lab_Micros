import max7219
from machine import Pin, SPI
from time import sleep

num_display = 4
spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
cs_pin = Pin(6, Pin.OUT)
display = max7219.Matrix8x8(spi, cs_pin, num_display)

# Lista con los mensajes requeridos por el manual
mensajes = ["UNAM", "FI", "*", "*", "2026", "26 - 2", "*", "*", "*", "*", "PEPE"]

while True:
    for msg in mensajes:
        display.fill(0)               # Limpia la pantalla antes de cada mensaje
        display.text(msg, 0, 0, 1)    # Posiciona el texto desde el píxel (0,0)
        display.show()                # Ejecuta la impresión
        sleep(2)                      # Retardo de 2 segundos entre mensajes