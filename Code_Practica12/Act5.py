import network
import socket
import machine
import time

# --- 1. CONFIGURACIÓN DE SALIDAS ---
# Definimos los 4 pines de salida solicitados (GPIO 0, 1, 2 y 3)
leds = [machine.Pin(i, machine.Pin.OUT) for i in [18, 18, 19, 20]]

# --- 2. DATOS DE RED ---
ssid = 'S23+ de Angel'
password = 'angel280731'

# --- 3. CONEXIÓN ---
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    time.sleep(1)
    print("Conectando...")

print("Conectado. IP:", wlan.ifconfig()[0])

# --- 4. INTERFAZ HTML ---
def web_page():
    html = """
    <html>
    <head>
        <title>Control de 4 Salidas</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: Arial; text-align: center; }
            .btn-on { background-color: #4CAF50; color: white; padding: 10px; margin: 5px; text-decoration: none; }
            .btn-off { background-color: #f44336; color: white; padding: 10px; margin: 5px; text-decoration: none; }
        </style>
    </head>
    <body>
        <h1>Panel de Control de 4 LEDs</h1>
        <p>Equipo:Espinoza Matamoros Percival Ulises</p>
        <p>Victor Jaziel Flores Colin</p>
        <p>Angel Husiel Lara Hernandez</p>
        <hr>
    """
    # Genera dinámicamente los botones para los 4 LEDs
    for i in range(4):
        estado = "ENCENDIDO" if leds[i].value() == 1 else "APAGADO"
        html += f"<h3>LED {i} (GPIO {i}) - Estado: {estado}</h3>"
        html += f'<p><a href="/?led{i}=on"><button class="btn-on">ENCENDER</button></a>'
        html += f' <a href="/?led{i}=off"><button class="btn-off">APAGAR</button></a></p>'
    
    html += "</body></html>"
    return html

# --- 5. SERVIDOR ---
s = socket.socket()
s.bind(('0.0.0.0', 80))
s.listen(5)

while True:
    cl, addr = s.accept()
    request = str(cl.recv(1024))
    
    # Lógica para identificar cuál de los 4 LEDs controlar
    for i in range(4):
        if f"/?led{i}=on" in request:
            leds[i].value(1)
        if f"/?led{i}=off" in request:
            leds[i].value(0)
            
    cl.send('HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n')
    cl.sendall(web_page())
    cl.close()