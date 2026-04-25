from imu import MPU6050 # [cite: 1273]
from machine import Pin, I2C # [cite: 1274]
import utime # [cite: 1275]

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000) # [cite: 1276]
imu = MPU6050(i2c) # [cite: 1277]

while True: # [cite: 1278]
    # Lee la aceleración en X (en Gs) y la redondea a 2 decimales
    ax = round(imu.accel.x, 2) # [cite: 1279]
    print(f"Fuerza G en X: {ax}") # [cite: 1280]
    
    utime.sleep_ms(200) # [cite: 1281]