
# Importa las clases Pin e I2C del módulo machine
from machine import Pin, I2C


# Configura el pin 8 como SDA (Serial Data Line)
sda = Pin(8)
# Configura el pin 9 como SCL (Serial Clock Line)
scl = Pin(9)
# Inicializa el bus I2C número 0 con los pines definidos
i2c = I2C(0, scl=scl, sda=sda)


# Escanea los dispositivos conectados al bus I2C
devices = i2c.scan()

if devices:
    # Si se encontraron dispositivos I2C
    for d in devices:
        # Imprime la dirección de cada dispositivo en formato hexadecimal
        print("Dispositivo I2C en dirección:", hex(d))
else:
    # Si no se encontró ningún dispositivo I2C
    print("No se encontraron dispositivos")