from machine import Pin, UART
import time

uart = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))

# --- Configuración Motores (Práctica 5) ---
# Motor 1
dir1_m1 = Pin(0, Pin.OUT)
dir2_m1 = Pin(1, Pin.OUT)
en_m1 = Pin(20, Pin.OUT)

# Motor 2
dir1_m2 = Pin(2, Pin.OUT)
dir2_m2 = Pin(3, Pin.OUT)
en_m2 = Pin(19, Pin.OUT)

def control_motor(motor, estado):
    if motor == 1:
        dir1, dir2, en = dir1_m1, dir2_m1, en_m1
    else:
        dir1, dir2, en = dir1_m2, dir2_m2, en_m2
        
    if estado == "PARO":
        en.value(0); dir1.value(0); dir2.value(0)
    elif estado == "HORARIO":
        en.value(1); dir1.value(1); dir2.value(0)
    elif estado == "ANTIHORARIO":
        en.value(1); dir1.value(0); dir2.value(1)

control_motor(1, "PARO")
control_motor(2, "PARO")

while True:
    if uart.any() > 0:
        cmd = uart.read(1).decode('utf-8').upper()
        
        if cmd == 'S': # PARO 
            control_motor(1, "PARO")
            control_motor(2, "PARO")
        elif cmd == 'A': # ADELANTE (Ambos horario) 
            control_motor(1, "HORARIO")
            control_motor(2, "HORARIO")
        elif cmd == 'R' or cmd == 'T': # REVERSA/ATRÁS (Ambos antihorario) 
            control_motor(1, "ANTIHORARIO")
            control_motor(2, "ANTIHORARIO")
        elif cmd == 'D': # DERECHA 
            control_motor(1, "HORARIO")
            control_motor(2, "ANTIHORARIO")
        elif cmd == 'I': # IZQUIERDA 
            control_motor(1, "ANTIHORARIO")
            control_motor(2, "HORARIO")