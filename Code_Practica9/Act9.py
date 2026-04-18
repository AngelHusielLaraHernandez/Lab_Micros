import time, machine, onewire, ds18x20, dht, tm1637
from neopixel import Neopixel

# --- CONFIGURACIÓN DE PINES (Basado en Figura 9-16) ---
# Barra Neopixel en GPIO 4
pixels = Neopixel(8, 0, 4, "GRB")

# Displays TM1637
tm_ds = tm1637.TM1637(clk=machine.Pin(0), dio=machine.Pin(1))    # Para el DS18B20
tm_dht = tm1637.TM1637(clk=machine.Pin(10), dio=machine.Pin(11)) # Para el DHT11

# Sensores de Temperatura
ds_sensor = ds18x20.DS18X20(onewire.OneWire(machine.Pin(16)))
dht_sensor = dht.DHT11(machine.Pin(21))

# Colores Neopixel: Verde, Amarillo, Rojo, Apagado
V = (0, 255, 0); A = (255, 255, 0); R = (255, 0, 0); OFF = (0, 0, 0)

def apagar_semaforos():
    for i in range(6): pixels.set_pixel(i, OFF)
    pixels.show()

while True:
    # --- RUTINA DEL SEMÁFORO (Basado en Práctica 3) ---
    apagar_semaforos()
    
    # Estado 1: V1 encendido (Led 0), R2 encendido (Led 5) por 5 segundos
    pixels.set_pixel(0, V); pixels.set_pixel(5, R); pixels.show()
    time.sleep(5)
    
    # Estado 2: V1 intermitente
    for _ in range(5):
        pixels.set_pixel(0, OFF); pixels.show(); time.sleep(0.2)
        pixels.set_pixel(0, V); pixels.show(); time.sleep(0.2)
        
    apagar_semaforos()
    # Estado 3: A1 encendido (Led 1), R2 encendido (Led 5) por 3 segundos
    pixels.set_pixel(1, A); pixels.set_pixel(5, R); pixels.show()
    time.sleep(3)
    
    apagar_semaforos()
    # Estado 4: R1 encendido (Led 2), V2 encendido (Led 3) por 5 segundos
    pixels.set_pixel(2, R); pixels.set_pixel(3, V); pixels.show()
    time.sleep(5)
    
    # Estado 5: V2 intermitente
    for _ in range(5):
        pixels.set_pixel(3, OFF); pixels.show(); time.sleep(0.2)
        pixels.set_pixel(3, V); pixels.show(); time.sleep(0.2)
        
    apagar_semaforos()
    # Estado 6: R1 encendido (Led 2), A2 encendido (Led 4) por 3 segundos
    pixels.set_pixel(2, R); pixels.set_pixel(4, A); pixels.show()
    time.sleep(3)

    # --- DESPLIEGUE DE TEMPERATURAS ---
    try:
        # DS18B20 al TM1637(GP0, GP1)
        roms = ds_sensor.scan()
        ds_sensor.convert_temp()
        time.sleep_ms(750)
        temp_ds = ds_sensor.read_temp(roms[0])
        tm_ds.number(int(temp_ds)) 
        
        # DHT11 al TM1637(GP10, GP11)
        dht_sensor.measure()
        temp_dht = dht_sensor.temperature()
        tm_dht.number(int(temp_dht))
        
    except Exception as e:
        print("Error leyendo sensores:", e)
        
    # Mantiene la temperatura 4 segundos a la vista antes de reiniciar el ciclo del semáforo
    time.sleep(4)