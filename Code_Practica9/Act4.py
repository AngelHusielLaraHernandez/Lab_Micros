import tm1637
from machine import Pin
from utime import sleep

tm = tm1637.TM1637(clk=Pin(0), dio=Pin(1))
# Zumbador conectado al GPIO 17 como salida
zumbador = Pin(17, Pin.OUT) 

# Bucle for descendente desde 20 hasta 0 (pasos de -1)
for cuenta in range(20, -1, -1):
    tm.number(cuenta) # Muestra el número actual en el display
    sleep(1)          # Retardo de 1 segundo entre cada número
    
# Al terminar el bucle (cuando llega a 0), activa la alarma
zumbador.value(1) # Enciende el zumbador
sleep(1)          # Lo mantiene sonando 1 segundo
zumbador.value(0) # Lo apaga