import network          # Importa el modulo de red para conexiones WiFi
import socket           # Importa socket para crear el servidor HTTP
import machine          # Importa machine para controlar pines GPIO
import time             # Importa time para manejar retardos

# --- 1. CONFIGURACION DE SALIDAS ---
# Crea una lista con 4 pines GPIO configurados como salida para los LEDs
leds = [machine.Pin(i, machine.Pin.OUT) for i in [18, 18, 19, 20]]  # GPIO 18, 18, 19 y 20

# --- 2. DATOS DE RED ---
ssid = 'S23+ de Angel'      # Nombre de la red WiFi (SSID) a conectar
password = 'angel280731'     # Contrasena de la red WiFi

# --- 3. CONEXION ---
wlan = network.WLAN(network.STA_IF)  # Crea interfaz WLAN en modo estacion (cliente)
wlan.active(True)                     # Activa la interfaz WiFi de la Pico W
wlan.connect(ssid, password)          # Inicia la conexion con las credenciales

# Bucle de espera hasta lograr la conexion WiFi
while not wlan.isconnected():         # Mientras no se establezca la conexion
    time.sleep(1)                     # Espera 1 segundo entre reintentos
    print("Conectando...")            # Muestra mensaje de progreso

print("Conectado. IP:", wlan.ifconfig()[0])  # Imprime la direccion IP asignada

# --- 4. INTERFAZ HTML ---
def web_page():
    # Funcion que genera dinamicamente la pagina HTML con el estado de los 4 LEDs
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
    # Genera dinamicamente los botones de encendido/apagado para cada uno de los 4 LEDs
    for i in range(4):                # Itera sobre los indices 0, 1, 2 y 3
        estado = "ENCENDIDO" if leds[i].value() == 1 else "APAGADO"  # Lee el estado actual del LED
        html += f"<h3>LED {i} (GPIO {i}) - Estado: {estado}</h3>"    # Muestra el titulo con estado
        html += f'<p><a href="/?led{i}=on"><button class="btn-on">ENCENDER</button></a>'   # Boton ON
        html += f' <a href="/?led{i}=off"><button class="btn-off">APAGAR</button></a></p>' # Boton OFF

    html += "</body></html>"  # Cierra las etiquetas HTML del cuerpo y documento
    return html               # Retorna la pagina HTML completa

# --- 5. SERVIDOR ---
s = socket.socket()           # Crea un nuevo socket TCP para el servidor
s.bind(('0.0.0.0', 80))      # Enlaza el socket a todas las interfaces en el puerto 80
s.listen(5)                   # Pone el socket en modo escucha con cola de 5 conexiones

# Bucle principal del servidor web
while True:                           # Bucle infinito que atiende peticiones
    cl, addr = s.accept()             # Espera y acepta una conexion de un cliente
    request = str(cl.recv(1024))      # Recibe la peticion HTTP y la convierte a cadena

    # Logica para identificar cual de los 4 LEDs controlar segun la URL
    for i in range(4):                # Itera sobre los 4 LEDs posibles
        if f"/?led{i}=on" in request:   # Si la URL contiene el parametro de encendido
            leds[i].value(1)            # Enciende el LED correspondiente
        if f"/?led{i}=off" in request:  # Si la URL contiene el parametro de apagado
            leds[i].value(0)            # Apaga el LED correspondiente

    # Envia la respuesta HTTP con las cabeceras y el contenido HTML
    cl.send('HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n')  # Cabeceras HTTP
    cl.sendall(web_page())            # Envia la pagina HTML generada dinamicamente
    cl.close()                        # Cierra la conexion con el cliente
