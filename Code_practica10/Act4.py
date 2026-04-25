import pcf8574
from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(9), sda=Pin(8)) # [cite: 958]
pcf = pcf8574.PCF8574(i2c, 0x39) # [cite: 958]

ON = 0  # [cite: 959]
OFF = 1 # [cite: 960]

# Estado inicial del puerto
pcf.port = 0x37 # [cite: 961]

print("Iniciamos") # [cite: 963]

while True: # [cite: 964]
    pcf.pin(6, 1) # Asegura que P6 funcione como entrada (alta impedancia) [cite: 962]
    
    # Lee el estado del botón en el Pin P6
    if pcf.pin(6) == 0: # [cite: 965]
        pcf.pin(0, ON)  # Acción: Enciende el LED en P0 [cite: 967]
        print("Bajo") # [cite: 971]
    else: # [cite: 966]
        pcf.pin(0, OFF) # Acción: Apaga el LED en P0 [cite: 970]
        print("Alto") # [cite: 968]
        
    time.sleep(0.1) # Breve retardo para no saturar la lectura