from machine import Pin
import time

# --- Configuración de Entradas ---
s2 = Pin(12, Pin.IN, Pin.PULL_DOWN) # Botón 2
s1 = Pin(11, Pin.IN, Pin.PULL_UP)   # Botón 1
sw1_1 = Pin(10, Pin.IN)             # Switch 1
sw1_2 = Pin(9, Pin.IN)              # Switch 2
sw1_3 = Pin(8, Pin.IN)              # Switch 3

# --- Configuración de Salidas ---
leds = [Pin(i, Pin.OUT) for i in range(8)] # GPIO0 a GPIO7
buzzer = Pin(22, Pin.OUT)
# Pines reservados para el contador en binario
contador_pins = [Pin(3, Pin.OUT), Pin(4, Pin.OUT), Pin(5, Pin.OUT), Pin(6, Pin.OUT)]

def apagar_todo():
    for led in leds: led.value(0)
    buzzer.value(0)

def encender_todo():
    for led in leds: led.value(1)
    buzzer.value(0)

def mostrar_contador(num):
    """Muestra un número binario de 4 bits en los pines del contador"""
    for i in range(4):
        contador_pins[i].value((num >> i) & 1)

while True:
    # Si los botones S1 y S2 están en su estado de activación, evaluar el DIP Switch
    # Combina los valores de los 3 switches en un solo número entero (0 a 7)
    estado_dip = (sw1_1.value() << 2) | (sw1_2.value() << 1) | sw1_3.value()
    
    if estado_dip == 0:     # 000: Todos apagados
        apagar_todo()
    elif estado_dip == 1:   # 001: Todos encendidos
        encender_todo()
    elif estado_dip == 4:   # 100: Contador ascendente 0-9
        apagar_todo()
        for i in range(10):
            mostrar_contador(i)
            time.sleep(0.5)
    elif estado_dip == 5:   # 101: Contador descendente 9-0
        apagar_todo()
        for i in range(9, -1, -1):
            mostrar_contador(i)
            time.sleep(0.5)
    elif estado_dip == 7:   # 111: Notas musicales (Simulación)
        apagar_todo()
        for _ in range(3):  # Parpadeo del zumbador
            buzzer.value(1)
            time.sleep(0.1)
            buzzer.value(0)
            time.sleep(0.1)
    else:
        apagar_todo() # Para el resto de combinaciones
        
    time.sleep(0.1)