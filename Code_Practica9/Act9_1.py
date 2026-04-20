import time, machine, onewire, ds18x20, dht, tm1637
from neopixel import Neopixel

# --- CONFIGURACIÓN DE HARDWARE ---
pixels = Neopixel(8, 0, 4, "GRB")
tm_ds = tm1637.TM1637(clk=machine.Pin(0), dio=machine.Pin(1))
tm_dht = tm1637.TM1637(clk=machine.Pin(10), dio=machine.Pin(11))
ds_sensor = ds18x20.DS18X20(onewire.OneWire(machine.Pin(16)))
dht_sensor = dht.DHT11(machine.Pin(21))

tm_ds.brightness(3)
tm_dht.brightness(3)

# Colores Neopixel
V = (0, 255, 0); A = (255, 255, 0); R = (255, 0, 0); OFF = (0, 0, 0)

def apagar_semaforos():
    for i in range(6): pixels.set_pixel(i, OFF)
    pixels.show()

while True:
    # --- 1. SECUENCIA DEL SEMÁFORO ---
    apagar_semaforos()
    
    # Estado 1: Verde 1 / Rojo 2
    pixels.set_pixel(0, V); pixels.set_pixel(5, R); pixels.show()
    time.sleep(5)
    
    # Estado 2: Verde 1 intermitente
    for _ in range(5):
        pixels.set_pixel(0, OFF); pixels.show(); time.sleep(0.2)
        pixels.set_pixel(0, V); pixels.show(); time.sleep(0.2)
        
    apagar_semaforos()
    # Estado 3: Amarillo 1 / Rojo 2
    pixels.set_pixel(1, A); pixels.set_pixel(5, R); pixels.show()
    time.sleep(3)
    
    apagar_semaforos()
    # Estado 4: Rojo 1 / Verde 2
    pixels.set_pixel(2, R); pixels.set_pixel(3, V); pixels.show()
    time.sleep(5)
    
    # Estado 5: Verde 2 intermitente
    for _ in range(5):
        pixels.set_pixel(3, OFF); pixels.show(); time.sleep(0.2)
        pixels.set_pixel(3, V); pixels.show(); time.sleep(0.2)
        
    apagar_semaforos()
    # Estado 6: Rojo 1 / Amarillo 2
    pixels.set_pixel(2, R); pixels.set_pixel(4, A); pixels.show()
    time.sleep(3)

    # --- 2. LECTURA Y DESPLIEGUE DE SENSORES ---
    try:
        # DS18B20
        roms = ds_sensor.scan()
        if roms:
            ds_sensor.convert_temp()
            time.sleep_ms(750) 
            temp_ds = ds_sensor.read_temp(roms[0])
            tm_ds.number(int(temp_ds)) 
        
        # DHT11
        dht_sensor.measure()
        temp_dht = dht_sensor.temperature()
        tm_dht.number(int(temp_dht))
        
    except OSError:
        pass # Evita detener el bucle infinito del semáforo si hay ruido
        
    time.sleep(3) # Pausa antes de reiniciar todo el ciclo