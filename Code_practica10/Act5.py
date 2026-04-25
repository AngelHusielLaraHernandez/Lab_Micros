from machine import I2C, Pin # [cite: 1019]
import time # [cite: 1019]
from esp8266_i2c_lcd import I2cLcd # [cite: 1020]

# La dirección por defecto de estos módulos suele ser 0x27
DEFAULT_I2C_ADDR = 0x27 # [cite: 1021]

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000) # [cite: 1022]
# Configura el objeto LCD: I2C, Dirección, Filas, Columnas
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16) # [cite: 1023]

# Imprime con salto de línea (\n)
lcd.putstr("UNAM!\nFI") # [cite: 1024]
time.sleep(3) # [cite: 1025]

lcd.clear() # Borra toda la pantalla [cite: 1026]

# Mueve el cursor a la columna 3, fila 0 (primera línea)
lcd.move_to(3, 0) # [cite: 1027]
lcd.putstr("Laboratorio") # [cite: 1028]

# Mueve el cursor a la columna 0, fila 1 (segunda línea)
lcd.move_to(0, 1) # [cite: 1029]
lcd.putstr("* MICROS*") # [cite: 1030]

time.sleep(1) # [cite: 1031]