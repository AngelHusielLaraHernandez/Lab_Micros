import machine
import utime

# Lista de pines configurados como salidas
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(8)]

while True:
    # Contar de 0 a 255 (8 bits)
    for contador in range(256):
        # Recorrer los 8 bits del número actual
        for bit in range(8):
            # Extraemos el valor del bit en la posición actual (0 o 1)
            # Desplazamos el contador a la derecha 'bit' veces y hacemos AND con 1
            estado_bit = (contador >> bit) & 1
            
            # Asignamos ese estado al LED correspondiente
            leds[bit].value(estado_bit)
            
        # Retardo de 50 ms entre cada número
        utime.sleep_ms(50)