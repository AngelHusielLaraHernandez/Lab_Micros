# Práctica 10 — Laboratorio de Microcomputadoras: Comunicación I2C

> **Plataforma Raspberry Pi Pico (RP2040) — Programación en MicroPython con IDE Thonny**

---

## Objetivo

Aprender la teoría y aplicación del protocolo I2C, controlar módulos de diversos tipos con comunicación I2C.

---

## Actividades

| # | Descripción | Estado |
|:-:|-------------|:------:|
| 1 | Código inicial de introducción a I2C | Pendiente |
| 2 | Comunicación serie I2C usando el circuito PCF8574 | Pendiente |
| 3 | Generar secuencia de la tabla 10-1 con PCF8574 | Pendiente |
| 4 | Modificación de código y explicación de funcionamiento con PCF8574 | Completada |
| 5 | Control de módulo LCD I2C y estudio de librerías | Completada |
| 6 | Interacción y visualización con librería LCD I2C | Completada |
| 7 | Comunicación I2C a través del módulo TMP102 (sensor de temperatura) | Pendiente |
| 8 | Comunicación I2C a través del módulo AHT10 (sensor de temperatura y humedad) | Pendiente |
| 9 | Uso del módulo MPU6050 (Acelerómetro y giroscopio) | Pendiente |
| 10 | Realizar programa que genere las acciones mostradas en la tabla 10-2 | Pendiente |

### Progreso general

Completadas: 3 / 10

> **Nota:** Las actividades listadas forman parte de la Práctica 10 y actualmente se encuentran todas pendientes de desarrollo y respuesta.

---

## Contenido técnico

### Actividades 1-4: Expansor de E/S PCF8574
- Configuración de pines para I2C (SDA, SCL).
- Uso del PCF8574 para expandir salidas digitales (LEDs RGB) y lectura de entradas.

### Actividades 5-6: Interfaz Visual con LCD I2C
- Configuración y escritura en pantallas alfanuméricas.
- Implementación de librerías I2C para dispositivos de visualización.

### Actividades 7-8: Sensores de Variables Ambientales
- Protocolo para leer registros de temperatura con el TMP102.
- Adquisición de temperatura y humedad a través del AHT10.

### Actividades 9-10: Sensores Inerciales y Secuencias Integradas
- Lectura de ejes espaciales (aceleración y giroscopio) con MPU6050.
- Ejecución de secuencias condicionales de tabla de estados (10-2).

---

## Estructura del proyecto

```text
Practica1/
├── Code/
│   ├── Act1.py
│   ├── Act2.py
│   ├── Act3.py
│   ├── Act4.py
│   ├── Act5.py
│   ├── Act6.py
│   ├── Act7.py
│   ├── Act8.py
│   ├── Act9.py
│   └── Act10.py
├── img/
├── document/
├── portada_img/
├── PracticasPasadas/
├── main.tex
├── portada.tex
├── referencias.bib
├── main.pdf
└── README.md
```

---

## Compilación del reporte

```bash
latexmk -pdf -g -interaction=nonstopmode main.tex
```

Alternativa paso a paso:

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

---

## Equipo

| Integrante | Número de cuenta |
|------------|------------------|
| Espinoza Matamoros Percival Ulises | 320025561 |
| Flores Colin Victor Jaziel | 320266083 |
| Lara Hernandez Angel Husiel | 320060829 |

**Grupo:** 06  
**Semestre:** 2026-2  
**Profesor:** Ing. Moisés Meléndez Reyes  
**Práctica:** 10 (Comunicación I2C)

---

## Notas importantes

- Este README corresponde a la práctica 10: Comunicación I2C.