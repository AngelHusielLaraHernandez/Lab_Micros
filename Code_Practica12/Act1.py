import network #

# Configura el módulo en modo Estación (STA_IF) para que actúe como un cliente Wi-Fi
wlan = network.WLAN(network.STA_IF) #
wlan.active(True) #

# Escanea el entorno buscando redes disponibles
networks = wlan.scan() #

print("Redes cercanas:") #
for network_info in networks: #
    # Imprime una tupla con (ssid, bssid, channel, RSSI, authmode, hidden)
    print(network_info) #