# ============================================================
#  PROYECTO FINAL - Multimetro Digital con Raspberry Pi Pico 2W
#  Laboratorio de Microcomputadoras - UNAM FI
#  Equipo: Espinoza, Flores, Lara
# ============================================================
#
#  Hardware:
#    - Pantalla OLED SSD1306 128x64 (I2C0: SDA=GP0, SCL=GP1)
#    - 4 Botones con pull-up externo 10k a 3.3V (GP2-GP5)
#    - LM35 sensor de temperatura (GP28 / ADC2)
#    - Divisor de voltaje 12k/2.2k  (GP26 / ADC0)
#    - Resistencia shunt 1 ohm 1W   (GP27 / ADC1)
#
#  Pines justificados segun datasheet Pico 2W (RP-008304):
#    GP0  (Pin  1) -> I2C0 SDA  - Datos OLED
#    GP1  (Pin  2) -> I2C0 SCL  - Reloj OLED
#    GP2  (Pin  4) -> GPIO IN   - Boton Arriba
#    GP3  (Pin  5) -> GPIO IN   - Boton Abajo
#    GP4  (Pin  6) -> GPIO IN   - Boton Enter
#    GP5  (Pin  7) -> GPIO IN   - Boton Back
#    GP26 (Pin 31) -> ADC0      - Voltimetro (divisor de voltaje)
#    GP27 (Pin 32) -> ADC1      - Amperimetro (shunt 1 ohm)
#    GP28 (Pin 34) -> ADC2      - Temperatura (LM35)
# ============================================================

from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import time
import math

# ========================
#  CONFIGURACION DE HARDWARE
# ========================

# --- Pantalla OLED 128x64 via I2C0 ---
# Segun datasheet Pico 2W (Sec. 2.1, Fig. 2):
#   GP0 = I2C0 SDA (Pin fisico 1)
#   GP1 = I2C0 SCL (Pin fisico 2)
# Frecuencia I2C: 400kHz (Fast Mode)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

# --- Botones con pull-up externo de 10k a 3.3V ---
# Cuando se presiona el boton, el pin se conecta a GND (lectura = 0)
# Cuando NO se presiona, el pull-up mantiene el pin en HIGH (lectura = 1)
# Segun datasheet Sec. 3.2: GP0-GP22 son digitales puros,
# GP2-GP5 no tienen funcion analogica, ideales para entradas digitales.
btn_arriba = Pin(2, Pin.IN, Pin.PULL_UP)   # GP2 - Pin 4
btn_abajo  = Pin(3, Pin.IN, Pin.PULL_UP)   # GP3 - Pin 5
btn_enter  = Pin(4, Pin.IN, Pin.PULL_UP)   # GP4 - Pin 6
btn_back   = Pin(5, Pin.IN, Pin.PULL_UP)   # GP5 - Pin 7

# --- Canales ADC para medicion ---
# Segun datasheet Sec. 3.2-3.3:
#   GP26 = ADC0, GP27 = ADC1, GP28 = ADC2 (los unicos 3 ADC de usuario)
#   ADC de 12 bits, lectura de 16 bits (0-65535) via read_u16()
#   Voltaje de referencia = 3.3V (rail IOVDD)
#   Voltaje maximo en pin ADC: IOVDD + 300mV = 3.6V (absoluto)
adc_voltaje   = ADC(Pin(26))  # ADC0 - Divisor de voltaje (12k + 2.2k)
adc_corriente = ADC(Pin(27))  # ADC1 - Resistencia shunt 1 ohm
adc_temp      = ADC(Pin(28))  # ADC2 - Sensor LM35

# ========================
#  CONSTANTES DE CALIBRACION
# ========================

# Factor de conversion ADC: 3.3V / 65535 (16 bits)
ADC_FACTOR = 3.3 / 65535

