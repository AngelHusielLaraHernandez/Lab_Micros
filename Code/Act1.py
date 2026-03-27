from machine import ADC, Pin
import time

# Configura el ADC interno (canal 4) que corresponde al sensor de temperatura interno del RP2040
Sensor = ADC(4)

while True:
    # Lee el valor bruto de 16 bits (0 a 65535) y lo convierte a su equivalente en voltaje (0 a 3.3V)
    Valor = Sensor.read_u16() * (3.3 / 65535)
    
    # Utiliza la ecuación oficial del fabricante para transformar el voltaje leído a °C
    Temp = 27 - (Valor - 0.706) / 0.001721
    
    # Imprime la temperatura en consola
    print(Temp)
    
    # (Buena práctica): Retardo para evitar saturar la consola de Thonny
    time.sleep(1)