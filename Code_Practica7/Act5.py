from machine import Pin, UART, ADC, PWM
import time

# Configuración UART
uart = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))

# Configuración de periféricos de prácticas anteriores 
pot = ADC(26)
ldr = ADC(27)
tmp36 = ADC(28)
buzzer = PWM(Pin(22))
buzzer.duty_u16(0)
leds = [Pin(i, Pin.OUT) for i in range(8)]

def apagar_leds():
    for led in leds: led.value(0)

uart.write('Menú Actividad 5 listo. Ingrese una opcion (1-7):\n')

while True:
    if uart.any() > 0:
        # Lee 1 byte y lo decodifica a texto
        cmd = uart.read(1).decode('utf-8') 
        
        if cmd == '1':
            voltaje = pot.read_u16() * (3.3 / 65535)
            uart.write(f"Potenciometro: {voltaje:.2f} V\n") [cite: 358]
            
        elif cmd == '2':
            val_ldr = ldr.read_u16()
            uart.write(f"LDR (Hex): {hex(val_ldr)}\n") [cite: 358]
            
        elif cmd == '3':
            v_tmp = tmp36.read_u16() * (3.3 / 65535)
            temp_c = (v_tmp - 0.5) * 100
            temp_f = (temp_c * 9/5) + 32
            temp_k = temp_c + 273.15
            uart.write(f"TMP36: {temp_c:.1f} C, {temp_f:.1f} F, {temp_k:.1f} K\n") [cite: 358]
            
        elif cmd == '4':
            uart.write("Reproduciendo DO...\n") [cite: 358]
            buzzer.freq(261) # Frecuencia DO
            buzzer.duty_u16(32768)
            time.sleep(0.5)
            buzzer.duty_u16(0)
            
        elif cmd == '5':
            uart.write("Parpadeo 5 veces\n") [cite: 358]
            for _ in range(5):
                for led in leds: led.value(1)
                time.sleep(0.2)
                for led in leds: led.value(0)
                time.sleep(0.2)
                
        elif cmd == '6':
            uart.write("Corrimiento Derecha\n") [cite: 358]
            apagar_leds()
            for i in range(8):
                leds[i].value(1)
                time.sleep(0.1)
                leds[i].value(0)
                
        elif cmd == '7':
            uart.write("Corrimiento Izquierda\n") [cite: 358]
            apagar_leds()
            for i in range(7, -1, -1):
                leds[i].value(1)
                time.sleep(0.1)
                leds[i].value(0)
                
    time.sleep(0.05)