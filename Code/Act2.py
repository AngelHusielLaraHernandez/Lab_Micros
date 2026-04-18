from machine import Pin, SPI
import max7219_8digit
import time

# --- Configuración SPI y Display ---
spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
ss = Pin(5, Pin.OUT)
display = max7219_8digit.Display(spi, ss)

# --- Entradas de Control ---
# Configura GPIO12 para conteo ascendente y GPIO13 para conteo descendente
btn_asc = Pin(12, Pin.IN, Pin.PULL_UP)
btn_desc = Pin(13, Pin.IN, Pin.PULL_UP)

# Variables globales para el contador
contador = 0
direccion = 0 # 1 = subiendo, -1 = bajando, 0 = detenido

while True:
    # Evalúa si se presionó el botón ascendente (lee 0 por el Pull-Up)
    if btn_asc.value() == 0:
        direccion = 1
    # Evalúa si se presionó el botón descendente
    elif btn_desc.value() == 0:
        direccion = -1

    # Aplica el incremento o decremento según la dirección activa
    if direccion == 1:
        contador += 1
    elif direccion == -1:
        contador -= 1

    # Formatea el número a 8 espacios para limpiar residuos en el display (ej. "       5")
    texto = "{:8d}".format(contador)
    
    # Envía y muestra el texto
    display.write_to_buffer(texto)
    display.display()
    
    # Retardo condicionado: 0.5s si está contando (según manual), 0.1s si está en reposo
    if direccion != 0:
        time.sleep(0.5)
    else:
        time.sleep(0.1)