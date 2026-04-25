import utime # [cite: 1211]
from machine import Pin, I2C # [cite: 1212]
import ahtx0 # [cite: 1213]

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000) # [cite: 1214]
# Instancia la clase de la librería asociándole el bus I2C
sensor = ahtx0.AHT10(i2c) # [cite: 1214]

while True: # [cite: 1215]
    # Imprime temperatura en grados centígrados (2 decimales)
    print("\nTemperature: %0.2f C" % sensor.temperature) # [cite: 1216]
    
    # Imprime humedad relativa (2 decimales)
    print("Humidity: %0.2f %%" % sensor.relative_humidity) # [cite: 1216]
    
    utime.sleep(5) # Retardo para evitar auto-calentamiento del microchip # [cite: 1216]