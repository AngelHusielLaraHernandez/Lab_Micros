import network #
import socket #
import machine #
import time #

# Configura el GPIO 2 como salida
led1 = machine.Pin(2, machine.Pin.OUT) #

ssid = 'TU_RED_WIFI' #
password = 'TU_CONTRASEÑA' #

wlan = network.WLAN(network.STA_IF) #
wlan.active(True) #
wlan.connect(ssid, password) #

print("Conectando a Wi-Fi...") #
while not wlan.isconnected(): #
    time.sleep(1) #
    print(".", end="") #

print("\nConectado a Wi-Fi!") #
print("Dirección IP:", wlan.ifconfig()[0]) #

def web_page(): #
    # Página web convertida en un string largo de Python
    html = """
    <html>
    <head><title>Control GPIO 2</title><meta name="viewport" content="width=device-width, initial-scale=1"></head>
    <body>
        <h1>Control de LEDs</h1>
        <p><a href="/?led1=on"><button>LED 1 ON</button></a>
        <a href="/?led1=off"><button>LED 1 OFF</button></a></p>
    </body>
    </html>
    """
    return html #

# Configura el Socket para escuchar en el puerto HTTP estándar (80)
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1] #
s = socket.socket() #
s.bind(addr) #
s.listen(5) #

print("Servidor web escuchando en", addr) #

while True: #
    cl, addr = s.accept() #
    print('Conexión de', addr) #
    request = cl.recv(1024) #
    request = str(request) #
    
    # Evalúa qué botón presionó el usuario analizando el URL
    if "/?led1=on" in request: #
        led1.value(1) #
    if "/?led1=off" in request: #
        led1.value(0) #
        
    response = web_page() #
    
    cl.send('HTTP/1.1 200 OK\n') #
    cl.send('Content-Type: text/html\n') #
    cl.send('Connection: close\n\n') #
    cl.sendall(response.encode('utf-8')) #
    cl.close() #