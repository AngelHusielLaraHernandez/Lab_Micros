from machine import Pin, UART

# La conexión física RX/TX cruzada es la misma, la magia la hace el módulo BT [cite: 359]
uart = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))

led0 = Pin(0, Pin.OUT)
led1 = Pin(1, Pin.OUT)
led2 = Pin(2, Pin.OUT)
led3 = Pin(3, Pin.OUT)

while True:
    if uart.any() > 0:
        # Pasa el carácter a mayúscula por seguridad [cite: 359]
        data = uart.read(1).decode('utf-8').upper() 
        
        if data == 'A':
            led0.value(1) [cite: 359]
        elif data == 'T':
            led1.value(1) [cite: 359]
        elif data == 'D':
            led2.value(1) [cite: 359]
        elif data == 'I':
            led3.value(1) [cite: 359]
        elif data == 'S':
            # Apaga todo [cite: 359]
            led0.value(0) 
            led1.value(0)
            led2.value(0)
            led3.value(0)