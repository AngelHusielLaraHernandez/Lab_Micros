.text
.global main

main:
    MOV R1, #80         @ Dato 1 
    MOV R2, #20         @ Dato 2 
    
    ADD R3, R1, R2      @ R3 = 80 + 20 = 100
    
    @ Para dividir entre 2 usamos LSR (Logical Shift Right)
    LSR R0, R3, #1      @ Desplaza bits a la derecha 1 vez. 
    
    @ El resultado (50) ya esta en R0 listo para devolverlo
    MOV R7, #1          @ Salida
    SVC 0