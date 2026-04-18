import tm1637
from machine import Pin
from utime import sleep

# Inicializa el display TM1637 con Reloj (CLK) en GPIO 0 y Datos (DIO) en GPIO 1
tm = tm1637.TM1637(clk=Pin(0), dio=Pin(1))

# Variables iniciales para segundos y minutos
Sec = 0
Min = 0

while True:
    # Muestra los minutos y segundos activando los dos puntos centrales (colon=True)
    tm.numbers(Min, Sec, colon=True)
    sleep(0.5) # Retardo de medio segundo
    
    # Muestra los minutos y segundos desactivando los dos puntos (efecto de parpadeo)
    tm.numbers(Min, Sec, colon=False)
    sleep(0.5) # Retardo de medio segundo
    
    Sec = Sec + 1 # Lógica del reloj: incrementa 1 segundo
    
    if Sec == 60:      # Si llega a 60 segundos...
        Min = Min + 1  # Incrementa un minuto
        Sec = 0        # Reinicia los segundos a 0
        
        if Min == 60:  # Si llega a 60 minutos...
            Min = 0    # Reinicia los minutos a 0