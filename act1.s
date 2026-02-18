.global _start      @ Hace visible la etiqueta _start para el enlazador (linker)

_start:             @ Punto de entrada del programa
    MOV R1, #0x19   @ Carga el valor hexadecimal 19 (25 decimal) en el registro R1
    MOV R2, #53     @ Carga el valor decimal 53 en el registro R2
    
    ADD R3, R2, R1  @ Suma: R3 = R2 + R1. Resultado esperado: 78
    
    MOV R0, R3      @ Mueve el resultado (78) al registro R0 (registro de retorno)
    MOV R7, #1      @ Carga el valor 1 en R7. En Linux, 1 significa "Syscall Exit" (Salir)
    SVC 0           @ Supervisor Call: Llama al Kernel para ejecutar la salida (Exit)