import network
import socket
import machine
import time

# --- 1. CONFIGURACIÓN DE HARDWARE ---
# Se utiliza el GPIO 2 para el control del LED según las instrucciones
led1 = machine.Pin(18, machine.Pin.OUT)

# --- 2. CONFIGURACIÓN DE RED ---
# Datos obtenidos de tu escaneo previo
ssid = 'S23+ de Angel'
password = 'angel280731'

# --- 3. FUNCIÓN DE LA INTERFAZ (Actividad 3) ---
def web_page():
    # Código HTML que se enviará al navegador
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Servidor Web Pico W</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: Arial; text-align: center; margin: 0px auto; padding-top: 30px; }
            .button { background-color: #4CAF50; border: none; color: white; padding: 16px 40px;
                      text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer; }
            .button2 { background-color: #555555; }
        </style>
    </head>
    <body>
        <h1>Control de Microcomputadoras</h1>
        <p>Estado del LED 1: <strong>Control via Web</strong></p>
        
        <p><a href="/?led1=on"><button class="button">ENCENDER</button></a></p>
        <p><a href="/?led1=off"><button class="button button2">APAGAR</button></a></p>
        
        <hr>
        <h3>Integrantes del Equipo:</h3>
        <p>Angel Husiel Lara Hernandez</p>
        <p>Percival Ulises Espinoza Matamoros</p>
        <p>Victor Jaziel Flores Colin</p>
    </body>
    </html>
    """
    return html

# --- 4. CONEXIÓN A LA RED ---
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Conectando a Wi-Fi...")
# Espera hasta que la conexión sea exitosa
while not wlan.isconnected():
    time.sleep(1)
    print(".", end="")

print("\n¡Conexión establecida!")
print("Dirección IP del servidor:", wlan.ifconfig()[0])

# --- 5. CONFIGURACIÓN DEL SERVIDOR (SOCKET) ---
# Se prepara el socket para escuchar peticiones en el puerto 80 (HTTP)
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(5)

print("Servidor web escuchando en", addr)

# --- 6. BUCLE PRINCIPAL DEL SERVIDOR ---
while True:
    try:
        # Acepta la conexión de un cliente (celular o PC)
        cl, addr = s.accept()
        print('Conexión recibida desde:', addr)
        
        # Recibe la petición del navegador
        request = cl.recv(1024)
        request = str(request)
        
        # Analiza la petición para cambiar el estado del LED
        if "/?led1=on" in request:
            led1.value(1) # Enciende el LED físico
            print("LED ENCENDIDO")
        if "/?led1=off" in request:
            led1.value(0) # Apaga el LED físico
            print("LED APAGADO")
            
        # Genera la respuesta con el código HTML
        response = web_page()
        
        # Envía las cabeceras HTTP estándar y el contenido
        cl.send('HTTP/1.1 200 OK\n')
        cl.send('Content-Type: text/html\n')
        cl.send('Connection: close\n\n')
        cl.sendall(response)
        
        # Cierra la conexión con el cliente actual
        cl.close()
        
    except Exception as e:
        print("Error en el servidor:", e)
        cl.close()