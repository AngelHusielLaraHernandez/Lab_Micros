/* Actividad 7: Suma de 32 bits detectando acarreo
*/
.data
    dato1: .word 0xFFFFFFFF  @ Número grande para forzar acarreo
    dato2: .word 0x00000002
    res:   .word 0
    carry: .word 0

.text
.global main

main:
    LDR R0, =dato1      @ Carga dirección de dato1
    LDR R1, [R0]        @ Carga valor de dato1 en R1
    LDR R0, =dato2      @ Carga dirección de dato2
    LDR R2, [R0]        @ Carga valor de dato2 en R2
    
    ADDS R3, R1, R2     @ Suma R1+R2 y actualiza banderas (Sufijo 'S')
    
    LDR R0, =res        @ Dirección resultado
    STR R3, [R0]        @ Guarda la suma
    
    MOV R4, #0          @ Prepara registro para el acarreo
    ADC R4, R4, #0      @ Suma con Acarreo: R4 = 0 + 0 + Carry Flag
    
    LDR R0, =carry      @ Dirección acarreo
    STR R4, [R0]        @ Guarda el acarreo (1 si hubo, 0 si no)

    MOV R7, #1
    SVC 0