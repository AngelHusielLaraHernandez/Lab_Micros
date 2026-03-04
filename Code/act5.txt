import machine
import utime

# Crear una lista con los pines del 0 al 7 configurados como salida
# Esto facilita encenderlos y apagarlos todos juntos con un bucle
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(8)]

while True:
    # --- Estado: Todos en '1' (Encendidos) ---
    for led in leds:
        led.value(1)       # Asigna el valor 1 a cada LED de la lista
    utime.sleep_ms(500)    # Retardo a elección (500 ms)
    
    # --- Estado: Todos en '0' (Apagados) ---
    for led in leds:
        led.value(0)       # Asigna el valor 0 a cada LED de la lista
    utime.sleep_ms(500)    # Retardo a elección (500 ms)