import math
from imu import MPU6050
from machine import Pin, I2C
import utime

# Inicialización I2C y Sensor MPU6050
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
imu = MPU6050(i2c)

# Configuración de actuadores indicados en la Tabla 10-2 [cite: 1284]
led = Pin(18, Pin.OUT)
buzzer = Pin(17, Pin.OUT)

while True:
    # 1. Lee las fuerzas G en los tres ejes
    ax = imu.accel.x
    ay = imu.accel.y
    az = imu.accel.z
    
    # 2. Transforma la aceleración a Ángulo de inclinación (Roll) usando trigonometría
    try:
        # math.atan2 devuelve radianes; lo convertimos a grados
        angulo_x = math.degrees(math.atan2(ax, math.sqrt(ay**2 + az**2)))
    except Exception:
        angulo_x = 0
        
    print(f"Inclinación actual: {angulo_x:.1f}°")
    
    # 3. Lógica de control basada en la Tabla 10-2 [cite: 1284]
    # Reposo: Entre -45° y 45°
    if -45 <= angulo_x <= 45:
        led.value(0)    # LED = OFF [cite: 1284]
        buzzer.value(0) # BUZZER = OFF [cite: 1284]
        
    # Peligro: Menor o igual a -46°  o  Mayor o igual a 46°
    elif angulo_x <= -46 or angulo_x >= 46:
        led.value(1)    # LED = ON [cite: 1284]
        buzzer.value(1) # BUZZER = ON [cite: 1284]
        
    utime.sleep_ms(200) # [cite: 1281]