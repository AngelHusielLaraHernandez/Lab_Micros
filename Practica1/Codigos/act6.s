.text
.global main

main:
    MOV R0, #1          @ Iniciamos con el bit 0 encendido (valor 1 decimal)
    MOV R1, #0          @ Contador de desplazamientos
    MOV R2, #31         @ Límite de desplazamientos (posición 31)

bucle_shift:
    CMP R1, R2          @ Comparamos contador con 31
    BGT fin             @ Si R1 > 31, terminamos
    
    @ Aquí R0 tiene el bit en la posición actual. 
    @ En un entorno real aquí lo enviarías a un LED.
    
    LSL R0, R0, #1      @ Desplaza el bit a la izquierda (Logical Shift Left)
    ADD R1, R1, #1      @ Incrementa contador
    B bucle_shift       @ Repite

fin:
    MOV R7, #1          @ Salida
    SVC 0
