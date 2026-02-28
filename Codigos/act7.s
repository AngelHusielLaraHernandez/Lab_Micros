/* ACTIVIDAD 7: Ordenamiento Burbuja de 32 elementos (32 bits)
   Objetivo: Conservar arreglo original, ordenar la copia.
*/
.data
    @ Arreglo original desordenado (32 elementos)
    A: .word 32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,
    12,11,10,9,8,7,6,5,4,3,2,1
    @ Arreglo copia donde se hará el ordenamiento
    B: .skip 128              @ Reserva 128 bytes (32 words x 4)

.text
.global main

main:
    @ --- FASE 1: COPIAR A en B ---
    ldr r0, =A                @ R0 apunta a Original
    ldr r1, =B                @ R1 apunta a Copia
    mov r2, #32               @ R2 contador para copiar
copiar:
    cmp r2, #0                @ ¿Quedan elementos por copiar?
    beq iniciar_orden         @ Si es 0, terminamos de copiar y vamos a ordenar
    ldr r3, [r0], #4          @ Lee de A y avanza
    str r3, [r1], #4          @ Escribe en B y avanza
    sub r2, r2, #1            @ Resta 1 al contador
    b copiar

    @ --- FASE 2: ORDENAMIENTO BURBUJA (Sobre B) ---
iniciar_orden:
    mov r4, #32               @ R4 = N (Cantidad total de elementos)
bucle_externo:
    subs r4, r4, #1           @ Resta 1 a N (N = N - 1) y actualiza flags (S final)
    beq fin_ordenamiento      @ Si N llega a 0, todo está ordenado
    
    ldr r1, =B                @ Resetea el puntero R1 al inicio de B para cada pasada
    mov r5, #0                @ R5 = 'i' (Índice del bucle interno)

bucle_interno:
    cmp r5, r4                @ Compara el índice interno 'i' con 'N'
    beq bucle_externo         @ Si i == N, terminó esta pasada, regresa al bucle externo
    
    ldr r6, [r1]              @ R6 = B[i] (Valor actual)
    ldr r7, [r1, #4]          @ R7 = B[i+1] (Valor adyacente derecho)
    
    cmp r6, r7                @ Comparamos si el actual es mayor que el derecho
    ble no_cambiar            @ Branch if Less or Equal: Si B[i] <= B[i+1] están bien, no cambies
    
    @ Si llegamos aquí, B[i] es mayor, tenemos que hacer INTERCAMBIO (Swap)
    str r7, [r1]              @ Escribimos el valor menor (R7) en la posición izquierda B[i]
    str r6, [r1, #4]          @ Escribimos el valor mayor (R6) en la posición derecha B[i+1]

no_cambiar:
    add r1, r1, #4            @ Avanzamos el puntero de memoria para evaluar los siguientes
    add r5, r5, #1            @ i++
    b bucle_interno           @ Repetimos el bucle interno

fin_ordenamiento:
    MOV R7, #1                @ sys_exit
    SVC 0                     @ Fin