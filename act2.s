.text                   @ Sección de código
.global _start          @ Punto de entrada global

_start:
    MOV R0, #5          @ Carga el valor 5 en R0
    MOV R1, #0x01       @ Carga el valor 1 en R1
    SUBS R3, R0, R1     @ Resta R1 a R0 (5-1), guarda en R3 y actualiza banderas (S)
    
    BEQ igual           @ Si Z=1 (resultado fue 0, son iguales), salta a etiqueta 'igual'
    BNE diferente       @ Si Z=0 (resultado no fue 0, son diferentes), salta a 'diferente'

igual:                  @ Etiqueta para caso igual
    MOV R0, #1          @ Descriptor de archivo 1 (Salida estándar / pantalla)
    LDR R1, =texto1     @ Carga la dirección de memoria de 'texto1' en R1
    MOV R2, #14         @ Longitud del mensaje (ajustada a longitud real)
    MOV R7, #4          @ Código syscall 4 (Write/Escribir)
    SVC 0               @ Ejecutar llamada al sistema
    B fin               @ Salto incondicional al final para no ejecutar 'diferente'

diferente:              @ Etiqueta para caso diferente
    MOV R0, #1          @ Descriptor de archivo 1 (Salida estándar)
    LDR R1, =texto2     @ Carga la dirección de memoria de 'texto2' en R1
    MOV R2, #17         @ Longitud del mensaje (ajustada a longitud real)
    MOV R7, #4          @ Código syscall 4 (Write/Escribir)
    SVC 0               @ Ejecutar llamada al sistema

fin:                    @ Etiqueta de finalización
    MOV R0, R3          @ Mueve el resultado de la resta a R0
    MOV R7, #1          @ Código syscall 1 (Exit)
    SVC 0               @ Terminar programa

    .data                   @ Sección de datos (variables en memoria)
    texto1: .asciz "Datos iguales\n"      @ Define cadena de texto terminada en nulo
    texto2: .asciz "Datos diferentes\n"   @ Define cadena de texto terminada en nulo
