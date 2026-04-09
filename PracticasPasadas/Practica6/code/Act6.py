from machine import Pin, PWM
import time

pwm0 = PWM(Pin(0))
pwm1 = PWM(Pin(1))

pwm0.freq(1000)
pwm1.freq(1000)

MAX_DUTY = 65535
PASO = 1000 # Escala de incremento para hacerlo fluido

while True:
    # Fase 1: PWM0 aumenta brillo, PWM1 disminuye brillo
    for duty in range(0, MAX_DUTY, PASO):
        pwm0.duty_u16(duty)
        pwm1.duty_u16(MAX_DUTY - duty) # Se le asigna la diferencia para hacer el inverso
        time.sleep(0.02)
        
    # Fase 2: PWM0 disminuye brillo, PWM1 aumenta brillo
    for duty in range(MAX_DUTY, 0, -PASO):
        pwm0.duty_u16(duty)
        pwm1.duty_u16(MAX_DUTY - duty)
        time.sleep(0.02)