from machine import Pin
import utime
import _thread

# --- Entradas y Salidas ---
S1 = Pin(12, Pin.IN, Pin.PULL_UP) #
S2 = Pin(13, Pin.IN, Pin.PULL_UP) #

led_s1 = Pin(18, Pin.OUT) #
led_s2 = Pin(19, Pin.OUT) #

# Bandera para comunicar la ISR de S2 con el segundo núcleo
flag_s2_presionado = False

# --- HILO SECUNDARIO (Core 1) ---
def nucleo_dos():
    global flag_s2_presionado
    while True:
        # El núcleo 2 está monitoreando si la bandera se activó
        if flag_s2_presionado:
            led_s2.toggle() # Toggle en GPIO19
            print("Núcleo 2: Toggle LED 2")
            flag_s2_presionado = False # Reinicia la bandera
            utime.sleep_ms(300) # Antirrebote
        utime.sleep_ms(10)

# Inicia el Hilo 2
_thread.start_new_thread(nucleo_dos, ())

# --- RUTINAS DE INTERRUPCIÓN ---
def isr_s1(pin):
    # Esta ISR se ejecuta en el Núcleo 1 (Core 0)
    led_s1.toggle() # Toggle en GPIO18
    print("Núcleo 1: Toggle LED 1")
    utime.sleep_ms(300)

def isr_s2(pin):
    # Activa la bandera para que el Núcleo 2 haga el trabajo
    global flag_s2_presionado
    flag_s2_presionado = True

# --- CONFIGURACIÓN DE INTERRUPCIONES ---
S1.irq(trigger=Pin.IRQ_FALLING, handler=isr_s1) #
S2.irq(trigger=Pin.IRQ_FALLING, handler=isr_s2) #

print("Multinúcleo listo. Presione S1 o S2.")

# --- BUCLE DEL HILO PRINCIPAL (Core 0) ---
while True:
    pass