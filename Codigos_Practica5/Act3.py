from machine import Pin, PWM
import time

# --- ENTRADAS ---
S2 = Pin(12, Pin.IN, Pin.PULL_DOWN)
S1 = Pin(11, Pin.IN, Pin.PULL_UP)
sw1_1 = Pin(10, Pin.IN)
sw1_2 = Pin(9, Pin.IN)
sw1_3 = Pin(8, Pin.IN)

# --- SALIDA PWM (Servo) ---
servo = PWM(Pin(21))
servo.freq(50) # El estándar para servomotores es un periodo de 20ms (50Hz)

def leer_entradas():
    return (S2.value(), S1.value(), sw1_1.value(), sw1_2.value(), sw1_3.value())

def set_servo_angulo(angulo):
    """
    Convierte un ángulo de 0 a 180 en el ciclo de trabajo equivalente.
    0.5ms (1638 duty) equivale a 0°.
    2.5ms (8192 duty) equivale a 180°.
    """
    min_duty = 1638
    max_duty = 8192
    duty = int(min_duty + (angulo / 180.0) * (max_duty - min_duty))
    servo.duty_u16(duty)

while True:
    estado = leer_entradas()
    
    if estado == (0, 0, 0, 0, 0):
        servo.duty_u16(0) # PARO (Apaga la señal PWM, liberando el torque del servo)
    elif estado == (0, 0, 0, 0, 1):
        set_servo_angulo(0)
    elif estado == (0, 0, 0, 1, 0):
        set_servo_angulo(45)
    elif estado == (0, 0, 0, 1, 1):
        set_servo_angulo(90)
    elif estado == (0, 0, 1, 0, 0):
        set_servo_angulo(135)
    elif estado == (0, 0, 1, 0, 1):
        set_servo_angulo(180)
        
    time.sleep(0.1)