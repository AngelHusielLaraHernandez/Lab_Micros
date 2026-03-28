import select   # Importa la librería para monitorear eventos en flujos de datos [cite: 341]
import sys      # Importa la librería para acceder a la entrada/salida estándar (consola) [cite: 341]
import time
import machine

# Crea un objeto 'poll' para verificar si hay datos listos para leerse [cite: 341]
poll_obj = select.poll() 
# Registra la entrada estándar (teclado/consola) para ser monitoreada [cite: 341]
poll_obj.register(sys.stdin, 1)

# Imprime un mensaje directo al flujo de salida (sin agregar salto de línea automático) [cite: 341]
sys.stdout.write("Esperando recepción de datos \n")
# Imprime usando la función estándar de Python [cite: 341]
print("Teclea un carácter y luego <enter>")

while True:
    # poll(0) verifica instantáneamente si se tecleó algo sin bloquear el código [cite: 341]
    if poll_obj.poll(0): 
        ch = sys.stdin.read(1) # Lee exactamente 1 carácter tecleado [cite: 341]
        sys.stdout.write("Dato recibido \n") [cite: 341]
        print("Hola UNAM") [cite: 341]
    time.sleep(0.1) # Breve pausa para no saturar el procesador [cite: 341]