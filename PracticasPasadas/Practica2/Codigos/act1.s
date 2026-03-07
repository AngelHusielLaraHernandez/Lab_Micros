/* ACTIVIDAD 1: Direccionamiento con desplazamiento a la izquierda (LSL)
   Objetivo: Guardar el valor del contador en un arreglo de 16 posiciones.
*/
.data
    i: .skip 64               @ Reserva 64 bytes de memoria (16 palabras de 4 bytes)

.text
.global main                  @ Define 'main' como global para Code::Blocks / Linker

main:
    ldr r1, =i                @ Carga en R1 la dirección base de la variable 'i'
    mov r2, #0                @ R2 será nuestro contador, inicializado en 0

loop: 
    cmp r2, #16               @ Compara el contador R2 con el límite de 16
    beq fin                   @ Si R2 es igual a 16 (Branch if EQual), salta a la etiqueta 'fin'
    
    add r3, r1, r2, LSL #2    @ R3 = R1 + (R2 desplazado a la izquierda 2 bits). Equivale a R3 = R1 + (R2 * 4). Calcula la dirección en memoria.
    str r2, [r3]              @ Guarda el valor actual del contador (R2) en la dirección de memoria apuntada por R3
    add r2, r2, #1            @ Incrementa el contador (R2 = R2 + 1)
    b loop                    @ Salto incondicional (Branch) de regreso a 'loop'

fin: 
    MOV R7, #1                @ Carga la llamada al sistema sys_exit (1)
    SVC 0                     @ Ejecuta la llamada para salir limpiamente al SO