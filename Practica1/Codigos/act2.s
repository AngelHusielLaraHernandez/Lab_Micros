.text                   
.global _start          

_start:
    MOV R0, #5          @ Carga el valor 5 en R0
    MOV R1, #0x01       @ Carga el valor 1 en R1
    SUBS R3, R0, R1     @ Resta R1 a R0 (5-1), guarda en R3 y actualiza banderas
    
    BEQ igual           @ Si Z=1, salta a etiqueta 'igual'
    BNE diferente       @ Si Z=0, salta a 'diferente'

igual:                  
    MOV R0, #1          @ Descriptor de archivo 1 (Salida estandar / pantalla)
    LDR R1, =texto1     @ Carga la direccion de 'texto1'
    MOV R2, #14         @ Longitud del mensaje
    MOV R7, #4          @ Syscall 4 (Write)
    SVC 0               
    B fin               @ Salto al final

diferente:              
    MOV R0, #1          @ Descriptor de archivo 1
    LDR R1, =texto2     @ Carga la direccion de 'texto2'
    MOV R2, #17         @ Longitud del mensaje
    MOV R7, #4          @ Syscall 4 (Write)
    SVC 0               

fin:                    
    MOV R0, R3          
    MOV R7, #1          @ Syscall 1 (Exit)
    SVC 0               

.data                   
    texto1: .asciz "Datos iguales\n"      
    texto2: .asciz "Datos diferentes\n"   