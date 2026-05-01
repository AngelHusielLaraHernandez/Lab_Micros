import machine, onewire, ds18x20, time

# Configura el bus 1-Wire en el pin GPIO 16
ds_pin = machine.Pin(16)

# Crea la instancia del sensor vinculándolo al bus 1-Wire
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

# Escanea el bus para encontrar la dirección MAC/ROM del sensor conectado
roms = ds_sensor.scan()
print("Sensor detectado", roms)

while True:
    # Envía la orden para que el sensor inicie la conversión de temperatura
    ds_sensor.convert_temp()
    
    # El manual técnico del DS18B20 exige al menos 750ms para completar la conversión a 12 bits
    time.sleep_ms(750)
    
    # Itera sobre los sensores encontrados en el bus
    for rom in roms:
        print(rom) # Imprime el código ROM del sensor
        # Recupera el valor convertido de temperatura
        tempC = ds_sensor.read_temp(rom)
        # Lo muestra formateado a 2 decimales
        print('temperatura (C):', "{:.2f}".format(tempC))
        print()
        
    time.sleep(2) # Pausa antes de la siguiente lectura
    