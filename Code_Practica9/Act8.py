import dht
from machine import Pin
import time

Sensor = dht.DHT11(Pin(21))
led = Pin(20, Pin.OUT)       # Salida para LED
buzzer = Pin(17, Pin.OUT)    # Salida para Zumbador

# Valor que deberás ajustar basado en lo que te dio tu sensor en reposo (por ejemplo 25°C)
Temp_ref = 25 

while True:
    try:
        Sensor.measure()
        Temp_actual = Sensor.temperature()
        
        print(f"Temperatura Actual: {Temp_actual}°C | Umbral de disparo: {Temp_ref + 5}°C")
        
        # Evalúa las condiciones de la tabla 9-1
        if Temp_actual > (Temp_ref + 5):
            led.value(1)     # Acción LED = ON
            buzzer.value(1)  # Acción BUZZER = ON
        else:
            led.value(0)     # Acción LED = OFF
            buzzer.value(0)  # Acción BUZZER = OFF
            
    except OSError as e:
        print("Error de lectura del sensor:", e)
        
    time.sleep(2)