# Divisor de voltaje: R1 = 12k (superior), R2 = 2.2k (inferior)
# Vout = Vin * R2 / (R1 + R2)
# Vin  = Vout * (R1 + R2) / R2
# Factor = (12000 + 2200) / 2200 = 14200 / 2200 = 6.4545
# Voltaje maximo medible: 3.3V * 6.4545 = 21.3V (margen de seguridad)
R1 = 12000  # Ohms
R2 = 2200   # Ohms
DIVISOR_FACTOR = (R1 + R2) / R2  # 6.4545...

# Amperimetro: R_shunt = 1 ohm
# V = I * R  =>  I = V / R = V / 1 = V
# Corriente en mA = voltaje_adc * 1000
R_SHUNT = 1.0  # Ohms

# LM35: 10mV por grado Celsius
# Temperatura = Voltaje / 0.010
LM35_FACTOR = 0.010  # V/°C

# Numero de muestras para promediar (reduce ruido del ADC)
NUM_MUESTRAS = 16

# ========================
#  VARIABLES DE ESTADO
# ========================

opciones_menu = ["Temperatura", "Voltaje DC", "Corriente DC"]
unidades_menu = ["C", "V", "mA"]
indice_menu = 0
estado = "INTRO"  # INTRO -> MENU -> MEDICION

# Anti-rebote: tiempo minimo entre pulsaciones (ms)
DEBOUNCE_MS = 200
ultimo_pulso = 0

# ========================
#  FUNCIONES AUXILIARES
# ========================

def debounce():
    """Retorna True si ha pasado suficiente tiempo desde la ultima pulsacion."""
    global ultimo_pulso
    ahora = time.ticks_ms()
    if time.ticks_diff(ahora, ultimo_pulso) > DEBOUNCE_MS:
        ultimo_pulso = ahora
        return True
    return False

def leer_adc_promedio(adc, n=NUM_MUESTRAS):
    """Lee el ADC n veces y retorna el promedio para reducir ruido."""
    suma = 0
    for _ in range(n):
        suma += adc.read_u16()
    return suma / n

# ========================
#  FUNCIONES DE MEDICION
# ========================

def medir_temperatura():
    """
    Lee la temperatura del sensor LM35.
    LM35 produce 10mV por cada grado Celsius.
    Temp (C) = Voltaje_ADC / 0.010
    """
    lectura = leer_adc_promedio(adc_temp)
    voltaje = lectura * ADC_FACTOR
    temperatura = voltaje / LM35_FACTOR
    return temperatura

def medir_voltaje():
    """
    Lee el voltaje externo a traves del divisor de voltaje.
    Divisor: R1=12k (serie), R2=2.2k (a GND)
    Vin = Vadc * (R1 + R2) / R2
    Rango: 0 a ~21.3V DC
    """
    lectura = leer_adc_promedio(adc_voltaje)
    voltaje_adc = lectura * ADC_FACTOR
    voltaje_real = voltaje_adc * DIVISOR_FACTOR
    return voltaje_real

def medir_corriente():
    """
    Lee la corriente a traves de la resistencia shunt.
    R_shunt = 1 ohm, V = I*R => I = V/R = V (en Amperes)
    Resultado en miliamperes: I_mA = V * 1000
    Rango: 0 a 3300 mA (limitado por potencia del shunt a ~1A)
    """
    lectura = leer_adc_promedio(adc_corriente)
    voltaje = lectura * ADC_FACTOR
    corriente_mA = (voltaje / R_SHUNT) * 1000
    return corriente_mA

# ========================
#  FUNCIONES DE DIBUJO OLED
# ========================

def dibujar_marco(titulo=""):
    """Dibuja un marco decorativo en la pantalla OLED."""
    oled.fill(0)
    # Marco exterior
    oled.rect(0, 0, 128, 64, 1)
    # Linea doble superior
    oled.hline(0, 2, 128, 1)
    if titulo:
        # Barra de titulo
        oled.fill_rect(1, 1, 126, 12, 1)
        # Centrar titulo
        x = (128 - len(titulo) * 8) // 2
        oled.text(titulo, x, 3, 0)

