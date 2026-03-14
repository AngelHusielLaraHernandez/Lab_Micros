import machine
import utime

# Lista de pines configurados como salidas
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(8)]

while True:
    # Recorrer cada LED de la lista (del GPIO 0 al 7)
    for i in range(8):
        # Apagamos todos los LEDs primero para limpiar el estado
        for led in leds:
            led.value(0)
            
        # Encendemos solo el LED actual en la secuencia
        leds[i].value(1)
        
        # Retardo de 100 ms según la solicitud
        utime.sleep_ms(100)