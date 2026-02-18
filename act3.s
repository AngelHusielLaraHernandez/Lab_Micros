/* Actividad 3: Programa con 10 instrucciones distintas
   Objetivo: Manipulación de bits y memoria
*/

.data
    var1: .word 0xAA    @ Definimos una variable con valor hexadecimal AA

.text
.global main

main:
    MOV R0, #10         @ 1. MOV: Carga valor 10
    MOV R1, #20         @ Carga valor 20
    ADD R2, R0, R1      @ 2. ADD: Suma 10 + 20 = 30
    SUB R3, R1, R0      @ 3. SUB: Resta 20 - 10 = 10
    
    LDR R4, =var1       @ 4. LDR (dirección): Carga dirección de var1
    LDR R5, [R4]        @ 5. LDR (valor): Carga el valor 0xAA de memoria
    
    AND R6, R5, #0x0F   @ 6. AND: Máscara para quedarse con la parte baja (0x0A)
    ORR R7, R2, #1      @ 7. ORR: Operación lógica OR con 1
    
    CMP R2, #30         @ 8. CMP: Compara si R2 es 30
    BEQ es_treinta      @ 9. BEQ: Salta si es igual
    
    MOV R0, #0          @ Si no es igual, pone 0
    B salir             @ 10. B: Salto incondicional

es_treinta:
    MOV R0, #1          @ Si es igual, pone 1

salir:
    MOV R7, #1          @ Salida
    SVC 0