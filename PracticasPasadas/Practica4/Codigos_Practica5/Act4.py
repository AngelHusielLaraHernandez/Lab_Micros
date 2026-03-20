from machine import Pin, PWM
import time

# --- CONFIGURACIÓN ---
servo = PWM(Pin(21))
servo.freq(50) # 50 Hz = 20 ms de periodo

def set_servo_angulo(angulo):
    min_duty = 1638
    max_duty = 8192
    duty = int(min_duty + (angulo / 180.0) * (max_duty - min_duty))
    servo.duty_u16(duty)

# --- BUCLE PRINCIPAL ---
while True:
    # Barrido ascendente (0° a 180°)
    for angulo in range(0, 181, 5): # Avanza de 5 en 5 grados
        set_servo_angulo(angulo)
        time.sleep(0.05) # Velocidad del barrido
        
    # Barrido descendente (180° a 0°)
    for angulo in range(180, -1, -5):
        set_servo_angulo(angulo)
        time.sleep(0.05)