        .text
        .global main

        main:
        MOV R0, #0          @ R0 sera nuestro contador, inicia en 0
        MOV R1, #9          @ R1 es el limite superior (9)
        MOV R2, #0          @ R2 es el limite inferior (0)

        loop1:              @ Etiqueta para subir
        ADD R0, R0, #1      @ Incrementa R0 en 1
        CMP R1, R0          @ Compara si llegamos al limite superior (9)
        BNE loop1           @ Si NO es igual, repite loop1

        loop2:              @ Etiqueta para bajar
        ADD R0, R0, #-1     @ Decrementa R0 en 1
        CMP R2, R0          @ Compara si llegamos al limite inferior (0)
        BEQ loop1           @ Si es igual a 0, salta de nuevo a loop1
        B loop2             @ Si no es 0, sigue bajando