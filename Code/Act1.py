from machine import Pin
import time

# --- 1. CONFIGURACIÓN DE ENTRADAS ---
sw1_1 = Pin(10, Pin.IN)
sw1_2 = Pin(9, Pin.IN)
sw1_3 = Pin(8, Pin.IN)

# --- 2. CONFIGURACIÓN DE SALIDAS (Motores) ---
# Motor 1
dir1_m1 = Pin(0, Pin.OUT)
dir2_m1 = Pin(1, Pin.OUT)
en_m1 = Pin(20, Pin.OUT)

# Motor 2
dir1_m2 = Pin(2, Pin.OUT)
dir2_m2 = Pin(3, Pin.OUT)
en_m2 = Pin(19, Pin.OUT)

# --- 3. FUNCIONES AUXILIARES ---
def control_motor(motor, estado):
    """Controla el giro de un motor específico"""
    if motor == 1:
        dir1, dir2, en = dir1_m1, dir2_m1, en_m1
    else:
        dir1, dir2, en = dir1_m2, dir2_m2, en_m2
        
    if estado == "PARO":
        en.value(0)
        dir1.value(0)
        dir2.value(0)
    elif estado == "HORARIO":
        en.value(1)
        dir1.value(1)
        dir2.value(0)
    elif estado == "ANTIHORARIO":
        en.value(1)
        dir1.value(0)
        dir2.value(1)

def leer_entradas():
    return (sw1_1.value(), sw1_2.value(), sw1_3.value())

# --- 4. BUCLE PRINCIPAL ---
while True:
    entradas = leer_entradas()
    
    # Lógica basada en la Tabla 5-2
    if entradas == (0, 0, 0):
        control_motor(1, "PARO")
        control_motor(2, "PARO")
    elif entradas == (0, 0, 1):
        control_motor(1, "ANTIHORARIO")
        control_motor(2, "PARO")
    elif entradas == (0, 1, 0):
        control_motor(1, "PARO")
        control_motor(2, "HORARIO")
    elif entradas == (0, 1, 1):
        control_motor(1, "ANTIHORARIO")
        control_motor(2, "HORARIO")
    elif entradas == (1, 0, 0):
        control_motor(1, "HORARIO")
        control_motor(2, "HORARIO")
    elif entradas == (1, 0, 1):
        control_motor(1, "HORARIO")
        control_motor(2, "HORARIO")
    elif entradas == (1, 1, 0):
        control_motor(1, "HORARIO")
        control_motor(2, "ANTIHORARIO")
    elif entradas == (1, 1, 1):
        control_motor(1, "PARO")
        control_motor(2, "PARO")
        
    time.sleep(0.05) # Estabilizador de lecturas
