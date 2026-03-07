# Practica 3 — Laboratorio de Microcomputadoras

> **Plataforma Raspberry Pi Pico (RP2040) — Programacion en MicroPython con IDE Thonny**

---

## Objetivo

Conocer los recursos de la plataforma con el microcontrolador **RP2040** contenida en la
Raspberry Pi Pico; desarrollar algoritmos mediante la programacion en **MicroPython**
utilizando el IDE **Thonny** para generar salidas a traves de las terminales GPIO.

---

## Actividades

| # | Descripcion | Estado |
|:-:|-------------|:------:|
| 1 | Parpadeo basico de un LED en GPIO 0 (500 ms) | Completada |
| 2 | Modificar tiempos de parpadeo: rapido (100 ms) y lento (2000 ms) | Completada |
| 3 | Parpadeo de LED en GPIO 5 con retardo de 300 ms | Completada |
| 4 | Control alternado de GPIO 2 y GPIO 3 a 85 ms | Pendiente |
| 5 | Encender y apagar GPIO 0 a GPIO 7 simultaneamente | Pendiente |
| 6 | Repetir encendido/apagado 10 veces con pausa de 2 s | Pendiente |
| 7 | Secuencia tipo "LED viajero" de GPIO 0 a GPIO 7 (100 ms) | Pendiente |
| 8 | Secuencia de llenado acumulativo de GPIO 0 a GPIO 7 (100 ms) | Pendiente |
| 9 | Contador binario ascendente de 8 bits (50 ms) | Pendiente |
| 10 | Control de dos semaforos con secuencia de estados | Pendiente |

### Progreso general

```
Completadas : [###-------] 3 / 10
Pendientes  : [-------###] 7 / 10
```

> **Nota:** Las actividades 4 a 10 se encuentran pendientes de desarrollo
> (propuesta de solucion, diagramas de flujo y analisis de resultados).

---

## Pendientes adicionales

- [ ] Completar la seccion *Propuesta de solucion* para las actividades 4 a 10
- [ ] Agregar diagramas de flujo para las actividades 4 a 10
- [ ] Redactar el *Analisis de resultados* para las actividades 4 a 10
- [ ] Escribir las conclusiones individuales de cada integrante
- [ ] **Actualizar las fuentes bibliograficas** en `referencias.bib`

---

## Estructura del proyecto

```
Lab_Micros/
├── Code/                # Codigos fuente en MicroPython
│   ├── act1.py          # Actividad 1  — Parpadeo basico
│   ├── act2.py          # Actividad 2  — Tiempos variables
│   ├── act3.py          # Actividad 3  — LED en GPIO 5
│   ├── act4.py          # Actividad 4  — GPIO 2 y GPIO 3
│   ├── act5.py          # Actividad 5  — GPIO 0 a GPIO 7
│   ├── act6.py          # Actividad 6  — 10 repeticiones
│   ├── act7.py          # Actividad 7  — LED viajero
│   ├── act8.py          # Actividad 8  — Llenado acumulativo
│   ├── act9.py          # Actividad 9  — Contador 8 bits
│   └── act10.py         # Actividad 10 — Semaforos
├── image/               # Imagenes del reporte
├── In/                  # Instrucciones de la practica
├── portada_img/         # Escudos UNAM / FI para la portada
├── PracticasPasadas/    # Practicas anteriores (1 y 2)
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
- El reporte utiliza diagramas de flujo en **TikZ** para las actividades completadas.
- La portada y el objetivo corresponden a la **Practica 3**.
- Las fuentes bibliograficas requieren actualizacion para reflejar la nueva practica.
