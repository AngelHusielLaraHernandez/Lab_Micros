from machine import Pin, PWM
import time


pwm = PWM(Pin(1))

pwm.freq(1000)

while True:
   
    for duty in range(0, 65535, 500):
        pwm.duty_u16(duty) 
        time.sleep(0.05)   
        
    
    pwm.duty_u16(0)
    time.sleep(2)