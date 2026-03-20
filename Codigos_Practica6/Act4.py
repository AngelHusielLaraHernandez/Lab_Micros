from machine import ADC
import time

sensor_interno = ADC(4) # Sensor nativo del chip
sensor_tmp36 = ADC(28)  # TMP36 en el GPIO28

while True:
    # --- SENSOR INTERNO ---
    v_int = sensor_interno.read_u16() * (3.3 / 65535)
    temp_c_int = 27 - (v_int - 0.706) / 0.001721
    temp_f_int = (temp_c_int * 9/5) + 32
    
    # --- SENSOR TMP36 ---
    # El TMP36 da 10mV por cada 1°C y tiene un offset (desplazamiento) de 500mV (0.5V) a 0°C
    v_tmp = sensor_tmp36.read_u16() * (3.3 / 65535)
    temp_c_tmp = (v_tmp - 0.5) * 100
    temp_f_tmp = (temp_c_tmp * 9/5) + 32
    
    # --- DESPLIEGUE ---
    print(f"Temperatura interna = {temp_c_int:.1f}°C; {temp_f_int:.1f}°F")
    print(f"Temperatura TMP36 = {temp_c_tmp:.1f}°C; {temp_f_tmp:.1f}°F")
    
    if temp_c_int > temp_c_tmp:
        print("El sensor interno tiene el valor mayor de temperatura.\n")
    elif temp_c_tmp > temp_c_int:
        print("El sensor TMP36 tiene el valor mayor de temperatura.\n")
    else:
        print("Ambos sensores registran lo mismo.\n")
        
    time.sleep(2)