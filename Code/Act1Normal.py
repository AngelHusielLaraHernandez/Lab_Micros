import select   
import sys      
import time
import machine

poll_obj = select.poll() 
poll_obj.register(sys.stdin, 1)
sys.stdout.write("Esperando recepción de datos \n")
print("Teclea un carácter y luego <enter>")

while True:
    if poll_obj.poll(0): 
        ch = sys.stdin.read(1) 
        sys.stdout.write("Dato recibido \n") 
        print("Hola UNAM") 
    time.sleep(0.1) 