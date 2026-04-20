from ST7735 import TFT
from sysfont import sysfont
from machine import SPI, Pin

# Configuración SPI0. Las pantallas TFT ST7735 suelen requerir una frecuencia alta (20MHz) y polaridad 0
spi = SPI(0, baudrate=20000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(4))

# Inicialización (spi, A0/DC=15, RESET=14, CS=5)
tft = TFT(spi, 15, 14, 5)

# Rutina de inicio en hardware de la pantalla
tft.initg()

# Configura el espacio de color correcto (True para pantallas que invierten BGR por RGB)
tft.rgb(True)

# Gira la orientación de la pantalla (0-3). '2' la pone invertida verticalmente o landscape
tft.rotation(2)

# Llena la pantalla con color blanco
tft.fill(TFT.WHITE)

# Escribe texto: (coordenadas), "Mensaje", Color, fuente, escala (tamaño), salto_de_línea
tft.text((10, 10), "MICROS", TFT.RED, sysfont, 2, nowrap=True)
tft.text((25, 30), "FI", TFT.GREEN, sysfont, 2, nowrap=True)