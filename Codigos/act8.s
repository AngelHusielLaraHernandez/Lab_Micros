/* Actividad 8: Suma de 64 bits (Parte Baja y Alta)
   Num1 = R1:R0 (Alta:Baja)
   Num2 = R3:R2 (Alta:Baja)
*/

.text
.global main

main:
    @ Cargamos el primer número de 64 bits (ej. 0x00000001 FFFFFFFF)
    LDR R0, =0xFFFFFFFF @ Parte baja Num1
    LDR R1, =0x00000001 @ Parte alta Num1
    
    @ Cargamos el segundo número de 64 bits (ej. 0x00000000 00000002)
    LDR R2, =0x00000002 @ Parte baja Num2
    LDR R3, =0x00000000 @ Parte alta Num2
    
    @ Paso 1: Sumar las partes bajas y actualizar banderas (ADDS)
    ADDS R4, R0, R2     @ R4 = R0 + R2 (Parte baja resultado)
    
    @ Paso 2: Sumar las partes altas + el acarreo anterior (ADC)
    ADC R5, R1, R3      @ R5 = R1 + R3 + Carry (Parte alta resultado)
    
    @ Resultado final en R5:R4 (64 bits)
    
    MOV R7, #1
    SVC 0