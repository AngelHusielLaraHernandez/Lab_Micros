import machine, onewire, ds18x20, time

ds_pin = machine.Pin(16)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan()

while True:
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    
    for rom in roms:
        # Lectura de la temperatura en Celsius
        tempC = ds_sensor.read_temp(rom)
        
        # Ecuación de conversión a Fahrenheit
        tempF = (tempC * 9/5) + 32
        
        print(rom)
        print('temperature (°C):', "{:.2f}".format(tempC))
        print('temperature (°F):', "{:.2f}".format(tempF))
        print()
        
    time.sleep(2)