from machine import ADC, Pin
import time


Sensor = ADC(4)

while True:
    
    Valor = Sensor.read_u16() * (3.3 / 65535)
    
    
    Temp = 27 - (Valor - 0.706) / 0.001721
    
    
    print(Temp)
    
    
    time.sleep(1)