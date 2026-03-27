from machine import ADC
import time

# Configura el ADC0 asociado al pin físico GPIO26 donde está el potenciómetro
potenciometro = ADC(26) 

while True:
    # Lee la conversión analógico-digital (resultado de 16 bits)
    conversion = potenciometro.read_u16()
    
    # Transforma ese valor digital (0 - 65535) a su voltaje real (0 - 3.3V)
    voltaje = conversion * (3.3 / 65535)
    
    # Despliega con el formato solicitado, usando 2 decimales para el voltaje
    print(f"Conversión = {conversion}; Voltaje = {voltaje:.2f} Volts")
    
    # Actualiza cada segundo
    time.sleep(1)