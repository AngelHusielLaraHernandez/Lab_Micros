import machine
import utime

# Configura los pines GPIO 2 y GPIO 3 como salidas
LED1 = machine.Pin(2, machine.Pin.OUT)
LED2 = machine.Pin(3, machine.Pin.OUT)

while True:
    # Estado 1: GPIO2 en Alto (1), GPIO3 en Bajo (0)
    LED1.value(1)
    LED2.value(0)
    utime.sleep_ms(85) # Espera 85 ms entre estados
    
    # Estado 2: GPIO2 en Bajo (0), GPIO3 en Alto (1)
    LED1.value(0)
    LED2.value(1)
    utime.sleep_ms(85) # Espera 85 ms entre estados