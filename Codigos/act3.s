.data
var1: .word 0xAA            @ Definimos una variable con valor hexadecimal AA

.text
.global main

main:
    MOV R0, #10             @ 1. MOV: Carga valor 10 en R0
    MOV R1, #20             @ 2. MOV: Carga valor 20 en R1
    ADD R2, R0, R1          @ 3. ADD: Suma 10 + 20 = 30 en R2
    SUB R3, R1, R0          @ 4. SUB: Resta 20 - 10 = 10 en R3
    
    LDR R4, =var1           @ 5. LDR (dirección): Carga dirección de var1 en R4
    LDR R5, [R4]            @ 6. LDR (valor): Carga el valor 0xAA de memoria en R5
    
    AND R6, R5, #0x0F       @ 7. AND: Máscara para quedarse con la parte baja (0x0A)
    ORR R7, R2, #1          @ 8. ORR: Operación lógica OR con 1 (30 OR 1 = 31)
    
    CMP R2, #30             @ 9. CMP: Compara si R2 es igual a 30
    BEQ es_treinta          @ 10. BEQ: Salta si es igual (R2 = 30)
    
    MOV R0, #0              @ Si no es igual, pone 0 en R0
    B sailr                 @ 11. B: Salto incondicional (instrucción adicional)

es_treinta:
    MOV R0, #1              @ Si es igual, pone 1 en R0

sailr:
    MOV R7, #1              @ Preparamos la salida (sys_exit)
    SVC 0                   @ 12. SVC: Ejecutamos la salida
