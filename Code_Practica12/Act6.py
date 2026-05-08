import network, socket, machine, time

# --- CONFIGURACIÓN DE PINES ---
salidas = [machine.Pin(i, machine.Pin.OUT) for i in range(4)]     # GPIO 0 a 3 (Salidas)
entradas = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_UP) for i in (14, 15)] # GPIO 14 y 15 (Botones)
adc = machine.ADC(26)                                             # ADC0 en GPIO 26 (Potenciómetro)
pwm = machine.PWM(machine.Pin(4))                                 # PWM en GPIO 4
pwm.freq(1000)
valor_pwm = 0 # Valor inicial

# --- CONEXIÓN WIFI ---
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('TU_RED', 'TU_CONTRASEÑA')
while not wlan.isconnected(): time.sleep(1)
print("Dashboard disponible en:", wlan.ifconfig()[0])

def web_page():
    # Lectura de los sensores en tiempo real
    estado_d1 = "PRESIONADO" if entradas[0].value() == 0 else "LIBERADO"
    estado_d2 = "PRESIONADO" if entradas[1].value() == 0 else "LIBERADO"
    voltaje_adc = adc.read_u16() * (3.3 / 65535)
    
    html = f"""<html><head><meta name='viewport' content='width=device-width, initial-scale=1'></head>
    <body style="font-family: Arial;">
        <h2>Dashboard IOT - Equipo</h2>
        
        <h3>Lectura de Sensores</h3>
        <p>Botón 1 (GPIO 14): <b>{estado_d1}</b></p>
        <p>Botón 2 (GPIO 15): <b>{estado_d2}</b></p>
        <p>Sensor Analógico (GPIO 26): <b>{voltaje_adc:.2f} Volts</b></p>
        <a href="/"><button>Actualizar Lecturas</button></a><hr>
        
        <h3>Control de Salidas (GPIO 0-3)</h3>"""
    
    for i in range(4):
        estado_actual = "ENCENDIDO" if salidas[i].value() == 1 else "APAGADO"
        html += f'<p>Salida {i} ({estado_actual}): <a href="/?out{i}=on"><button>ON</button></a> <a href="/?out{i}=off"><button>OFF</button></a></p>'
        
    html += f"""<hr><h3>Control PWM (GPIO 4)</h3>
        <p>Intensidad Actual: <b>{valor_pwm} / 100</b></p>
        <a href="/?pwm=0"><button>0%</button></a>
        <a href="/?pwm=25"><button>25%</button></a>
        <a href="/?pwm=50"><button>50%</button></a>
        <a href="/?pwm=100"><button>100%</button></a>
    </body></html>"""
    return html

s = socket.socket()
s.bind(socket.getaddrinfo('0.0.0.0', 80)[0][-1])
s.listen(5)

while True:
    cl, addr = s.accept()
    request = str(cl.recv(1024))
    
    # Evalúa salidas digitales
    for i in range(4):
        if f"/?out{i}=on" in request: salidas[i].value(1)
        if f"/?out{i}=off" in request: salidas[i].value(0)
        
    # Evalúa control PWM (convierte el porcentaje a 16-bits)
    if "/?pwm=0" in request: valor_pwm = 0; pwm.duty_u16(0)
    if "/?pwm=25" in request: valor_pwm = 25; pwm.duty_u16(16383)
    if "/?pwm=50" in request: valor_pwm = 50; pwm.duty_u16(32767)
    if "/?pwm=100" in request: valor_pwm = 100; pwm.duty_u16(65535)
        
    cl.send('HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n')
    cl.sendall(web_page().encode('utf-8'))
    cl.close()