import dht
from machine import Pin
import time

# Configura el sensor DHT11 en el GPIO 21
Sensor = dht.DHT11(Pin(21))

while True:
    # Instruye al sensor para que recolecte los datos del ambiente
    Sensor.measure()
    
    # Extrae la temperatura y la humedad ya procesadas de la memoria interna
    temp = Sensor.temperature()
    hum = Sensor.humidity()
    
    # Imprime los resultados
    print(f"Temperatura: {temp}°C Humedad: {hum}%")
    
    # Retardo indispensable de 2 segundos. El DHT11 no soporta lecturas muy rápidas continuas.
    time.sleep(2)