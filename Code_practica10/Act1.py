from machine import Pin, I2C

# Configuración del bus I2C0 en los pines 8 (SDA) y 9 (SCL)
sda = Pin(8)
scl = Pin(9)
i2c = I2C(0, scl=scl, sda=sda) # [cite: 743]

# Escaneo de dispositivos conectados al bus I2C
devices = i2c.scan() # [cite: 744]

if devices: # [cite: 745]
    for d in devices: # [cite: 746]
        # Imprime la dirección en formato hexadecimal (ej. 0x39, 0x27)
        print("Dispositivo I2C en dirección:", hex(d)) # [cite: 747]
else:
    print("No se encontraron dispositivos")