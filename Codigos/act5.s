/* Actividad 5: Bucle Ascendente y Descendente
*/

.text
.global main

main:
    MOV R0, #0          @ R0 será nuestro contador, inicia en 0
    MOV R1, #9          @ R1 es el límite superior (9)
    MOV R2, #0          @ R2 es el límite inferior (0)

loop1:                  @ Etiqueta para subir
    ADD R0, R0, #1      @ Incrementa R0 en 1
    CMP R1, R0          @ Compara si llegamos al límite superior (9)
    BNE loop1           @ Si NO es igual (Branch Not Equal), repite loop1
                        @ Si llega aquí, R0 vale 9, pasamos a loop2

loop2:                  @ Etiqueta para bajar
    ADD R0, R0, #-1     @ Decrementa R0 en 1 (sumando -1)
    CMP R2, R0          @ Compara si llegamos al límite inferior (0)
    BEQ loop1           @ Si es igual a 0, salta de nuevo a loop1 (reinia el ciclo)
    B loop2             @ Si no es 0, sigue bajando