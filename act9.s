/* Actividad 9: Factorial de un número (n!)
*/

.text
.global main

main:
    MOV R0, #5          @ Número n al que calculamos factorial (ej. 5)
    MOV R1, #1          @ R1 guardará el resultado acumulado (inicia en 1)

loop_fact:
    CMP R0, #1          @ Compara n con 1
    BLE fin_fact        @ Si n <= 1, terminamos
    
    MUL R1, R1, R0      @ R1 = R1 * R0 (Acumulado * n)
    SUB R0, R0, #1      @ Decrementa n
    B loop_fact         @ Repite

fin_fact:
    MOV R0, R1          @ Mueve resultado final a R0
    MOV R7, #1          @ Salir
    SVC 0