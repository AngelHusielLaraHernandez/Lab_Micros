/* ACTIVIDAD 6: Búsqueda del número mayor en arreglo
   Objetivo: Encontrar el máximo y guardar su valor y su dirección de memoria.
*/
.data
    @ Arreglo de 20 números al azar para la prueba
    ARREGLO: .word 5, 12, 3, 45, 2, 105, 1, 8, 33, 10, 11, 14, 0, 77, 21, 6, 9, 88, 4, 15
    MAX_VAL: .word 0          @ Variable para guardar el número más grande
    MAX_DIR: .word 0          @ Variable para guardar la dirección de memoria de ese número

.text
.global main

main:
    ldr r0, =ARREGLO          @ R0 = Puntero principal que recorrerá el arreglo
    mov r1, #20               @ R1 = Límite de elementos (20)
    ldr r2, [r0]              @ R2 = Guarda el MÁXIMO (Inicia asumiendo que el índice 0 es el mayor)
    mov r3, r0                @ R3 = Guarda la DIRECCIÓN del máximo (Inicia con la del índice 0)
    mov r4, #1                @ R4 = Contador de ciclo (inicia en 1 porque ya evaluamos el 0)
    add r0, r0, #4            @ Avanzamos el puntero de memoria al índice 1

buscar_mayor:
    cmp r4, r1                @ Compara el contador con 20
    beq fin_busqueda          @ Si terminamos, salta al final
    
    ldr r5, [r0]              @ R5 = Lee el valor actual de la memoria
    cmp r5, r2                @ Compara (Valor_Actual vs Máximo_Registrado)
    ble siguiente             @ Branch if Less or Equal: Si es menor o igual, ignóralo y salta a 'siguiente'
    
    @ Si llegó a esta línea, encontramos un nuevo mayor
    mov r2, r5                @ R2 adopta el nuevo valor mayor
    mov r3, r0                @ R3 adopta la dirección de memoria de este nuevo mayor

siguiente:
    add r0, r0, #4            @ Avanzamos la lectura en la memoria (4 bytes)
    add r4, r4, #1            @ Incrementamos el contador de ciclo
    b buscar_mayor            @ Repetimos

fin_busqueda:
    ldr r6, =MAX_VAL          @ Carga dirección para guardar el valor
    str r2, [r6]              @ Almacena en memoria el valor mayor
    ldr r6, =MAX_DIR          @ Carga dirección para guardar la ubicación
    str r3, [r6]              @ Almacena en memoria la dirección del mayor

    MOV R7, #1                @ sys_exit
    SVC 0                     @ Terminar