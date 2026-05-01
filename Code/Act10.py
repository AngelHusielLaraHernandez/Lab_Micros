
# Importa la librería math para operaciones matemáticas
import math
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


# Configura el pin 18 como salida para el LED
led = Pin(18, Pin.OUT)
# Configura el pin 17 como salida para el buzzer
buzzer = Pin(17, Pin.OUT)


# Bucle infinito para leer aceleración, calcular ángulo y controlar actuadores
while True:
    # Lee la aceleración en los tres ejes
    ax = imu.accel.x
    ay = imu.accel.y
    az = imu.accel.z
    # Calcula el ángulo de inclinación (roll) usando trigonometría
    try:
        # math.atan2 devuelve radianes; se convierte a grados
        angulo_x = math.degrees(math.atan2(ax, math.sqrt(ay**2 + az**2)))
    except Exception:
        angulo_x = 0
    # Imprime el ángulo de inclinación actual
    print(f"Inclinación actual: {angulo_x:.1f}°")
    # Si el ángulo está entre -45° y 45°, apaga LED y buzzer
    if -45 <= angulo_x <= 45:
        led.value(0)    # LED = OFF
        buzzer.value(0) # BUZZER = OFF
    # Si el ángulo es menor o igual a -46° o mayor o igual a 46°, enciende LED y buzzer
    elif angulo_x <= -46 or angulo_x >= 46:
        led.value(1)    # LED = ON
        buzzer.value(1) # BUZZER = ON
    # Espera 200 ms antes de la siguiente lectura
    utime.sleep_ms(200)