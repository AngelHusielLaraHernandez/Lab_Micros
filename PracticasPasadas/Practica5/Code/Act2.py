from machine import Pin, PWM
import time

# --- ENTRADAS ---
sw1_1 = Pin(10, Pin.IN)
sw1_2 = Pin(9, Pin.IN)
sw1_3 = Pin(8, Pin.IN)

# --- SALIDAS ---
bobinas = [Pin(7, Pin.OUT), Pin(6, Pin.OUT), Pin(5, Pin.OUT), Pin(4, Pin.OUT)]
buzzer = PWM(Pin(22))
buzzer.duty_u16(0)

# --- CONFIGURACIÓN DEL MOTOR ---
# Secuencia de pasos completos (A, B, C, D)
secuencia = [(1,1,0,0), (0,1,1,0), (0,0,1,1), (1,0,0,1)]
PASOS_POR_REV = 512  # Ajusta a 2048 si usas un motor 28BYJ-48 con reducción completa
TIEMPO_PASO = 0.005  # 5 ms de velocidad por paso

def leer_entradas():
    return (sw1_1.value(), sw1_2.value(), sw1_3.value())

def apagar_motor():
    for b in bobinas: b.value(0)

def dar_paso(idx):
    for i in range(4): bobinas[i].value(secuencia[idx][i])

def sonar_zumbador():
    buzzer.freq(1000)
    buzzer.duty_u16(32768)
    time.sleep(0.3)
    buzzer.duty_u16(0)

def girar_grados(grados, sentido, sonar=False):
    pasos = int((grados / 360.0) * PASOS_POR_REV)
    idx = 0
    for _ in range(pasos):
        if leer_entradas() not in [(0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]: break
        dar_paso(idx)
        time.sleep(TIEMPO_PASO)
        idx = (idx + 1) if sentido == "HORARIO" else (idx - 1)
        idx %= 4
    apagar_motor()
    if sonar: sonar_zumbador()

def girar_revoluciones(revs, sentido, sonar_por_rev=True, condicion_salida=None):
    for _ in range(revs):
        if leer_entradas() != condicion_salida: break
        girar_grados(360, sentido, sonar=False)
        girar_grados(360, sentido, sonar=False)
        girar_grados(360, sentido, sonar=False)
        girar_grados(360, sentido, sonar=False)
        if sonar_por_rev: sonar_zumbador()

idx_continuo = 0

while True:
    estado = leer_entradas()
    
    if estado == (0, 0, 0): # PARO
        apagar_motor()
        
    elif estado == (0, 0, 1): # HORARIO CONTINUO
        dar_paso(idx_continuo)
        time.sleep(TIEMPO_PASO)
        idx_continuo = (idx_continuo + 1) % 4
        
    elif estado == (0, 1, 0): # ANTIHORARIO CONTINUO
        dar_paso(idx_continuo)
        time.sleep(TIEMPO_PASO)
        idx_continuo = (idx_continuo - 1) % 4
        
    elif estado == (0, 1, 1): # 90° HORARIO cada 2 seg
        girar_grados(90, "HORARIO")
        time.sleep(2)
        
    elif estado == (1, 0, 0): # 180° ANTIHORARIO cada 3 seg
        girar_grados(360, "ANTIHORARIO")
        girar_grados(360, "ANTIHORARIO")
        time.sleep(3)
        
    elif estado == (1, 0, 1): # 360° HORARIO cada 4 seg + Zumbador
        girar_grados(360, "HORARIO")
        girar_grados(360, "HORARIO")
        girar_grados(360, "HORARIO")
        girar_grados(360, "HORARIO", sonar=True)
        time.sleep(4)
        
    elif estado == (1, 1, 0): # 5 REVS HORARIO + Zumbador x Rev
        girar_revoluciones(5, "HORARIO", True, (1, 1, 0))
        while leer_entradas() == (1, 1, 0): time.sleep(0.1) # Evita bucle infinito si no sueltas
            
    elif estado == (1, 1, 1): # 10 REVS ANTIHORARIO + Zumbador x Rev
        girar_revoluciones(10, "ANTIHORARIO", True, (1, 1, 1))
        while leer_entradas() == (1, 1, 1): time.sleep(0.1)

