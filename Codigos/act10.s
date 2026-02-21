/* Actividad 10: Traducción de ciclo FOR
   Variables: j -> R0, i -> R1
*/

.text
.global main

main:
    MOV R0, #0          @ j = 0 (R0)
    MOV R1, #0          @ i = 0 (R1) (Inicialización del for)
    MOV R2, #50         @ Límite 50

for_loop:
    CMP R1, R2          @ Compara i con 50 (Condición)
    BGT fin_for         @ Si i > 50, salta fuera del bucle (Branch Greater Than)
    
    @ Cuerpo del ciclo { j = j + 2 }
    ADD R0, R0, #2      @ j = j + 2
    
    @ Incremento del for (i++)
    ADD R1, R1, #1      @ i = i + 1
    
    B for_loop          @ Vuelve a evaluar la condición

fin_for:
    @ Aquí termina el programa. R0 tendrá el resultado final de j (102)
    MOV R7, #1
    SVC 0