from machine import Pin
import time

# Configura S1 (GPIO 11) como entrada con PULL_UP interna
S1 = Pin(11, Pin.IN, Pin.PULL_UP)

# Configura salidas de los LEDs y el zumbador
led4 = Pin(4, Pin.OUT)
led5 = Pin(5, Pin.OUT)
led6 = Pin(6, Pin.OUT)
led7 = Pin(7, Pin.OUT)
buzzer = Pin(22, Pin.OUT)

def apagar_salidas():
    led4.value(0)
    led5.value(0)
    led6.value(0)
    led7.value(0)
    buzzer.value(0)

def encender_salidas():
    led4.value(1)
    led5.value(1)
    led6.value(1)
    led7.value(1)
    buzzer.value(1)

while True:
    # Como es PULL_UP, 1 significa botón liberado y 0 botón presionado
    if S1.value() == 1:
        apagar_salidas()
        print("Push button S1 liberado, '1'\nSalidas en bajo")
    else:
        encender_salidas()
        print("Push button S1 presionado, '0'\nSalidas en alto")
        
    time.sleep(0.2) # Pequeño retardo para evitar rebotes