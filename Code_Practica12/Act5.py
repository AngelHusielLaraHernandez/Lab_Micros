import network, socket, machine, time

# Configura las 4 salidas solicitadas (GPIO 0, 1, 2, 3)
leds = [machine.Pin(i, machine.Pin.OUT) for i in range(4)]

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('TU_RED', 'TU_CONTRASEÑA')

while not wlan.isconnected(): time.sleep(1)
print("Conectado en IP:", wlan.ifconfig()[0])

def web_page():
    # Genera la página dinámica con un bucle para los 4 LEDs
    html = "<html><head><meta name='viewport' content='width=device-width, initial-scale=1'></head><body><h1>4 Salidas GPIO</h1>"
    for i in range(4):
        html += f'<p>LED {i} (GPIO {i}): <a href="/?led{i}=on"><button>ON</button></a> '
        html += f'<a href="/?led{i}=off"><button>OFF</button></a></p>'
    html += "</body></html>"
    return html

s = socket.socket()
s.bind(socket.getaddrinfo('0.0.0.0', 80)[0][-1])
s.listen(5)

while True:
    cl, addr = s.accept()
    request = str(cl.recv(1024))
    
    # Revisa si se recibió la instrucción para alguno de los 4 LEDs
    for i in range(4):
        if f"/?led{i}=on" in request: leds[i].value(1)
        if f"/?led{i}=off" in request: leds[i].value(0)
        
    cl.send('HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n')
    cl.sendall(web_page().encode('utf-8'))
    cl.close()