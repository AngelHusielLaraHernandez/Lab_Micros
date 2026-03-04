import machine
import utime

# Lista de pines configurados como salidas
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(8)]

while True:
    # --- Secuencia de llenado ---
    for i in range(8):
        leds[i].value(1)      # Enciende el LED actual, dejando los anteriores encendidos
        utime.sleep_ms(100)   # Retardo de 100 ms
        
    # Apagamos todos para reiniciar el efecto visual
    for led in leds:
        led.value(0)
    utime.sleep_ms(500)       # Pausa antes de repetir