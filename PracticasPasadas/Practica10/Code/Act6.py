
# Importa las clases Pin e I2C del módulo machine
from machine import Pin, I2C
# Importa la clase SSD1306_I2C para controlar la pantalla OLED
from ssd1306 import SSD1306_I2C

# Inicializa el bus I2C en los pines 9 (SCL) y 8 (SDA) a 400kHz
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)

# Crea el objeto oled para controlar la pantalla OLED de 128x64 píxeles
oled = SSD1306_I2C(128, 64, i2c)


# Escanea los dispositivos conectados al bus I2C y muestra sus direcciones
devices = i2c.scan()
if devices:
    for d in devices:
        print("I2C Address: " + hex(d))


# Limpia la pantalla (la llena de negro)
oled.fill(0)


# Escribe "Microcomputadoras" en la posición (1,6) y "Practica I2C" en (3,30)
oled.text("Microcomputadoras", 1, 6, 1)
oled.text("Practica I2C", 3, 30, 1)


# Muestra el contenido en la pantalla física
oled.show()
# Imprime mensaje en consola
print("UNAM FI")