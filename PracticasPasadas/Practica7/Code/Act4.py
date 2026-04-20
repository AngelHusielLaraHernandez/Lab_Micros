from machine import Pin, UART
import time

# Configura el UART0 a 9600 baudios usando el GPIO16(TX) y GPIO17(RX) 
uart = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))
# Formato estándar: 8 bits de datos, sin paridad, 1 bit de paro 
uart.init(bits=8, parity=None, stop=1)
led = Pin(25, Pin.OUT)

# Envía mensaje al módulo USB-TTL 
uart.write('Inicia Comunicacion Serie\n')

while True:
    # Comprueba si hay datos en el buffer de recepción UART 
    if uart.any() > 0: 
        data = uart.read() # Lee todos los datos disponibles 
        uart.write(data)   # Eco: retransmite lo mismo que recibió 
        led.toggle()       # Cambia el estado del LED interno 
    
    # Se ajusta a 0.1s para mayor fluidez, en el manual dice 1s pero eso causa retrasos al teclear.
    time.sleep(0.1)