import network          # Importa el modulo de red para manejar conexiones WiFi
import socket           # Importa el modulo socket para crear el servidor web
import machine          # Importa machine para controlar los pines GPIO
import time             # Importa time para manejar retardos y pausas

# --- 1. CONFIGURACION DE HARDWARE ---
# Se configura el pin GPIO 18 como salida digital para controlar el LED
led1 = machine.Pin(18, machine.Pin.OUT) # Crea un objeto Pin en GPIO18 como salida

# --- 2. CONFIGURACION DE RED ---
# Se definen las credenciales de la red WiFi a la que se conectara la Pico W
ssid = 'S23+ de Angel'      # Nombre de la red WiFi (SSID)
password = 'angel280731'     # Contrasena de la red WiFi

# --- 3. FUNCION DE LA INTERFAZ WEB (Actividad 3) ---
def web_page():
    # Funcion que genera el codigo HTML de la pagina web de control
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
    return html  # Retorna la cadena HTML completa al servidor

# --- 4. CONEXION A LA RED ---
wlan = network.WLAN(network.STA_IF)  # Crea una interfaz WLAN en modo estacion (cliente)
wlan.active(True)                     # Activa la interfaz de red inalambrica
wlan.connect(ssid, password)          # Inicia la conexion a la red WiFi con las credenciales

print("Conectando a Wi-Fi...")        # Muestra mensaje de inicio de conexion
# Bucle que espera hasta que la conexion WiFi se establezca
while not wlan.isconnected():         # Mientras no este conectado
    time.sleep(1)                     # Espera 1 segundo entre intentos
    print(".", end="")                # Imprime un punto como indicador de progreso

print("\n¡Conexión establecida!")                        # Confirma conexion exitosa
print("Dirección IP del servidor:", wlan.ifconfig()[0])  # Muestra la IP asignada por DHCP

# --- 5. CONFIGURACION DEL SERVIDOR (SOCKET) ---
# Se crea un socket TCP para escuchar peticiones HTTP en el puerto 80
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]  # Obtiene la direccion para enlazar el socket
s = socket.socket()    # Crea un nuevo socket TCP
s.bind(addr)           # Enlaza el socket a la direccion y puerto 80
s.listen(5)            # Pone el socket en modo escucha con cola de 5 conexiones

print("Servidor web escuchando en", addr)  # Muestra la direccion del servidor

# --- 6. BUCLE PRINCIPAL DEL SERVIDOR ---
while True:                          # Bucle infinito del servidor web
    try:
        cl, addr = s.accept()        # Espera y acepta una conexion entrante de un cliente
        print('Conexión recibida desde:', addr)  # Muestra la IP del cliente conectado

        request = cl.recv(1024)      # Recibe hasta 1024 bytes de la peticion HTTP
        request = str(request)       # Convierte la peticion a cadena para analizarla

        # Analiza la peticion para determinar la accion sobre el LED
        if "/?led1=on" in request:   # Si la URL contiene el parametro led1=on
            led1.value(1)            # Enciende el LED fisico en GPIO18
            print("LED ENCENDIDO")   # Muestra el estado en consola
        if "/?led1=off" in request:  # Si la URL contiene el parametro led1=off
            led1.value(0)            # Apaga el LED fisico en GPIO18
            print("LED APAGADO")     # Muestra el estado en consola

        response = web_page()        # Genera la pagina HTML de respuesta

        # Envia las cabeceras HTTP y el contenido HTML al navegador del cliente
        cl.send('HTTP/1.1 200 OK\n')           # Envia el codigo de estado HTTP 200
        cl.send('Content-Type: text/html\n')    # Indica que el contenido es HTML
        cl.send('Connection: close\n\n')        # Indica que la conexion se cerrara
        cl.sendall(response)                    # Envia todo el contenido HTML

        cl.close()                   # Cierra la conexion con el cliente actual

    except Exception as e:           # Captura cualquier error durante la comunicacion
        print("Error en el servidor:", e)  # Muestra el error en consola
        cl.close()                   # Cierra la conexion en caso de error
