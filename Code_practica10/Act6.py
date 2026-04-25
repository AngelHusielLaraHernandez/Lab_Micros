from machine import Pin, I2C # [cite: 1078]
from ssd1306 import SSD1306_I2C # [cite: 1079]

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000) # [cite: 1080]
# Pantalla OLED de 128x64 píxeles
oled = SSD1306_I2C(128, 64, i2c) # [cite: 1081]

devices = i2c.scan() # [cite: 1082]
if devices: # [cite: 1083]
    for d in devices: # [cite: 1084]
        print("I2C Address: " + hex(d)) # [cite: 1086]

oled.fill(0) # Llena la pantalla de "negro" (la limpia) [cite: 1087]

# Escribe texto: (Mensaje, coord_X, coord_Y, color=1)
oled.text("Microcomputadoras", 1, 6, 1) # [cite: 1088]
oled.text("Practica I2C", 3, 30, 1) # [cite: 1089]

oled.show() # Envía el buffer de memoria a la pantalla física [cite: 1090]
print("UNAM FI") # [cite: 1091]