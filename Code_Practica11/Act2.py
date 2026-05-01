from machine import Pin
import utime

S1 = Pin(12, Pin.IN, Pin.PULL_UP)
# Salida para la señal cuadrada en GPIO 20 (LED)
salida_senal = Pin(20, Pin.OUT)

# Variable global para comunicar la ISR con el bucle principal
generar_senal = False

def FuncISR_S1(pin):
    global generar_senal
    generar_senal = not generar_senal # Alterna el estado (Activa/Desactiva la señal)
    print("Estado de señal cambiado")
    utime.sleep_ms(200) # Antirrebote

# Configura la interrupción por flanco de bajada
S1.irq(trigger=Pin.IRQ_FALLING, handler=FuncISR_S1)

print("Presiona S1 para iniciar/detener la señal de 1Hz")

while True:
    if generar_senal:
        # Genera una señal de 1 Hz (1 ciclo por segundo = 0.5s en Alto y 0.5s en Bajo)
        salida_senal.value(1)
        utime.sleep(0.5)
        salida_senal.value(0)
        utime.sleep(0.5)
    else:
        # Si no debe generar señal, asegura que la salida esté apagada
        salida_senal.value(0)
        utime.sleep(0.1) # Pequeña pausa para no saturar el procesador