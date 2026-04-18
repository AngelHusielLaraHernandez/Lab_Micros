from ST7735 import TFT
from sysfont import sysfont
from machine import SPI, Pin

spi = SPI(0, baudrate=20000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(4))

# Nota: Cambiamos CS al pin 7 según el diagrama de integración de la siguiente actividad
tft = TFT(spi, 15, 14, 7) 
tft.initg()
tft.rgb(True)
tft.rotation(1) # Rotación en modo apaisado (Landscape)
        
tft.fill(TFT.BLACK) # Fondo Negro para resaltar colores
        
# Escribimos los nombres en diferentes líneas (eje Y va aumentando) y con distintos colores
tft.text((5, 10), "1. Juan Perez", TFT.CYAN, sysfont, 1, nowrap=True)
tft.text((5, 30), "2. Maria Gomez", TFT.YELLOW, sysfont, 1, nowrap=True)
tft.text((5, 50), "3. Luis Lopez", TFT.MAGENTA, sysfont, 1, nowrap=True)
tft.text((5, 70), "4. Ana Diaz", TFT.WHITE, sysfont, 1, nowrap=True)

# Título más grande (escala 2) en la parte inferior
tft.text((5, 100), "Equipo", TFT.RED, sysfont, 2, nowrap=True)