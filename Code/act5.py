from machine import Pin, PWM
import time

# --- 1. CONFIGURACIÓN DE ENTRADAS ---
S2 = Pin(12, Pin.IN, Pin.PULL_DOWN)
S1 = Pin(11, Pin.IN, Pin.PULL_UP)
SW1_1 = Pin(10, Pin.IN)
SW1_2 = Pin(9, Pin.IN)
SW1_3 = Pin(8, Pin.IN)

# --- 2. CONFIGURACIÓN DE SALIDAS ---
# Creamos una lista con los 8 LEDs ordenados desde el GPIO 0 (LED 0) hasta el GPIO 7 (LED 7)
pines_leds = [Pin(i, Pin.OUT) for i in range(8)]

# Zumbador en el GPIO 22 usando PWM para poder hacer tonos y pitidos
buzzer = PWM(Pin(22))
buzzer.duty_u16(0) # Inicia silenciado

# --- 3. FUNCIONES AUXILIARES ---
def leer_entradas():
    """Lee el estado de todos los botones y switches y devuelve una tupla"""
    return (S2.value(), S1.value(), SW1_3.value(), SW1_2.value(), SW1_1.value())

def set_leds(valor_binario):
    """
    Recibe un número de 8 bits y enciende/apaga los LEDs en consecuencia.
    Ejemplo: 0b10000001 encenderá el LED 7 y el LED 0.
    """
    for i in range(8):
        # Extrae el bit correspondiente a la posición 'i' y se lo asigna al LED
        pines_leds[i].value((valor_binario >> i) & 1)

def beep(estado):
    """Enciende o apaga un pitido simple (1kHz)"""
    if estado:
        buzzer.freq(1000)
        buzzer.duty_u16(32768) # 50% de volumen
    else:
        buzzer.duty_u16(0)     # 0% de volumen (silencio)

def tocar_nota(frecuencia):
    """Reproduce una frecuencia musical específica"""
    buzzer.freq(frecuencia)
    buzzer.duty_u16(32768)


# --- 4. BUCLE PRINCIPAL ---
while True:
    entradas = leer_entradas()
    
    # 0 1 0 0 0: Todos apagados
    if entradas == (0, 1, 0, 0, 0):
        print(entradas)
        set_leds(0b00000000)
        beep(0)
        time.sleep(0.1)
        
    # 0 1 0 0 1: Todos encendidos
    elif entradas == (0, 1, 0, 0, 1):
        print(entradas)
        set_leds(0b11111111)
        beep(0)
        time.sleep(0.1)
        
    # 0 1 0 1 0: Desplazamiento a la derecha (LED 7 a LED 0)
    elif entradas == (0, 1, 0, 1, 0):
        print(entradas)
        set_leds(0b10101010)
            
    # 0 1 0 1 1: Desplazamiento a la izquierda (LED 0 a LED 7)
    elif entradas == (0, 1, 0, 1, 1):
        print(entradas)
        set_leds(0b01010101)
            
    # 0 1 1 0 0: Desplazamiento a la derecha con pitido al final
    elif entradas == (0, 1, 1, 0, 0):
        print(entradas)
        for i in range(7, -1, -1):
            if leer_entradas() != (0, 1, 1, 0, 0): break
            set_leds(1 << i)
            beep(0)
            time.sleep(0.15)
        # Al terminar la secuencia, apaga los LEDs y suena el buzzer un instante
        if leer_entradas() == (0, 1, 1, 0, 0):
            set_leds(0b00000000)
            beep(1)
            time.sleep(0.2)
            beep(0)
            
    # 0 1 1 0 1: Secuencia de extremos hacia el centro
    elif entradas == (0, 1, 1, 0, 1):
        print(entradas)
        for i in range(7, -1, -1): # Cuenta de 7 bajando hasta 0
            if leer_entradas() != (0, 1, 1, 0, 1): break # Rompe si cambias un switch
            set_leds(1 << i)
            if i ==6 :
                beep(1)
            else:
                beep (0)
                
            time.sleep(0.15)
            
    # 0 1 1 1 0: Secuencia del centro hacia los extremos
    elif entradas == (0, 1, 1, 1, 0):
        print(entradas)
        secuencia = [0b10000000, 0b01000000, 0b00100000, 0b00010000,0b00001000,0b00000100,0b00000010,0b00000001]

        for val in secuencia:
            beep(0)
            if leer_entradas() != (0, 1, 1, 1, 0): break
            set_leds(val)
            time.sleep(0.2)
        secuencia.reverse()
        for val in secuencia:
            if leer_entradas() != (0, 1, 1, 1, 0): break
            set_leds(val)
            time.sleep(0.2)
            
            if val == 128:
                beep(1)
                time.sleep(0.2)
            
    # 0 1 1 1 1: Auto (extremos a centro y viceversa) con pitido al llegar a extremos
    elif entradas == (0, 1, 1, 1, 1):
        print(entradas)
        secuencia = [0b10000001, 0b01000010, 0b00100100, 0b00011000, 0b00100100, 0b01000010, 0b10000001]
        for i, val in enumerate(secuencia):
            if leer_entradas() != (0, 1, 1, 1, 1): break
            set_leds(val)
            # Suena solo en el último paso de la secuencia (cuando llega a los extremos)
            if i == len(secuencia) - 1:
                beep(1)
            else:
                beep(0)
            time.sleep(0.15)
        beep(0) # Apaga por seguridad al salir del for
            
    # 0 0 1 1 1: Contador ascendente (0 a 9) en los LEDs 3, 4, 5 y 6
    elif entradas == (0, 0, 1, 1, 1):
        print(entradas)
        for num in range(10):
            if leer_entradas() != (0, 0, 1, 1, 1): break
            # Desplazamos el número 3 bits a la izquierda para que empiece en el LED 3
            # Ejemplo: el número 1 (0001) se convierte en 8 (00001000), encendiendo GPIO 3.
            set_leds(num << 3)
            time.sleep(0.5)
            
    # 1 1 1 1 1: Contador descendente (9 a 0) en los LEDs 3, 4, 5 y 6
    elif entradas == (1, 1, 1, 1, 1):
        print(entradas)
        for num in range(9, -1, -1):
            if leer_entradas() != (1, 1, 1, 1, 1): break
            set_leds(num << 3)
            time.sleep(0.5)
            
    # 1 0 1 1 1: Notas musicales
    elif entradas == (1, 0, 1, 1, 1):
        print(entradas)
        set_leds(0) # Apagamos los LEDs para esta función
        notas = [261, 293, 329, 349, 392, 440, 493, 523] # Do, Re, Mi, Fa, Sol, La, Si, Do
        for nota in notas:
            if leer_entradas() != (1, 0, 1, 1, 1): break
            tocar_nota(nota)
            time.sleep(0.4)
        beep(0) # Silencia al terminar la escala
        time.sleep(0.2) # Pausa antes de repetir
        
    # Estado por defecto: Todo apagado
    else:
        print(entradas)
        set_leds(0)
        beep(0)
        time.sleep(0.1)

