# Practica 4 — Laboratorio de Microcomputadoras

> **Plataforma Raspberry Pi Pico (RP2040) — Programacion en MicroPython con IDE Thonny**

---

## Objetivo

Realizar control de acciones mediante las terminales de **Raspberry Pi Pico** por medio de
las funciones **GPIO** en la modalidad de entrada y salida.

---

## Actividades

| # | Descripcion | Estado |
|:-:|-------------|:------:|
| 1 | Lectura de interruptor en GPIO8 e impresion de estado en consola | Completada |
| 2 | Control de LED verde en GPIO0 segun estado de interruptor en GPIO8 | Completada |
| 3 | Control de LED con push button en GPIO12 (PULL_UP) | Completada |
| 4 | Secuencia de LEDs (GPIO4-GPIO7) y buzzer con push button S1 | Completada |
| 5 | Control de 8 LEDs, buzzer y contadores segun tabla de entradas (5 switches) | Pendiente |

### Progreso general

```
Completadas : [########--] 2 / 5
Pendientes  : [--------##] 3 / 5
```

> **Nota:** La actividad 3,45 se encuentra pendiente de desarrollo
> (propuesta de solucion, diagramas de flujo y analisis de resultados).

---

## Estructura del proyecto

```
Practica1/
├── Code/                # Codigos fuente en MicroPython
│   ├── act1.py          # Actividad 1 — Lectura de interruptor
│   ├── act2.py          # Actividad 2 — Interruptor + LED
│   ├── act3.py          # Actividad 3 — Push button + LED
│   ├── act4.py          # Actividad 4 — Secuencia LEDs + buzzer
│   └── act5.py          # Actividad 5 — Control completo I/O
├── img/                 # Imagenes del reporte
├── In/                  # Instrucciones de la practica
├── portada_img/         # Escudos UNAM / FI para la portada
├── PracticasPasadas/    # Practicas anteriores (1, 2 y 3)
├── main.tex             # Documento principal de LaTeX
├── portada.tex          # Portada del reporte
├── referencias.bib      # Referencias bibliograficas
├── main.pdf             # PDF compilado
└── README.md            # Este archivo
```

---

## Compilacion del reporte

```bash
# Compilacion completa (recomendado)
latexmk -pdf main.tex

# O manualmente
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

---

## Equipo

| Integrante |
|------------|
| Espinoza Matamoros Percival Ulises |
| Flores Colin Victor Jaziel |
| Lara Hernandez Angel Husiel |

---

## Notas importantes

- Los codigos de cada actividad se encuentran en la carpeta `Code/`.
- El reporte utiliza diagramas de flujo en **TikZ** para las propuestas de solucion.
- Esta practica corresponde a la **Practica 4** del manual (GPIO entrada/salida).
