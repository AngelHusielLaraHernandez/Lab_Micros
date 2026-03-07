/* ACTIVIDAD 4: Arreglo exponencial y su suma
   Objetivo: Generar serie multiplicando por 2 (Shift), y sumar elementos.
*/
.data
    A:    .skip 80            @ Reserva memoria para 20 elementos (20 * 4 bytes = 80)
    SUMA: .word 0             @ Variable para guardar la sumatoria final

.text
.global main

main:
    ldr r0, =A                @ R0 apunta a la dirección de memoria de A
    mov r1, #3                @ R1 será la variable 'i' inicial (Ejemplo: usamos 3)
    mov r2, #0                @ R2 es el contador de elementos creados
    mov r3, #0                @ R3 será el Acumulador (Sumatoria), inicia en 0

loop_potencias:
    cmp r2, #20               @ Compara si ya generamos los 20 elementos
    beq fin_potencias         @ Si llegamos a 20, salimos del bucle
    
    str r1, [r0], #4          @ Guarda el valor actual en memoria y avanza el puntero R0
    add r3, r3, r1            @ Suma el valor actual de 'i' al Acumulador Total (R3)
    lsl r1, r1, #1            @ Desplazamiento Izquierdo: Multiplica 'i' por 2 para la siguiente iteración
    add r2, r2, #1            @ Incrementa contador
    b loop_potencias          @ Repite

fin_potencias:
    ldr r0, =SUMA             @ Carga la dirección de la variable SUMA
    str r3, [r0]              @ Guarda el resultado total (R3) en esa memoria
    MOV R7, #1                @ sys_exit
    SVC 0                     @ Termina