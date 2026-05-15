import network, socket, machine, time
import pcf8574 # Librería necesaria de la Práctica 10

# --- 1. CONFIGURACIÓN DE HARDWARE FÍSICO ---
# 3 LEDs normales en salidas digitales
pines_leds = [18, 19, 20]
leds = [machine.Pin(p, machine.Pin.OUT) for p in pines_leds]

# 2 Botones en entradas digitales con Pull-Up
botones = [machine.Pin(p, machine.Pin.IN, machine.Pin.PULL_UP) for p in (12, 13)]

# Zumbador como salida PWM
buzzer = machine.PWM(machine.Pin(17))
buzzer.freq(1000)
buzzer.duty_u16(0)
volumen_actual = 0

# Bus I2C y Módulo PCF8574 para el LED RGB
# Se asume Rojo=P0, Verde=P1, Azul=P2 del PCF8574
i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8))
pcf = pcf8574.PCF8574(i2c, 0x39) 
pcf.port = 0xFF # Apaga todos los pines del expansor inicialmente (lógica inversa común en RGBs)
color_rgb = "APAGADO"

# --- 2. CONFIGURACIÓN WI-FI ---
ssid = 'S23+ de Angel'
password = 'angel280731'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Iniciando conexión Wi-Fi...")
while not wlan.isconnected(): 
    time.sleep(1)

print("Dashboard listo en la IP:", wlan.ifconfig()[0])

# --- 3. INTERFAZ WEB DINÁMICA ---
def web_page():
    # Lectura del estado físico de los botones (0 = Presionado, 1 = Liberado)
    estado_s1 = "PRESIONADO" if botones[0].value() == 0 else "LIBERADO"
    estado_s2 = "PRESIONADO" if botones[1].value() == 0 else "LIBERADO"
    
    html = f"""
    <!DOCTYPE html>
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{ font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f9; margin: 0; padding: 20px; }}
        .tarjeta {{ background: white; padding: 20px; border-radius: 12px; margin: 15px auto; width: 90%; max-width: 450px; box-shadow: 0px 4px 8px rgba(0,0,0,0.1); }}
        button {{ padding: 12px 20px; font-size: 16px; margin: 5px; cursor: pointer; border-radius: 6px; border: none; font-weight: bold; color: white; }}
        .btn-on {{ background-color: #4CAF50; }} .btn-off {{ background-color: #f44336; }}
        .btn-azul {{ background-color: #2196F3; }} .btn-gris {{ background-color: #607D8B; }}
    </style>
    </head>
    <body>
        <h2>Laboratorio de Redes y Micros</h2>
        <p>Equipo:Espinoza Matamoros Percival Ulises</p>
        <p>Victor Jaziel Flores Colin</p>
        <p>Angel Husiel Lara Hernandez</p>
        
        <div class="tarjeta">
            <h3 style="color: #607D8B;">Sensores (Entradas)</h3>
            <p>Boton S1 (GPIO 12): <b>{estado_s1}</b></p>
            <p>Boton S2 (GPIO 13): <b>{estado_s2}</b></p>
            <a href="/"><button class="btn-azul">ACTUALIZAR ESTADO</button></a>
        </div>

        <div class="tarjeta">
            <h3 style="color: #4CAF50;">Control de LEDs (GPIO 18, 19, 20)</h3>"""
    
    # Crea los botones web para los 3 LEDs
    for i in range(3):
        estado_led = "ON" if leds[i].value() == 1 else "OFF"
        color_texto = "green" if estado_led == "ON" else "red"
        html += f'<p>LED {i+1} (Pin {pines_leds[i]}): <b style="color: {color_texto};">{estado_led}</b><br>'
        html += f'<a href="/?led{i}=1"><button class="btn-on">ON</button></a> '
        html += f'<a href="/?led{i}=0"><button class="btn-off">OFF</button></a></p>'
        
    html += f"""
        </div>
        <div class="tarjeta">
            <h3 style="color: #FF9800;">Control Neopixel/RGB (vía PCF8574)</h3>
            <p>Color actual: <b>{color_rgb}</b></p>
            <a href="/?rgb=rojo"><button style="background: #F44336; border: none; padding: 10px; color: white;">Rojo</button></a>
            <a href="/?rgb=verde"><button style="background: #4CAF50; border: none; padding: 10px; color: white;">Verde</button></a>
            <a href="/?rgb=azul"><button style="background: #2196F3; border: none; padding: 10px; color: white;">Azul</button></a>
            <a href="/?rgb=apagado"><button class="btn-gris">Apagar</button></a>
        </div>

        <div class="tarjeta">
            <h3 style="color: #9C27B0;">Alarma Zumbador (PWM 22)</h3>
            <p>Nivel de volumen: <b>{volumen_actual}%</b></p>
            <a href="/?pwm=0"><button class="btn-gris">0%</button></a>
            <a href="/?pwm=16383"><button class="btn-azul">25%</button></a>
            <a href="/?pwm=65535"><button class="btn-on">100%</button></a>
        </div>
    </body></html>"""
    return html

# --- 4. SERVIDOR SOCKET ---
s = socket.socket()
s.bind(('0.0.0.0', 80))
s.listen(5)

while True:
    try:
        cl, addr = s.accept()
        request = str(cl.recv(1024))
        
        # 1. Evalúa control de LEDs simples
        for i in range(3):
            if f"/?led{i}=1" in request: leds[i].value(1)
            if f"/?led{i}=0" in request: leds[i].value(0)
            
        # 2. Evalúa control del Zumbador (PWM)
        if "/?pwm=" in request:
            try:
                val_pwm = int(request.split("/?pwm=")[1].split(" ")[0])
                buzzer.duty_u16(val_pwm)
                if val_pwm == 0: volumen_actual = 0
                elif val_pwm == 16383: volumen_actual = 25
                elif val_pwm == 65535: volumen_actual = 100
            except: pass
            
        # 3. Evalúa control del LED RGB mediante el I2C (PCF8574)
        if "/?rgb=" in request:
            # Apaga los 3 canales primero poniendo los bits en 1 (0xFF = 11111111)
            # Nota: Muchos módulos RGB con PCF8574 encienden con 0 y apagan con 1
            pcf.port = 0xFF 
            if "rojo" in request:
                pcf.pin(0, 0) # Enciende canal Rojo (P0)
                color_rgb = "ROJO"
            elif "verde" in request:
                pcf.pin(1, 0) # Enciende canal Verde (P1)
                color_rgb = "VERDE"
            elif "azul" in request:
                pcf.pin(2, 0) # Enciende canal Azul (P2)
                color_rgb = "AZUL"
            elif "apagado" in request:
                color_rgb = "APAGADO"

        # Envía la página actualizada al navegador
        cl.send('HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n')
        cl.sendall(web_page().encode('utf-8'))
        cl.close()
        
    except Exception as e:
        print("Error en conexión:", e)
        cl.close()