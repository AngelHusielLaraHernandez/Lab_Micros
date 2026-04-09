# Práctica 6 — Laboratorio de Microcomputadoras: Convertidor Analógico Digital y Control PWM

> **Plataforma Raspberry Pi Pico (RP2040) — Programación en MicroPython con IDE Thonny**

---

## Objetivo

Conocer el funcionamiento del **ADC** (Convertidor Analógico Digital) para realizar aplicaciones que requieran procesar señales en el mundo continuo, convertir señales provenientes de sensores; aprender el funcionamiento del control **PWM** (Modulación por Ancho de Pulso).

---

## Actividades

| # | Descripción | Estado |
|:-:|-------------|:------:|
| 1 | Comentar código de prueba de lectura ADC e indicar su funcionamiento | Pendiente |
| 2 | Programa que despliega en consola el resultado de conversión ADC y voltaje del potenciómetro (actualización cada segundo) | Pendiente |
| 3 | Programa que muestra el valor de temperatura en °C y °F del sensor interno de la Raspberry Pi Pico | Pendiente |
| 4 | Programa que muestra temperaturas del sensor interno y sensor TMP36, indicando cuál tiene valor mayor | Completada |
| 5 | Comentar código de control PWM con incremento gradual de duty cycle (efecto de respiración en LED) | Completada |
| 6 | Modificar programa para incremento/decremento automático de PWM en GPIO0 con valor inverso en GPIO1 | Pendiente |
| 7 | Control PWM mediante señal analógica proveniente del potenciómetro | Pendiente |

### Progreso general

```
Completadas : [####          ] 2 / 7
Pendientes  : [##########    ] 5 / 7
```

> **Nota:** Todas las actividades incluyen diagramas de flujo en TikZ, diagramas de circuito, códigos fuente en MicroPython comentados, fotografías del hardware montado y análisis detallado en el reporte LaTeX.

---

## Contenido técnico

### Actividades 1-2: Convertidor Analógico Digital (ADC)
- Lectura de señales analógicas mediante `machine.ADC`
- Conversión de valores digitales (0-65535) a voltaje (0-3.3V)
- Uso de potenciómetro como fuente de señal variable

### Actividades 3-4: Sensores de Temperatura
- **Sensor interno** del RP2040 (ADC canal 4)
- **Sensor externo TMP36** conectado a GP28 (ADC canal 28)
- Conversión de voltaje a temperatura en °C y °F
- Comparación y análisis de lecturas entre ambos sensores

### Actividades 5-7: Control PWM
- Configuración de señales PWM en pines GPIO
- Control de brillo de LEDs mediante ciclo de trabajo (duty cycle)
- Efecto de "respiración" con incremento/decremento automático
- Control analógico de PWM mediante potenciómetro

---

## Estructura del proyecto

```
Practica1/
├── Code/                    # Códigos fuente en MicroPython
│   ├── Ac1SinNombres.py     # Código base sin comentarios (Act. 1)
│   ├── Act1.py              # Actividad 1 — Lectura ADC comentada
│   ├── Act2.py              # Actividad 2 — ADC con potenciómetro
│   ├── Act3.py              # Actividad 3 — Sensor temperatura interno
│   ├── Act4.py              # Actividad 4 — Sensor interno + TMP36
│   ├── Act5SinNombre.py     # Código base sin comentarios (Act. 5)
│   ├── Act5.py              # Actividad 5 — PWM con duty cycle
│   ├── Act6.py              # Actividad 6 — PWM auto inc/dec
│   └── Act7.py              # Actividad 7 — PWM con potenciómetro
├── img/                     # Fotografías del hardware
│   ├── Actividad1/          # Montaje y pruebas Act. 1
│   ├── Actividad2/          # Montaje y pruebas Act. 2
│   ├── Actividad3/          # Montaje y pruebas Act. 3
│   ├── Actividad4/          # Montaje y pruebas Act. 4
│   ├── Actividad5/          # Montaje y pruebas Act. 5
│   ├── Actividad6/          # Montaje y pruebas Act. 6
│   └── Actividad7/          # Montaje y pruebas Act. 7
├── portada_img/             # Escudos UNAM / FI para la portada
├── PracticasPasadas/        # Prácticas anteriores (1 a 5)
├── main.tex                 # Documento principal LaTeX
├── portada.tex              # Portada del reporte
├── referencias.bib          # Referencias bibliográficas
├── main.pdf                 # PDF compilado
└── README.md                # Este archivo
```

---

## Diagramas incluidos

El reporte incluye los siguientes diagramas elaborados en **TikZ**:

| Figura | Descripción |
|--------|-------------|
| 6-1 | Circuito potenciómetro conectado a GP26 (ADC) |
| 6-2 | Circuito LED conectado a GP1 (PWM) |
| 6-3 | Circuito sensor TMP36 conectado a GP28 |
| 6-4 | Diagrama de flujo — Actividad 4 (comparación de temperaturas) |
| 6-5 | Diagrama de flujo — Actividad 5 (control PWM) |
| 6-6 | Circuito con dos LEDs y resistencias (GPIO0, GPIO1) |
| 6-7 | Oscilogramas de señales PWM |
| 6-8 | Circuito completo con potenciómetro y LEDs (Actividad 7) |

---

## Compilación del reporte

```bash
# Compilación completa (recomendado)
latexmk -pdf main.tex

# O manualmente
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
**Fecha de entrega:** 12 de Abril del 2026

---

## Notas importantes

- Los códigos de cada actividad se encuentran en la carpeta `Code/`
- El reporte utiliza diagramas de flujo y circuitos elaborados en **TikZ**
- Esta práctica corresponde a la **Práctica 6** del manual (ADC y PWM)
- Se incluyen diagramas de flujo con explicación del flujo de datos para las actividades 4 y 5
- Los circuitos incluyen símbolos estándar de resistencias, LEDs, potenciómetros y sensores

---

## Componentes utilizados

| Componente | Cantidad | Uso |
|------------|:--------:|-----|
| Raspberry Pi Pico | 1 | Microcontrolador principal |
| Potenciómetro 10kΩ | 1 | Entrada analógica variable |
| Sensor TMP36 | 1 | Medición de temperatura externa |
| LED | 2 | Indicadores visuales (PWM) |
| Resistencia 220Ω | 2 | Limitadores de corriente para LEDs |
| Protoboard | 1 | Montaje de circuitos |
| Cables jumper | Varios | Conexiones |
