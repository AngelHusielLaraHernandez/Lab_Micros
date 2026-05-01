
# Importa las clases I2C y Pin del módulo machine
from machine import I2C, Pin
# Importa la librería time para retardos
import time
# Importa la clase I2cLcd para controlar la pantalla LCD por I2C
from esp8266_i2c_lcd import I2cLcd


# Dirección I2C por defecto del LCD
DEFAULT_I2C_ADDR = 0x27

# Inicializa el bus I2C en los pines 9 (SCL) y 8 (SDA) a 200kHz
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)

# Crea el objeto lcd para controlar la pantalla (2 filas, 16 columnas)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)


# Muestra el texto "UNAM!" en la primera línea y "FI" en la segunda
lcd.putstr("UNAM!\nFI")
# Espera 3 segundos
time.sleep(3)


# Limpia la pantalla LCD
lcd.clear()


# Mueve el cursor a la columna 3, fila 0 y escribe "Laboratorio"
lcd.move_to(3, 0)
lcd.putstr("Laboratorio")


# Mueve el cursor a la columna 0, fila 1 y escribe "* MICROS*"
lcd.move_to(0, 1)
lcd.putstr("* MICROS*")


# Espera 1 segundo antes de finalizar
time.sleep(1)