from machine import Pin, UART
import time

uart = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))
uart.init(bits=8, parity=None, stop=1)
led = Pin(25, Pin.OUT)
uart.write('Inicia Comunicacion Serie\n')
while True:
    if uart.any() > 0: 
        data = uart.read()
        uart.write(data)   
        led.toggle()       
    time.sleep(0.1)