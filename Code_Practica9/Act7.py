import dht
from machine import Pin
import time

# Configura el DHT11 en el GPIO 21
Sensor = dht.DHT11(Pin(21))

while True:
    try:
        # Pide la trama de datos de 40 bits
        Sensor.measure()
        temp = Sensor.temperature()
        hum = Sensor.humidity()
        
        print(f"Temperatura: {temp}°C Humedad: {hum}%")
        
    except OSError:
        # Evita que el programa colapse si hay un error de lectura por ruido
        print("Fallo de sincronización, reintentando...")
        
    # Retardo mínimo de 2 segundos recomendado por el fabricante
    time.sleep(2)