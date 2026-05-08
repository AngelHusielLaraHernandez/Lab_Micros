
# Importa la librería para manejar el expansor PCF8574
import pcf8574
# Importa las clases I2C y Pin del módulo machine
from machine import I2C, Pin
# Importa la librería time para retardos
import time


# Inicializa el bus I2C en los pines 9 (SCL) y 8 (SDA)
i2c = I2C(0, scl=Pin(9), sda=Pin(8)) # [cite: 958]
# Crea el objeto pcf para controlar el expansor en la dirección 0x21
pcf = pcf8574.PCF8574(i2c, 0x21) # [cite: 958]


# Define el valor lógico para encender (ON) y apagar (OFF)
ON = 0
OFF = 1


# Estado inicial del puerto (configura los pines de salida)
pcf.port = 0x37


# Mensaje de inicio
print("Iniciamos")


# Bucle infinito para monitorear el botón y controlar el LED
while True:
    # Configura el pin 6 como entrada (alta impedancia)
    pcf.pin(6, 1)
    # Si el botón conectado a P6 está presionado (nivel bajo)
    if pcf.pin(6) == 0:
        # Enciende el LED conectado a P0
        pcf.pin(0, ON)
        print("Bajo")
    else:
        # Apaga el LED conectado a P0
        pcf.pin(0, OFF)
        print("Alto")
    # Espera breve para no saturar la lectura
    time.sleep(0.1)