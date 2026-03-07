from machine import Pin
import time

# --- Configuración de Entradas ---
S2 = Pin(12, Pin.IN, Pin.PULL_DOWN)  # Push button
S1 = Pin(11, Pin.IN, Pin.PULL_UP)    # Push button
SW1_1 = Pin(10, Pin.IN)              # Dip switch
SW1_2 = Pin(9, Pin.IN)               # Dip switch
SW1_3 = Pin(8, Pin.IN)               # Dip switch

# --- Configuración de Salidas ---
# Arreglo de LEDs para fácil acceso (GPIO 0 al 7)
leds = [Pin(i, Pin.OUT) for i in range(8)]
zumbador = Pin(22, Pin.OUT)

# Función para limpiar el estado (apagar todo)
def apagar_todo():
    for led in leds:
        led.value(0)
    zumbador.value(0)

# Función: Contador ascendente (0 a 9) usando los LEDs 3, 4, 5 y 6
def contador_ascendente():
    for i in range(10):
        leds[3].value((i >> 0) & 1) # Bit menos significativo
        leds[4].value((i >> 1) & 1)
        leds[5].value((i >> 2) & 1)
        leds[6].value((i >> 3) & 1) # Bit más significativo
        time.sleep(0.5)

# Función: Contador descendente (9 a 0) usando los LEDs 3, 4, 5 y 6
def contador_descendente():
    for i in range(9, -1, -1):
        leds[3].value((i >> 0) & 1)
        leds[4].value((i >> 1) & 1)
        leds[5].value((i >> 2) & 1)
        leds[6].value((i >> 3) & 1)
        time.sleep(0.5)

# Función: Simulación de notas musicales en el zumbador
def notas_musicales():
    for _ in range(3):
        zumbador.value(1)
        time.sleep(0.1)
        zumbador.value(0)
        time.sleep(0.2)

while True:
    apagar_todo()
    
    # Formamos una cadena de texto concatenando el valor actual de cada entrada
    # Ejemplo: "01000"
    estado = f"{S2.value()}{S1.value()}{SW1_1.value()}{SW1_2.value()}{SW1_3.value()}"
    
    # Evalúa la cadena y ejecuta la acción correspondiente según la Tabla 4-3
    if estado == "00111":
        contador_ascendente()
    elif estado == "11111":
        contador_descendente()
    elif estado == "10111":
        notas_musicales()
    elif estado == "01000":
        pass # Todo apagado por defecto
    elif estado == "01001":
        # Enciende LEDs específicos: 7, 6, 4, 2 y 5
        leds[7].value(1)
        leds[6].value(1)
        leds[4].value(1)
        leds[2].value(1)
        leds[5].value(1)
    
    # Se pueden agregar el resto de los "elif" para mapear cada combinación específica
    # de leds en la tabla 4-3 utilizando la misma sintaxis de encendido directo.
    
    time.sleep(0.1) # Retardo principal del bucle