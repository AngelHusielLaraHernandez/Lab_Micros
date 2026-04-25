from machine import Pin, I2C # [cite: 1146]
import time # [cite: 1147]

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=100000) # [cite: 1148]
addr = i2c.scan() # [cite: 1149]

if addr:
    print("address is : " + str(hex(addr[0]))) # [cite: 1150]

for i in range(100): # [cite: 1151]
    data= []
    # Lee 2 bytes de información desde la dirección 0x48 (dirección del TMP102)
    data = i2c.readfrom(0x48, 2) # [cite: 1153]
    
    # Convierte el arreglo de bytes a un número entero grande (Big Endian)
    intdata = int.from_bytes(data, 'big') # [cite: 1154]
    
    # El sensor es de 12 bits justificados a la izquierda, por lo que se deben desplazar 4 bits
    tmp = intdata >> 4 # [cite: 1155]
    
    # La resolución del TMP102 es de 0.0625°C por cada unidad de lectura
    print(f"Temperatura TMP102: {tmp * 0.0625} °C") # [cite: 1156]
    
    time.sleep(1) # [cite: 1157]