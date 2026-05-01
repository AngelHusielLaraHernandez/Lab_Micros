
# Importa la clase MPU6050 para el sensor IMU
from imu import MPU6050
# Importa las clases Pin e I2C del módulo machine
from machine import Pin, I2C
# Importa la librería utime para retardos
import utime


# Inicializa el bus I2C en los pines 8 (SDA) y 9 (SCL) a 400kHz
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
# Crea el objeto imu para leer el sensor MPU6050
imu = MPU6050(i2c)


# Bucle infinito para mostrar la aceleración en X
while True:
    # Lee la aceleración en X (en Gs) y la redondea a 2 decimales
    ax = round(imu.accel.x, 2)
    # Imprime la fuerza G en X
    print(f"Fuerza G en X: {ax}")
    # Espera 200 ms antes de la siguiente lectura
    utime.sleep_ms(200)