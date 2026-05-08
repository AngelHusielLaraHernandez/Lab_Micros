
# Importa la librería para manejar el expansor PCF8574
import pcf8574
# Importa las clases I2C y Pin del módulo machine
from machine import I2C, Pin
# Importa la librería time para retardos
import time


# Inicializa el bus I2C en los pines 9 (SCL) y 8 (SDA)
i2c = I2C(0, scl=Pin(9), sda=Pin(8))
# Crea el objeto pcf para controlar el expansor en la dirección 0x21
pcf = pcf8574.PCF8574(i2c, 0x21)


# Lista con los valores binarios para encender cada pin del puerto (P0 a P5)
secuencia = [
    0b000001, # Enciende P0
    0b000010, # Enciende P1
    0b000100, # Enciende P2
    0b001000, # Enciende P3
    0b010000, # Enciende P4
    0b100000  # Enciende P5
]


# Bucle infinito para recorrer la secuencia
while True:
    for valor in secuencia:
        # Envía el valor de la secuencia al puerto del expansor
        pcf.port = valor
        time.sleep(0.5)      # Velocidad de la secuencia