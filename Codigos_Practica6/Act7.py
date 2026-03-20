from machine import ADC, Pin, PWM
import time

# Potenciómetro como entrada analógica en ADC0
potenciometro = ADC(26)

# LEDs como salidas PWM
pwm0 = PWM(Pin(0))
pwm1 = PWM(Pin(1))
pwm0.freq(1000)
pwm1.freq(1000)

MAX_DUTY = 65535

while True:
    # La lectura del ADC da valores entre 0 y 65535 de forma nativa
    lectura_pot = potenciometro.read_u16()
    
    # Asignamos la lectura de voltaje directamente al ciclo de trabajo del PWM
    pwm0.duty_u16(lectura_pot)
    
    # El pin 1 refleja el inverso matemático de la perilla del potenciómetro
    pwm1.duty_u16(MAX_DUTY - lectura_pot)
    
    # Breve pausa para no forzar la lectura del ADC
    time.sleep(0.05)