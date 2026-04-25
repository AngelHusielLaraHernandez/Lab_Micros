import pcf8574
from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(9), sda=Pin(8))
pcf = pcf8574.PCF8574(i2c, 0x39)

# Representación binaria de la Tabla 10-1 (P0 al P5) [cite: 903, 904, 905, 906]
secuencia = [
    0b000001, # Enciende P0 [cite: 907, 911]
    0b000010, # Enciende P1 [cite: 912, 915]
    0b000100, # Enciende P2 [cite: 917, 919]
    0b001000, # Enciende P3 [cite: 922, 924]
    0b010000, # Enciende P4 [cite: 927, 930]
    0b100000  # Enciende P5 [cite: 932, 936]
]

while True:
    for valor in secuencia:
        pcf.port = valor     # Envía el byte completo al expansor
        time.sleep(0.5)      # Velocidad de la secuencia