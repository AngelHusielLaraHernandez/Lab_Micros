import network, socket, machine, time

# --- CONFIGURACIÓN DE HARDWARE ---
salidas = [machine.Pin(i, machine.Pin.OUT) for i in range(4)]
entradas = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_UP) for i in (14, 15)]
adc = machine.ADC(26)
pwm = machine.PWM(machine.Pin(4))
pwm.freq(1000)

# --- WIFI ---
ssid = 'S23+ de Angel'
password = 'angel280731'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while not wlan.isconnected(): time.sleep(1)

def web_page():
    # Lectura de sensores en el momento de la petición
    btn1 = "PRESIONADO" if entradas[0].value() == 0 else "LIBERADO"
    btn2 = "PRESIONADO" if entradas[1].value() == 0 else "LIBERADO"
    voltaje = adc.read_u16() * (3.3 / 65535)
    
    html = f"""
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
    <body style="font-family: sans-serif; text-align: center;">
        <h2>Dashboard IOT - Angel y Percival</h2>
        
        <div style="background: #f0f0f0; padding: 10px; border-radius: 10px;">
            <h3>Lecturas de Sensores</h3>
            <p>Boton 1 (GPIO 14): <b>{btn1}</b></p>
            <p>Boton 2 (GPIO 15): <b>{btn2}</b></p>
            <p>Voltaje ADC (GPIO 26): <b>{voltaje:.2f} V</b></p>
            <a href="/"><button>ACTUALIZAR DATOS</button></a>
        </div>

        <h3>Control de Salidas</h3>"""
    
    for i in range(4):
        html += f'<p>Salida {i}: <a href="/?o{i}=1"><button>ON</button></a> <a href="/?o{i}=0"><button>OFF</button></a></p>'
        
    html += """
        <hr>
        <h3>Control PWM (Brillo LED GPIO 4)</h3>
        <a href="/?p=0"><button>0%</button></a>
        <a href="/?p=32000"><button>50%</button></a>
        <a href="/?p=65535"><button>100%</button></a>
    </body></html>"""
    return html

s = socket.socket()
s.bind(('0.0.0.0', 80))
s.listen(5)

while True:
    cl, addr = s.accept()
    request = str(cl.recv(1024))
    
    # Procesamiento de Salidas Digitales
    for i in range(4):
        if f"/?o{i}=1" in request: salidas[i].value(1)
        if f"/?o{i}=0" in request: salidas[i].value(0)
    
    # Procesamiento de PWM (Brillo)
    if "/?p=" in request:
        try:
            # Extrae el valor numérico del URL
            valor = int(request.split("/?p=")[1].split(" ")[0])
            pwm.duty_u16(valor)
        except: pass

    cl.send('HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n')
    cl.sendall(web_page())
    cl.close()