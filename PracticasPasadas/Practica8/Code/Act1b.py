from machine import Pin, SPI
import max7219_8digit
import time

spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
ss = Pin(5, Pin.OUT)

display = max7219_8digit.Display(spi, ss)

display.write_to_buffer("01234567")
display.display()

time.sleep(1)