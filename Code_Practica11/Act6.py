from machine import Pin, PWM
import utime
import _thread
import tm1637
from neopixel import Neopixel

# --- HARDWARE ---
# Semáforos en Neopixel (GPIO 4)
pixels = Neopixel(8, 0, 4, "GRB")
# Autos: LED1(Rojo), LED2(Amarillo), LED3(Verde) -> Índices 0, 1, 2 en Neopixel
# Peatón: LED4(Rojo), LED5(Amarillo), LED6(Verde) -> Índices 3, 4, 5 en Neopixel
R_A = (255, 0, 0); AM_A = (255, 255, 0); V_A = (0, 255, 0)
R_P = (255, 0, 0); AM_P = (255, 255, 0); V_P = (0, 255, 0)
OFF = (0, 0, 0)

# Display Peatonal (GPIO 10 y 11)
tm = tm1637.TM1637(clk=Pin(10), dio=Pin(11))
tm.brightness(3)

# Botón Peatonal (GPIO 12)
boton_peaton = Pin(12, Pin.IN, Pin.PULL_UP)

# Zumbador Peatonal (Asumiendo GPIO 22, salida común en prácticas previas)
buzzer = PWM(Pin(22))
buzzer.duty_u16(0)

# --- VARIABLES DE ESTADO ---
# Semáforo (Lock) para sincronizar los dos núcleos
lock_semaforo = _thread.allocate_lock()
peticion_peaton = False
estado_autos_rojo = False

# --- RUTINA DE INTERRUPCIÓN (Botón Peatonal) ---
def isr_boton(pin):
    global peticion_peaton
    peticion_peaton = True # Activa la bandera de petición
    print("¡Botón presionado! Esperando ciclo en rojo...")

# Configura interrupción
boton_peaton.irq(trigger=Pin.IRQ_FALLING, handler=isr_boton)

def limpiar_neopixel():
    for i in range(6): pixels.set_pixel(i, OFF)
    pixels.show()

# --- HILO SECUNDARIO (Core 1): Rutina Peatonal ---
def rutina_peaton():
    global peticion_peaton
    while True:
        # Espera a que haya una petición Y que los autos estén en rojo
        if peticion_peaton and estado_autos_rojo:
            # Bloquea el núcleo 1 para que no cambie el semáforo a verde
            lock_semaforo.acquire()
            
            print("Iniciando paso peatonal...")
            pixels.set_pixel(3, OFF) # Apaga rojo peatón
            pixels.set_pixel(5, V_P) # Enciende verde peatón
            pixels.show()
            
            # Cuenta regresiva de 10 segundos
            for i in range(10, 0, -1):
                tm.number(i)
                # Sonido intermitente
                buzzer.freq(1000); buzzer.duty_u16(32768)
                utime.sleep_ms(200)
                buzzer.duty_u16(0)
                utime.sleep_ms(800)
                
            # Parpadeo amarillo peatón indicando que se acaba el tiempo
            pixels.set_pixel(5, OFF)
            for _ in range(3):
                pixels.set_pixel(4, AM_P); pixels.show()
                utime.sleep(0.3)
                pixels.set_pixel(4, OFF); pixels.show()
                utime.sleep(0.3)
                
            pixels.set_pixel(3, R_P) # Rojo peatón
            pixels.show()
            tm.write([0,0,0,0]) # Limpia display
            
            # Reinicia variables y libera el semáforo para el Núcleo 1
            peticion_peaton = False
            lock_semaforo.release() 
            
        utime.sleep_ms(100) # Previene saturación del núcleo

# Inicia el Hilo 2
_thread.start_new_thread(rutina_peaton, ())

# --- HILO PRINCIPAL (Core 0): Flujo de Automóviles ---
while True:
    # Intenta adquirir el candado. Si el peatón está pasando, se quedará esperando aquí.
    lock_semaforo.acquire() 
    
    estado_autos_rojo = False
    pixels.set_pixel(0, OFF) # Apaga rojo autos
    pixels.set_pixel(3, R_P) # Asegura rojo peatón
    pixels.set_pixel(2, V_A) # Verde autos
    pixels.show()
    utime.sleep(4)
    
    # Amarillo autos
    pixels.set_pixel(2, OFF)
    pixels.set_pixel(1, AM_A)
    pixels.show()
    utime.sleep(2)
    
    # Rojo autos
    pixels.set_pixel(1, OFF)
    pixels.set_pixel(0, R_A)
    pixels.show()
    estado_autos_rojo = True 
    
    # Libera el candado y espera un instante para que el Núcleo 2 pueda tomar el control si hay petición
    lock_semaforo.release()
    utime.sleep_ms(50) 
    
    # Mantiene en rojo un tiempo si no hay peatones cruzando
    if not peticion_peaton:
        utime.sleep(3)