def centrar_texto(texto, y, color=1):
    """Escribe texto centrado horizontalmente."""
    x = (128 - len(texto) * 8) // 2
    if x < 0:
        x = 0
    oled.text(texto, x, y, color)

# ========================
#  ANIMACION DE ENTRADA
# ========================

def animacion_intro():
    """
    Animacion de inicio que muestra:
    1. Efecto de borde expandiendose
    2. Titulo del proyecto
    3. Nombre de los integrantes
    Segun especificacion: mostrar numero de equipo y nombres.
    """
    # --- Fase 1: Efecto de borde expandiendose ---
    for i in range(0, 32, 2):
        oled.fill(0)
        oled.rect(32 - i, 32 - i, i * 2, i * 2, 1)
        oled.show()
        time.sleep_ms(30)

    # --- Fase 2: Titulo con efecto de escritura ---
    oled.fill(0)
    oled.rect(0, 0, 128, 64, 1)
    oled.hline(0, 2, 128, 1)
    oled.fill_rect(1, 1, 126, 12, 1)
    oled.show()
    time.sleep_ms(200)

    # Escribir titulo letra por letra
    titulo = "MULTIMETRO"
    x_start = (128 - len(titulo) * 8) // 2
    for i, c in enumerate(titulo):
        oled.text(c, x_start + i * 8, 3, 0)
        oled.show()
        time.sleep_ms(80)

    time.sleep_ms(300)

    # Subtitulo
    sub = "Pico 2W"
    centrar_texto(sub, 18)
    oled.show()
    time.sleep_ms(500)

    # Linea separadora animada
    for x in range(0, 128, 4):
        oled.hline(0, 28, x, 1)
        oled.show()
        time.sleep_ms(10)

    time.sleep_ms(200)

    # --- Fase 3: Nombres de integrantes ---
    # Nombres del archivo portada.tex
    nombres = [
        "Espinoza Percival",
        "Flores Victor",
        "Lara Angel"
    ]

    y_pos = 33
    for nombre in nombres:
        # Efecto: texto aparece de izquierda a derecha
        for i in range(len(nombre) + 1):
            # Limpiar zona de texto
            oled.fill_rect(4, y_pos, 120, 10, 0)
            texto_parcial = nombre[:i]
            oled.text(texto_parcial, 8, y_pos, 1)
            oled.show()
            time.sleep_ms(40)
        y_pos += 10

    time.sleep_ms(1500)

    # --- Fase 4: Transicion al menu ---
    # Efecto de barrido horizontal
    for x in range(0, 128, 4):
        oled.fill_rect(x, 0, 4, 64, 0)
        oled.show()
        time.sleep_ms(15)

    time.sleep_ms(200)

# ========================
#  INTERFAZ DE MENU
# ========================

def dibujar_menu():
    """
    Dibuja el menu principal con las 3 opciones.
    La opcion seleccionada se resalta con fondo blanco.
    Segun la especificacion del proyecto:
      - Se muestra '*' antes de la opcion seleccionada
      - Botones arriba/abajo para navegar
      - Enter para seleccionar
    """
    oled.fill(0)

    # Marco y titulo
    oled.rect(0, 0, 128, 64, 1)
    oled.fill_rect(1, 1, 126, 13, 1)
    centrar_texto("MULTIMETRO", 3, 0)

    # Linea separadora bajo titulo
    oled.hline(1, 15, 126, 1)

    # Dibujar opciones del menu
    for i in range(len(opciones_menu)):
        y = 19 + i * 15

        if i == indice_menu:
            # Opcion seleccionada: fondo blanco, texto negro
            oled.fill_rect(2, y, 124, 13, 1)
            oled.text(">" + opciones_menu[i], 6, y + 3, 0)
        else:
            # Opcion normal: texto blanco
            oled.text(" " + opciones_menu[i], 6, y + 3, 1)

    # Indicadores de navegacion en la parte inferior
    oled.hline(1, 62, 126, 1)

    oled.show()

