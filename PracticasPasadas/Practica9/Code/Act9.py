import time, machine, onewire, ds18x20, dht, tm1637
from neopixel import Neopixel

# --- 1. CONFIGURACIÓN DE HARDWARE ---
# Neopixel en GPIO 4 (Semáforo)
pixels = Neopixel(8, 0, 4, "GRB")

# Un solo Display TM1637 (CLK=0, DIO=1)
tm = tm1637.TM1637(clk=machine.Pin(0), dio=machine.Pin(1))
tm.brightness(3) # Brillo nivel 3

# Sensores
ds_sensor = ds18x20.DS18X20(onewire.OneWire(machine.Pin(16)))
dht_sensor = dht.DHT11(machine.Pin(21))

# Botón selector en GPIO 12 con Pull-Up interno
boton = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)

# --- 2. VARIABLES DE CONTROL ---
# modo_sensor 0: Muestra DS18B20 | modo_sensor 1: Muestra DHT11
modo_sensor = 0 
V = (0, 255, 0); A = (255, 255, 0); R = (255, 0, 0); OFF = (0, 0, 0)

# Interrupción para cambiar el modo del display al presionar el botón
def cambiar_modo(pin):
    global modo_sensor
    modo_sensor = 1 if modo_sensor == 0 else 0
    print("Modo cambiado. Mostrando sensor:", "DHT11" if modo_sensor == 1 else "DS18B20")

# Configura la interrupción por flanco de bajada (al presionar)
boton.irq(trigger=machine.Pin.IRQ_FALLING, handler=cambiar_modo)

def apagar_semaforos():
    for i in range(6): pixels.set_pixel(i, OFF)
    pixels.show()

# --- 3. BUCLE PRINCIPAL ---
while True:
    # --- FASE A: SECUENCIA DE SEMÁFOROS (Núcleo 1) ---
    apagar_semaforos()
    # Verde 1 / Rojo 2 (5 seg)
    pixels.set_pixel(0, V); pixels.set_pixel(5, R); pixels.show()
    time.sleep(5)
    
    # Verde 1 intermitente
    for _ in range(5):
        pixels.set_pixel(0, OFF); pixels.show(); time.sleep(0.2)
        pixels.set_pixel(0, V); pixels.show(); time.sleep(0.2)
        
    apagar_semaforos()
    # Amarillo 1 / Rojo 2 (3 seg)
    pixels.set_pixel(1, A); pixels.set_pixel(5, R); pixels.show()
    time.sleep(3)
    
    apagar_semaforos()
    # Rojo 1 / Verde 2 (5 seg)
    pixels.set_pixel(2, R); pixels.set_pixel(3, V); pixels.show()
    time.sleep(5)
    
    # Verde 2 intermitente
    for _ in range(5):
        pixels.set_pixel(3, OFF); pixels.show(); time.sleep(0.2)
        pixels.set_pixel(3, V); pixels.show(); time.sleep(0.2)
        
    apagar_semaforos()
    # Rojo 1 / Amarillo 2 (3 seg)
    pixels.set_pixel(2, R); pixels.set_pixel(4, A); pixels.show()
    time.sleep(3)
    apagar_semaforos()

    # --- FASE B: MOSTRAR TEMPERATURA (10 Segundos de lectura interactiva) ---
    print("Iniciando fase de visualización de sensores...")
    inicio_fase = time.time()
    
    while (time.time() - inicio_fase) < 10:
        try:
            if modo_sensor == 0:
                # Lectura DS18B20 (Requiere 750ms)
                roms = ds_sensor.scan()
                if roms:
                    ds_sensor.convert_temp()
                    time.sleep_ms(750) 
                    temp = ds_sensor.read_temp(roms[0])
                    print(f"DS18: {temp}")
                    tm.show("DS ") # Identificador visual rápido
                    time.sleep(0.5)
                    tm.number(int(temp))
            else:
                # Lectura DHT11 (Requiere muestreo lento)
                dht_sensor.measure()
                temp = dht_sensor.temperature()
                print(f"dh11: {temp}")
                tm.show("DH ") # Identificador visual rápido
                time.sleep(0.5)
                tm.number(int(temp))
                
        except Exception:
            tm.show("ERR ") # Mostrar error en display si falla la lectura
            
        time.sleep(1) # Pausa entre actualizaciones de display
        
    tm.write([0, 0, 0, 0]) # Limpia display antes de reiniciar semáforo