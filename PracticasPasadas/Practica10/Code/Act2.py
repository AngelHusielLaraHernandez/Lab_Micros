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

while True: # [cite: 819]
    pcf.port = 0x3F
    # Pone todos los pines en alto (0x3F = 111111)
    print("Puerto:", pcf.port)
    # Espera 0.8 segundos
    time.sleep(0.8)

    pcf.port = 0x3E
    # Pone el pin P0 en bajo (0x3E = 111110)
    print("Puerto:", pcf.port)
    # Espera 0.8 segundos
    time.sleep(0.8)