from machine import ADC, Pin
import time

# Configuración de pines según esquema
foto_resistencia = ADC(27) # GPIO27 corresponde al ADC1
led = Pin(7, Pin.OUT)      # LED controlado

# Valor de referencia umbral (Cámbialo tras ver qué rango arroja tu LDR físicamente)
V_REF = 30000 

# Variables para guardar memoria histórica de luz
val_max = 0
val_min = 65535

while True:
    lectura = foto_resistencia.read_u16()
    
    # Actualiza los límites si se detecta un nuevo máximo o mínimo
    if lectura > val_max: val_max = lectura
    if lectura < val_min: val_min = lectura
        
    print(f"Luz actual: {lectura} | Min: {val_min} | Max: {val_max} | Umbral: {V_REF}")
    
    # Condición solicitada: si la lectura rebasa la referencia, se enciende.
    if lectura > V_REF:
        led.value(1) # Alto
    else:
        led.value(0) # Bajo
        
    time.sleep(0.5)