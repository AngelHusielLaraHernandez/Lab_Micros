import tm1637
from machine import Pin
from utime import sleep

tm = tm1637.TM1637(clk=Pin(0), dio=Pin(1))
tm.brightness(3)

# Configura el zumbador en el GPIO 17
zumbador = Pin(17, Pin.OUT) 

# Conteo desde 20 hasta 0
for cuenta in range(20, -1, -1):
    tm.number(cuenta) 
    sleep(1)          
    
# Activa la alarma por 1 segundo
zumbador.value(1) 
sleep(1)          
zumbador.value(0)