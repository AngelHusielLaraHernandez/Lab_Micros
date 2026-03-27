# Practica 5 — Laboratorio de Microcomputadoras: Control de actuadores con GPIO

> **Plataforma Raspberry Pi Pico (RP2040) — Programación en MicroPython con IDE Thonny**

---

## Objetivo

Reforzar las habilidades para programar y configurar las funciones **GPIO** para controlar motores de corriente directa, motores a pasos y servomotores a través del microcontrolador **Raspberry Pi Pico**. Estudiar la importancia y aplicación de los amplificadores de potencia (drivers) en el control electromecánico.

---

## Actividades

| # | Descripción | Estado |
|:-:|-------------|:------:|
| 1 | Control de dos motores de corriente directa (driver L293D) mediante tabla de verdad (3 interruptores) | Completada |
| 2 | Control de un motor a pasos (driver ULN2003A) y retroalimentación auditiva (buzzer) con rutinas de giro continuo, pasos específicos y bucles | Completada |
| 3 | Control posicional dependiente de condicionales con un servomotor usando señales PWM, botones y switches | Pendiente |
| 4 | Rutina de barrido automático continuo para servomotor (0° a 180° y viceversa) usando PWM | Pendiente |

### Progreso general

```
Completadas : [-------#######] 2 / 4
Pendientes  : [#########-------] 2 / 4
```

> **Nota:** Todas las actividades incluyen diagramas de flujo, códigos fuente en Python, fotografías del hardware montado y el análisis detallado contenido en el reporte principal de LaTeX.

---

## Estructura del proyecto

```
Practica1/
├── Code/                # Códigos fuente en MicroPython
│   ├── Act1.py          # Actividad 1 — Motores DC con L293D
│   ├── Act2.py          # Actividad 2 — Motor a pasos con ULN2003A
│   ├── Act3.py          # Actividad 3 — Servomotor controlado por condicionales (botones/switches)
│   └── Act4.py          # Actividad 4 — Servomotor con barrido automático
├── img/                 # Imágenes, montajes y comprobación del sistema
├── portada_img/         # Escudos UNAM / FI para la portada
├── PracticasPasadas/    # Prácticas anteriores (1 a 4) 
├── main.tex             # Documento principal de LaTeX (Marco teórico, desarrollo, desarrollo y conclusiones)
├── portada.tex          # Portada del reporte
├── README.md            # Este documento
└── referencias.bib      # Fuentes de consulta y bibliografía
```
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
