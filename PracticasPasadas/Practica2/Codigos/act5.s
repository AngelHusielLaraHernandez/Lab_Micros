/* ACTIVIDAD 5: Multiplicación de matrices 2x2
   Objetivo: [A B] x [E F] = [I J]
             [C D]   [G H]   [K L]
*/
.data
    M1: .byte 2, 1, 3, 4      @ Matriz 1 (A,B,C,D) -> Valores de ejemplo de 8 bits
    M2: .byte 1, 5, 2, 1      @ Matriz 2 (E,F,G,H) -> Valores de ejemplo de 8 bits
    MR: .byte 0, 0, 0, 0      @ Matriz Resultado (I,J,K,L)

.text
.global main

main:
    ldr r0, =M1               @ Dirección Matriz 1
    ldr r1, =M2               @ Dirección Matriz 2
    ldr r2, =MR               @ Dirección Matriz Resultado

    @ Cargamos los elementos de M1 (Usamos LDRB por ser Bytes)
    ldrb r3, [r0, #0]         @ R3 = A (Posición 0)
    ldrb r4, [r0, #1]         @ R4 = B (Posición 1)
    ldrb r5, [r0, #2]         @ R5 = C (Posición 2)
    ldrb r6, [r0, #3]         @ R6 = D (Posición 3)

    @ Cargamos los elementos de M2
    ldrb r7, [r1, #0]         @ R7 = E
    ldrb r8, [r1, #1]         @ R8 = F
    ldrb r9, [r1, #2]         @ R9 = G
    ldrb r10,[r1, #3]         @ R10 = H

    @ Calculando I = A*E + B*G
    mul r11, r3, r7           @ R11 = A * E
    mla r11, r4, r9, r11      @ Multiply-Accumulate: R11 = (B * G) + R11
    strb r11, [r2, #0]        @ Guardamos 'I' en la matriz resultado

    @ Calculando J = A*F + B*H
    mul r11, r3, r8           @ R11 = A * F
    mla r11, r4, r10, r11     @ R11 = (B * H) + R11
    strb r11, [r2, #1]        @ Guardamos 'J'

    @ Calculando K = C*E + D*G
    mul r11, r5, r7           @ R11 = C * E
    mla r11, r6, r9, r11      @ R11 = (D * G) + R11
    strb r11, [r2, #2]        @ Guardamos 'K'

    @ Calculando L = C*F + D*H
    mul r11, r5, r8           @ R11 = C * F
    mla r11, r6, r10, r11     @ R11 = (D * H) + R11
    strb r11, [r2, #3]        @ Guardamos 'L'

    MOV R7, #1                @ sys_exit
    SVC 0                     @ Termina