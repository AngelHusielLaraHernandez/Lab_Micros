import pcf8574
from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(9), sda=Pin(8)) # [cite: 818]
# Inicializa el expansor PCF8574 en la dirección 0x39 [cite: 818]
pcf = pcf8574.PCF8574(i2c, 0x39) 

while True: # [cite: 819]
    # 0x3F en binario es 111111. Esto pone el puerto P0 en ALTO (1).
    pcf.port = 0x3F # [cite: 820]
    print("Puerto:", pcf.port) # [cite: 821]
    time.sleep(0.8) # [cite: 822]

    # 0x3E en binario es 111110. Esto pone el puerto P0 en BAJO (0).
    pcf.port = 0x3E # [cite: 823]
    print("Puerto:", pcf.port) # [cite: 823]
    time.sleep(0.8) # [cite: 824]