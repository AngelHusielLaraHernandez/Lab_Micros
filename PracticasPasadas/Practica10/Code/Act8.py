
# Importa la librería utime para retardos
import utime
# Importa las clases Pin e I2C del módulo machine
from machine import Pin, I2C
# Importa la librería ahtx0 para el sensor de temperatura y humedad
import ahtx0


# Inicializa el bus I2C en los pines 8 (SDA) y 9 (SCL) a 400kHz
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
# Crea el objeto sensor para leer el AHT10
sensor = ahtx0.AHT10(i2c)


# Bucle infinito para mostrar temperatura y humedad
while True:
    # Imprime la temperatura en grados centígrados (2 decimales)
    print("\nTemperature: %0.2f C" % sensor.temperature)
    # Imprime la humedad relativa (2 decimales)
    print("Humidity: %0.2f %%" % sensor.relative_humidity)
    # Espera 5 segundos antes de la siguiente lectura
    utime.sleep(5)