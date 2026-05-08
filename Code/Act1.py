from machine import Pin
import utime

# Configura S1 en el GPIO 12 como entrada con resistencia Pull-Up interna
S1 = Pin(12, Pin.IN, Pin.PULL_UP)

# Función de Manejo de Interrupción (Interrupt Service Routine - ISR)
# Se ejecuta automáticamente cuando ocurre el evento
def FuncISR_S1(pin):
    print("Interrupción detectada en S1") #
    # Pequeño retardo dentro de la ISR para evitar rebotes (bouncing) mecánicos del botón
    utime.sleep_ms(200) # (Reducido a 200ms, 1 segundo es mucho para una ISR)

# Vincula la función ISR al pin S1. 
# trigger=Pin.IRQ_FALLING significa que se activa al presionar el botón (pasar de 1 a 0)
S1.irq(trigger=Pin.IRQ_FALLING, handler=FuncISR_S1)

print("! ... Esperando Interrupción !") #

# Bucle principal infinito. El procesador se queda aquí hasta que ocurre una interrupción.
while True: #
    pass # No hace nada, solo espera