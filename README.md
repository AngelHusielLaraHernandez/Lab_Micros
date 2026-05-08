# Práctica 11 — Laboratorio de Microcomputadoras: Interrupciones y Programación Multinúcleo

> **Plataforma Raspberry Pi Pico (RP2040) — Programación en MicroPython con IDE Thonny**

---

## Objetivo

Entender y aplicar la programación mediante interrupciones, así como la realización de programas que utilicen diferentes núcleos y optimicen la ejecución en paralelo.

---


## Actividades

| # | Descripción | Estado |
|:-:|-------------|:------:|
| 1 | Interrupción básica con S1 (GPIO12) | Pendiente |
| 2 | Generar señal cuadrada en GPIO20 tras interrupción S1 | Pendiente |
| 3 | Dos interrupciones: S1 y S2, control de LEDs y contador TM1637 | Pendiente |
| 4 | Uso de hilos (multinúcleo) para parpadeo de LEDs | Pendiente |
| 5 | Interrupciones en diferentes núcleos, control de LEDs | Pendiente |
| 6 | Semáforo peatonal con interrupciones, hilos y display TM1637 | Pendiente |

### Progreso general

Completadas: 0 / 6

---


## Contenido técnico

### Actividades 1-2: Interrupciones básicas
- Configuración de pines de entrada y salida.
- Manejo de interrupciones por flanco de bajada.

### Actividades 3-4: Múltiples interrupciones y multinúcleo
- Control de múltiples entradas (S1, S2) y salidas (LEDs, TM1637).
- Uso de hilos para ejecución en paralelo en la Raspberry Pi Pico.

### Actividades 5-6: Semáforo peatonal y sincronización
- Implementación de semáforo con barra Neopixel y display TM1637.
- Sincronización de eventos entre núcleos y manejo de interrupciones para peatones.

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
**Práctica:** 11 (Interrupciones y Multinúcleo)

---

## Notas importantes

- Este README corresponde a la práctica 11: Interrupciones y Programación Multinúcleo.