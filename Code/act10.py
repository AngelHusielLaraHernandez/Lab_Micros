import machine
import utime

# Definición de pines para Semáforo 1
V1 = machine.Pin(0, machine.Pin.OUT) # Verde 1
A1 = machine.Pin(1, machine.Pin.OUT) # Amarillo 1
R1 = machine.Pin(2, machine.Pin.OUT) # Rojo 1

# Definición de pines para Semáforo 2
R2 = machine.Pin(5, machine.Pin.OUT) # Rojo 2
A2 = machine.Pin(6, machine.Pin.OUT) # Amarillo 2
V2 = machine.Pin(7, machine.Pin.OUT) # Verde 2

# Función auxiliar para apagar todos los LEDs de los semáforos
def apagar_todos():
    V1.value(0)
    A1.value(0)
    R1.value(0)
    V2.value(0)
    A2.value(0)
    R2.value(0)

while True:
    apagar_todos()
    # Estado 1: V1 encendido, R2 encendido por 5 segundos
    V1.value(1)
    R2.value(1)
    utime.sleep_ms(5000)
    
    # Estado 2: V1 intermitente (5 veces, 200 ms), R2 sigue encendido
    for _ in range(5):
        V1.value(0)          # Apaga V1
        utime.sleep_ms(200)  # Retardo 200 ms
        V1.value(1)          # Enciende V1
        utime.sleep_ms(200)  # Retardo 200 ms
        
    apagar_todos()
    # Estado 3: A1 encendido, R2 encendido por 3 segundos
    A1.value(1)
    R2.value(1)
    utime.sleep_ms(3000)
    
    apagar_todos()
    # Estado 4: R1 encendido, V2 encendido por 5 segundos
    R1.value(1)
    V2.value(1)
    utime.sleep_ms(5000)
    
    # Estado 5: R1 sigue encendido, V2 intermitente (5 veces, 200 ms)
    for _ in range(5):
        V2.value(0)          # Apaga V2
        utime.sleep_ms(200)  # Retardo 200 ms
        V2.value(1)          # Enciende V2
        utime.sleep_ms(200)  # Retardo 200 ms
        
    apagar_todos()
    # Estado 6: R1 encendido, A2 encendido por 3 segundos
    R1.value(1)
    A2.value(1)
    utime.sleep_ms(3000)