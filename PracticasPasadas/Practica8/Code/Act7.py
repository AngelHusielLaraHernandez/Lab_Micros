from machine import Pin, SPI
import time
import max7219_8digit
import max7219
from ST7735 import TFT
from sysfont import sysfont

# --- 1. Entradas (Botones) ---
#btn_inicia = Pin(12, Pin.IN, Pin.PULL_DOWN)  # Inicia / Reinicia
#btn_detiene = Pin(13, Pin.IN, Pin.PULL_UP) # Detiene

# --- 2. Bus SPI Compartido ---
# Usamos una configuración equilibrada que toleren todos los módulos
spi = SPI(0, baudrate=10000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3))

# --- 3. Inicialización Dispositivos (cada uno con su propio CS) ---
# A) Display 8 Dígitos (CS = GP5)
cs_8dig = Pin(5, Pin.OUT)
disp_8dig = max7219_8digit.Display(spi, cs_8dig)

# B) Matriz 8x8 (CS = GP6)
cs_matriz = Pin(6, Pin.OUT)
matriz = max7219.Matrix8x8(spi, cs_matriz, 4)

# C) Pantalla TFT (CS = GP7, A0 = GP15, RST = GP14)
tft = TFT(spi, 15, 14, 7)
tft.initg()
tft.rgb(True)
tft.rotation(1)
tft.fill(TFT.BLACK)
tft.text((10, 10), "CONTADOR:", TFT.YELLOW, sysfont, 2, nowrap=True)

# Variables de control
contador = 0
corriendo = False

btn_inicia=0
btn_detiene=0
# --- 4. Bucle Principal ---
while True:
    # Lógica de inicio / reinicio
    if btn_inicia == 0:
        corriendo = True
        time.sleep(0.2) # Pequeño retardo antirrebote
        
    # Lógica de paro
    if btn_detiene == 1:
        corriendo = False
        time.sleep(0.2) # Pequeño retardo antirrebote

    # Si está en modo "corriendo", actualiza los 3 displays
    if corriendo:
        print(contador)
        # 1. Manda al Display de 8 dígitos
        disp_8dig.write_to_buffer("{:8d}".format(contador))
        disp_8dig.display()
        
        # 2. Manda a la Matriz LED
        matriz.fill(0)
        matriz.text(str(contador), 0, 0, 1)
        matriz.show()
        
        # 3. Manda al TFT a Color (imprime espacios en negro para "borrar" el número anterior)
        tft.text((10, 40), str(contador), TFT.CYAN, sysfont, 3, nowrap=True)
        time.sleep(0.5)
        tft.text((10, 40), str(contador), TFT.BLACK, sysfont, 3, nowrap=True)
        
        contador += 1
        time.sleep(0.5) # Velocidad del contador indicada en el manual
    else:
        time.sleep(0.1) # Reposo sin bloqueo