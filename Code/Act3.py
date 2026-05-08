from machine import Pin
import utime
import tm1637 # Requiere tener la librería tm1637.py en la Raspberry Pi Pico

# --- Entradas ---
S1 = Pin(12, Pin.IN, Pin.PULL_UP) #
S2 = Pin(13, Pin.IN, Pin.PULL_UP) #

# --- Salidas ---
led1 = Pin(18, Pin.OUT) #
led2 = Pin(19, Pin.OUT) #

# --- Displays ---
tm_s1 = tm1637.TM1637(clk=Pin(0), dio=Pin(1))  # Display para S1
tm_s2 = tm1637.TM1637(clk=Pin(10), dio=Pin(11)) # Display para S2

# --- Variables Globales ---
contador_s1 = 0
contador_s2 = 0

# --- Rutinas de Interrupción (ISR) ---
def FuncISR_S1(pin):
    global contador_s1
    led1.value(1) # LED ON
    contador_s1 += 1
    tm_s1.number(contador_s1) # Actualiza cuenta en display
    print(f"Interrupción S1. Cuenta: {contador_s1}")
    utime.sleep_ms(300) # Antirrebote y retardo para ver el LED encendido
    led1.value(0) # Apaga el LED después del retardo

def FuncISR_S2(pin):
    global contador_s2
    led2.value(1) # LED ON
    contador_s2 += 1
    tm_s2.number(contador_s2) # Actualiza cuenta en display
    print(f"Interrupción S2. Cuenta: {contador_s2}")
    utime.sleep_ms(300) 
    led2.value(0) 

# --- Configuración de Interrupciones ---
# Ambas se disparan por flanco de bajada
S1.irq(trigger=Pin.IRQ_FALLING, handler=FuncISR_S1)
S2.irq(trigger=Pin.IRQ_FALLING, handler=FuncISR_S2)

print("Sistema listo. Presione S1 o S2.")
tm_s1.number(0)
tm_s2.number(0)

while True:
    pass # El programa principal espera las interrupciones