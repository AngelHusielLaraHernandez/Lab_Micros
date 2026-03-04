import machine # Importa la librería de hardware
import utime   # Importa la librería de tiempo

# Configura el pin GPIO 0 como salida
LED = machine.Pin(0, machine.Pin.OUT)

while True:                 # Bucle principal
    # --- Tiempos pequeños (Parpadeo rápido) ---
    LED.value(1)            # Enciende el LED
    utime.sleep_ms(100)     # Espera solo 100 ms (muy rápido)
    LED.value(0)            # Apaga el LED
    utime.sleep_ms(100)     # Espera 100 ms
    
    # --- Tiempos grandes (Parpadeo lento) ---
    LED.value(1)            # Enciende el LED
    utime.sleep_ms(2000)    # Espera 2000 ms (2 segundos)
    LED.value(0)            # Apaga el LED
    utime.sleep_ms(2000)    # Espera 2 segundos