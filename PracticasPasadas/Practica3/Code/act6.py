import machine
import utime

# Lista de pines configurados como salidas (GPIO 0 a 7)
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(8)]

while True:
    # Repetir la acción de parpadeo 10 veces
    for repeticion in range(10):
        # Todos encendidos
        for led in leds:
            led.value(1)
        utime.sleep_ms(200) # Retardo de 200 ms (según tabla)
        
        # Todos apagados
        for led in leds:
            led.value(0)
        utime.sleep_ms(200) # Retardo de 200 ms (según tabla)
        
    # Mantener apagado 2 segundos después de las 10 repeticiones
    for led in leds:
        led.value(0)        # Asegurar que todos estén apagados
    utime.sleep_ms(2000)    # Retardo de 2000 ms (2 segundos)