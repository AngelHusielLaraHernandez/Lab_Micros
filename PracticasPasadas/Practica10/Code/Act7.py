
# Importa las clases Pin e I2C del módulo machine
from machine import Pin, I2C
# Importa la librería time para retardos
import time


# Inicializa el bus I2C en los pines 9 (SCL) y 8 (SDA) a 100kHz
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)
# Escanea los dispositivos conectados al bus I2C
addr = i2c.scan()


# Si se encontró algún dispositivo, imprime su dirección
if addr:
    print("address is : " + str(hex(addr[0])))


# Realiza 100 lecturas del sensor TMP102
for i in range(100):
    data = []
    # Lee 2 bytes de información desde la dirección 0x48 (TMP102)
    data = i2c.readfrom(0x48, 2)
    # Convierte el arreglo de bytes a un número entero (Big Endian)
    intdata = int.from_bytes(data, 'big')
    # El sensor es de 12 bits justificados a la izquierda, se desplazan 4 bits
    tmp = intdata >> 4
    # Calcula la temperatura en °C
    print(f"Temperatura TMP102: {tmp * 0.0625} °C")
    # Espera 1 segundo antes de la siguiente lectura
    time.sleep(1)