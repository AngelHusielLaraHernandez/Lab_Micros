/* Actividad 3: Programa con 10 instrucciones (Versión Simplificada)
   Plataforma: Raspberry Pi (Code::Blocks)
   Objetivo: Usar 10 instrucciones diferentes de forma lineal.
*/

.text                   @ Inicio de la sección de código
.global main            @ "main" es necesario para Code::Blocks

main:
    @ --- INSTRUCCIÓN 1: MOV (Mover/Cargar) ---
    MOV R1, #10         @ Cargamos el valor 10 en el registro R1.

    @ --- INSTRUCCIÓN 2: ADD (Suma) ---
    ADD R2, R1, #5      @ R2 = 10 + 5. Resultado: 15.

    @ --- INSTRUCCIÓN 3: SUB (Resta) ---
    SUB R3, R2, #2      @ R3 = 15 - 2. Resultado: 13.

    @ --- INSTRUCCIÓN 4: MUL (Multiplicación) ---
    MUL R4, R1, R2      @ R4 = 10 * 15. Resultado: 150.
                        @ (Nota: MUL requiere solo registros, no números directos).

    @ --- INSTRUCCIÓN 5: AND (Y Lógico - Máscara) ---
    AND R5, R1, #1      @ R5 = 10 AND 1. (10 es 1010 en binario, 1 es 0001).
                        @ Resultado: 0 (Sirve para saber si es par).

    @ --- INSTRUCCIÓN 6: ORR (O Lógico - Encender bits) ---
    ORR R6, R1, #1      @ R6 = 10 OR 1. (1010 OR 0001). Resultado: 11 (1011).

    @ --- INSTRUCCIÓN 7: LSL (Desplazamiento Izquierda - Multiplicar por 2) ---
    LSL R7, R1, #1      @ R7 = 10 desplazado 1 vez a la izquierda.
                        @ 10 (decimal) -> 20 (decimal). Equivale a multiplicar por 2.

    @ --- INSTRUCCIÓN 8: LSR (Desplazamiento Derecha - Dividir por 2) ---
    LSR R8, R1, #1      @ R8 = 10 desplazado 1 vez a la derecha.
                        @ 10 (decimal) -> 5 (decimal). Equivale a dividir entre 2.

    @ --- INSTRUCCIÓN 9: CMP (Comparar) ---
    CMP R1, #10         @ Comparamos si R1 es igual a 10. 
                        @ Esto actualiza las banderas internas (Z flag).

    @ --- INSTRUCCIÓN 10: SVC (Llamada al Sistema - Salir) ---
    MOV R7, #1          @ Preparamos la salida (sys_exit).
    SVC 0               @ Ejecutamos la salida.