# ========================
#  PANTALLA DE MEDICION
# ========================

def dibujar_medicion(nombre, valor, unidad):
    """
    Dibuja la pantalla de medicion con:
    - Titulo de la magnitud
    - Valor numerico grande
    - Unidad de medida
    - Indicador de boton Back
    """
    oled.fill(0)

    # Marco
    oled.rect(0, 0, 128, 64, 1)

    # Barra de titulo
    oled.fill_rect(1, 1, 126, 13, 1)
    centrar_texto(nombre, 3, 0)

    # Linea bajo titulo
    oled.hline(1, 15, 126, 1)

    # Valor numerico (centrado, mas grande visualmente)
    if nombre == "Temperatura":
        texto_valor = "{:.1f}".format(valor)
        texto_unidad = chr(248) + "C"  # °C (puede no renderizar, usar alternativa)
        texto_unidad = "grados C"
    elif nombre == "Voltaje DC":
        texto_valor = "{:.2f}".format(valor)
        texto_unidad = "V DC"
    else:  # Corriente
        texto_valor = "{:.1f}".format(valor)
        texto_unidad = "mA DC"

    # Mostrar valor grande
    centrar_texto(texto_valor, 25)

    # Mostrar unidad
    centrar_texto(texto_unidad, 38)

    # Barra de progreso visual (porcentaje del rango)
    if nombre == "Temperatura":
        porcentaje = min(valor / 100.0, 1.0)
    elif nombre == "Voltaje DC":
        porcentaje = min(valor / 20.0, 1.0)
    else:
        porcentaje = min(valor / 3300.0, 1.0)

    # Dibujar barra
    barra_ancho = int(100 * porcentaje)
    oled.rect(13, 49, 102, 7, 1)  # Marco de la barra
    if barra_ancho > 0:
        oled.fill_rect(14, 50, barra_ancho, 5, 1)  # Relleno

    # Indicador de retorno
    oled.text("<Back", 1, 56, 1)

    oled.show()

# ========================
#  BUCLE PRINCIPAL
# ========================

def main():
    global indice_menu, estado

    # --- Pantalla de inicio con animacion ---
    estado = "INTRO"
    animacion_intro()

    # --- Transicion a menu ---
    estado = "MENU"
    dibujar_menu()

    # --- Maquina de estados principal ---
    while True:

        if estado == "MENU":
            # --- Boton ARRIBA ---
            if btn_arriba.value() == 0 and debounce():
                if indice_menu > 0:
                    indice_menu -= 1
                    dibujar_menu()
                # Si ya esta en el tope, no hace nada (spec)

            # --- Boton ABAJO ---
            elif btn_abajo.value() == 0 and debounce():
                if indice_menu < len(opciones_menu) - 1:
                    indice_menu += 1
                    dibujar_menu()
                # Si ya esta al fondo, no hace nada (spec)

            # --- Boton ENTER ---
            elif btn_enter.value() == 0 and debounce():
                estado = "MEDICION"
                # Mostrar primera lectura inmediatamente
                oled.fill(0)
                centrar_texto("Leyendo...", 28)
                oled.show()
                time.sleep_ms(100)

        elif estado == "MEDICION":
            # Realizar la medicion segun la opcion seleccionada
            if indice_menu == 0:
                valor = medir_temperatura()
                dibujar_medicion("Temperatura", valor, "C")
            elif indice_menu == 1:
                valor = medir_voltaje()
                dibujar_medicion("Voltaje DC", valor, "V")
            elif indice_menu == 2:
                valor = medir_corriente()
                dibujar_medicion("Corriente DC", valor, "mA")

            # Actualizar cada 250ms (4 lecturas por segundo)
            time.sleep_ms(250)

            # --- Boton BACK: regresar al menu ---
            if btn_back.value() == 0 and debounce():
                estado = "MENU"
                dibujar_menu()

        # Pequena pausa para no saturar el CPU
        time.sleep_ms(10)

# --- Punto de entrada ---
main()
