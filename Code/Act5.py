from machine import Pin, PWM
import time

# Configura salida PWM en el GPIO1
pwm = PWM(Pin(1))
# Asigna la frecuencia a 1 kHz
pwm.freq(1000)

while True:
    # Aumenta el ciclo de trabajo gradualmente
    for duty in range(0, 65535, 500):
        pwm.duty_u16(duty) # Aplica la señal PWM
        time.sleep(0.05)   # Retardo para notar el efecto visual
        
    # Apaga por completo la señal PWM
    pwm.duty_u16(0)
    time.sleep(2)