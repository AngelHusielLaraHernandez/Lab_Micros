import network #
from time import sleep #

# --- DATOS DE TU RED ---
ssid = 'S23+ de Angel'        # Nombre de tu red Wi-Fi
password = 'angel280731'  # Contraseña de tu red

wlan = network.WLAN(network.STA_IF) #
wlan.active(True) #
wlan.connect(ssid, password) #

connection_timeout = 10 # Tiempo máximo de espera: 10 segundos

while connection_timeout > 0: #
    # El estado 3 o mayor significa que la conexión fue exitosa
    if wlan.status() >= 3: #
        break #
    connection_timeout -= 1 #
    print('Espera conexión WIFI...') #
    sleep(1) #

if wlan.status() != 3: #
    raise RuntimeError('Error en conexión') # Muestra un error si falló
else: #
    print('Conexión establecida') #
    network_info = wlan.ifconfig() # Obtiene los datos IP asignados por el módem
    print('IP address:', network_info[0]) # Anota esta IP, la usarás en tu navegador