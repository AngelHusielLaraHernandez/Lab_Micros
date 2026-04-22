import machine, onewire, ds18x20, time

ds_pin = machine.Pin(16)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan()

while True:
    ds_sensor.convert_temp()
    time.sleep_ms(750) 
    
    for rom in roms:
        tempC = ds_sensor.read_temp(rom)
        tempF = (tempC * 9/5) + 32 # Conversión a Fahrenheit
        
        print(f"ROM: {rom}")
        print(f"Temperatura (°C): {tempC:.2f}")
        print(f"Temperatura (°F): {tempF:.2f}\n")
        
    time.sleep(2)
  