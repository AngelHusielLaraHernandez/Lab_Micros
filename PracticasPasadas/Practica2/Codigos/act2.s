/* ACTIVIDAD 2: Direccionamiento Post-indexado con 32 datos
   Objetivo: Guardar 32 números usando auto-incremento de dirección.
*/
.data
    i: .skip 128              @ Reserva 128 bytes (32 elementos * 4 bytes cada uno)

.text
.global main

main:
    ldr r1, =i                @ Carga en R1 la dirección base del arreglo 'i'
    mov r2, #0                @ R2 es el contador, inicia en 0

loop2:
    cmp r2, #32               @ Compara el contador con 32 (el doble que la act. 1)
    beq salir                 @ Si llegamos a 32, salta a 'salir'
    
    str r2, [r1], #4          @ DIRECCIONAMIENTO POST-INDEXADO: Guarda R2 en la memoria de R1, y LUEGO suma 4 a R1 automáticamente.
    add r2, r2, #1            @ Incrementa el contador R2 en 1
    b loop2                   @ Repite el bucle

salir:
    MOV R7, #1                @ Prepara sys_exit
    SVC 0                     @ Termina ejecución