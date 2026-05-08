from machine import Pin
import utime
import _thread # Librería para manejo de hilos (núcleos paralelos)

led1 = Pin(18, Pin.OUT) #
led2 = Pin(20, Pin.OUT) #

# Esta función se ejecutará en el SEGUNDO núcleo (Core 1)
def led2_thread():
    while True: #
        print("Este es un mensaje del segundo nucleo") #
        led2.toggle() # Cambia el estado del led2
        utime.sleep(0.2) # Pausa de 0.2 segundos

# Inicia el hilo secundario llamando a la función led2_thread
_thread.start_new_thread(led2_thread, ())

# Este bucle se ejecuta en el PRIMER núcleo (Core 0)
while True: #
    led1.toggle() # Cambia el estado del led1
    utime.sleep(0.25) # Pausa de 0.25 segundos