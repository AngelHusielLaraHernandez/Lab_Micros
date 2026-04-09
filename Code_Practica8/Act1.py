from machine import Pin, SPI
import max7219_8digit
import time

# Configura el bus SPI0. Frecuencia de 10MHz, polaridad 1 y fase 0 requeridas por el MAX7219.
# SCK (Reloj) en GPIO2, MOSI (Datos de salida) en GPIO3.
spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))

# Configura el pin GPIO5 como salida para el Chip Select (SS/CS)
ss = Pin(5, Pin.OUT)

# Crea el objeto del display vinculando el bus SPI y el pin de selección
display = max7219_8digit.Display(spi, ss)

# Escribe la cadena de texto en la memoria intermedia (buffer) del controlador
display.write_to_buffer("01234567")

# Ejecuta el comando para que lo que está en el buffer se muestre físicamente en los LEDs
display.display()

# Pequeña pausa al finalizar
time.sleep(1)