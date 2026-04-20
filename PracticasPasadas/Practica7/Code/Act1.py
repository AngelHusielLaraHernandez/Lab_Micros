import select   # Importa la librería para monitorear eventos en flujos de datos  
import sys      # Importa la librería para acceder a la entrada/salida estándar (consola)  
import time
import machine

# Crea un objeto 'poll' para verificar si hay datos listos para leerse  
poll_obj = select.poll() 
# Registra la entrada estándar (teclado/consola) para ser monitoreada  
poll_obj.register(sys.stdin, 1)

# Imprime un mensaje directo al flujo de salida (sin agregar salto de línea automático)  
sys.stdout.write("Esperando recepción de datos \n")
# Imprime usando la función estándar de Python  
print("Teclea un carácter y luego <enter>")

while True:
    # poll(0) verifica instantáneamente si se tecleó algo sin bloquear el código  
    if poll_obj.poll(0): 
        ch = sys.stdin.read(1) # Lee exactamente 1 carácter tecleado  
        sys.stdout.write("Dato recibido \n")  
        print("Hola UNAM")  
    time.sleep(0.1) # Breve pausa para no saturar el procesador  