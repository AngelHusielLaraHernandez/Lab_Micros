/* ACTIVIDAD 3: Copia de arreglo invertida
   Objetivo: A = [1..16], B = [16..1]
*/
.data
    A: .word 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16  @ Arreglo original de 16 datos
    B: .skip 64               @ Arreglo vacío 'B' para la copia (64 bytes)

.text
.global main

main:
    ldr r1, =A                @ R1 apunta al INICIO del arreglo original 'A'
    ldr r2, =B                @ R2 apunta al INICIO del arreglo destino 'B'
    add r2, r2, #60           @ Movemos R2 para que apunte al ÚLTIMO espacio de 'B' (15 posiciones * 4 bytes = +60)
    mov r3, #0                @ R3 es el contador, inicia en 0

loop_copia:
    cmp r3, #16               @ ¿Ya copiamos 16 elementos?
    beq fin_copia             @ Si sí, termina el ciclo
    
    ldr r4, [r1], #4          @ Lee el dato apuntado por R1, lo guarda en R4 y avanza R1 hacia ADELANTE (+4 bytes)
    str r4, [r2], #-4         @ Escribe R4 en la dirección R2, y mueve R2 hacia ATRÁS (-4 bytes)
    
    add r3, r3, #1            @ Aumenta el contador de copiados
    b loop_copia              @ Repite el ciclo

fin_copia:
    MOV R7, #1                @ sys_exit
    SVC 0                     @ Termina programa