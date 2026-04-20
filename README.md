# Práctica 8 — Laboratorio de Microcomputadoras: Comunicación SPI y control de pantallas

> **Plataforma Raspberry Pi Pico (RP2040) — Programación en MicroPython con IDE Thonny**

---

## Objetivo

Aprender el funcionamiento de la comunicación SPI; realizar comunicación entre diferentes componentes por medio de la comunicación serie síncrona en la modalidad SPI, y estudiar librerías para controlar pantallas SPI.

---

## Actividades

| # | Descripción | Estado |
|:-:|-------------|:------:|
| 1 | Control del display MAX7219 de 8 dígitos con mensajes predefinidos | Completada |
| 2 | Control del display de 8 dígitos mediante GPIO12 y GPIO13 | Completada |
| 3 | Control de la matriz MAX7219 de 4 módulos 8x8 | Completada |
| 4 | Despliegue secuencial de mensajes en la matriz SPI | Completada |
| 5 | Manejo del display TFT ST7735 con texto a color | Completada |
| 6 | Despliegue de nombres del equipo en pantalla TFT | Completada |
| 7 | Contador compartido en display TFT, matriz 8x8 y display de 8 dígitos | Completada |

### Progreso general

\Completadas : [#######        ] 3 / 7
Pendientes  : [#######         ] 4 / 7
\
> **Nota:** Todas las actividades incluyen códigos fuente en MicroPython comentados, análisis de resultados con redacción actualizada, y se elaboraron **diagramas de flujo funcionales en TikZ para las actividades 4, 5 y 7**, detallando el flujo de datos y control en el reporte LaTeX.

---

## Contenido técnico

### Actividades 1-3: Control de pantallas MAX7219
- Despliegue de texto en display de 8 dígitos mediante SPI.
- Control ascendente y descendente con entradas digitales GPIO12 y GPIO13.
- Manejo de una matriz 4x8x8 con mensajes programados.

### Actividades 4-5: Diagramas de flujo y control de TFT
- Despliegue secuencial de mensajes en la matriz SPI.
- Configuración e inicialización del display TFT ST7735.
- Escritura de texto estático con color, posición y escala.

### Actividades 6-7: Integración visual de múltiples salidas
- Despliegue de nombres del equipo en la TFT.
- Contador simultáneo en TFT, matriz 8x8 y display de 8 dígitos.
- Compartición del bus SPI con selección de chip independiente.

---

## Estructura del proyecto


```
Practica1/
├── Code/                    # Códigos fuente en MicroPython
│   ├── Ac1SinNombres.py     # Código base sin comentarios (Act. 1)
│   ├── Act1.py              # Actividad 1 — Display MAX7219 de 8 dígitos
│   ├── Act2.py              # Actividad 2 — Control con GPIO12 y GPIO13
│   ├── Act3.py              # Actividad 3 — Matriz MAX7219 4x8x8
│   ├── Act4.py              # Actividad 4 — Mensajes secuenciales en matriz SPI
│   ├── Act5SinNombre.py     # Código base sin comentarios (Act. 5)
│   ├── Act5.py              # Actividad 5 — TFT ST7735 con texto a color
│   ├── Act6.py              # Actividad 6 — Nombres del equipo en TFT
│   └── Act7.py              # Actividad 7 — Contador compartido en tres pantallas
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

## Diagramas incluidos

El reporte incluye los siguientes diagramas lógicos actualizados elaborados en **TikZ**:

| Tipo | Actividad | Descripción |
|------|-----------|-------------|
| **Flujograma** | **Actividad 4** | Recorrido secuencial de mensajes en la matriz MAX7219 con limpieza y retardo controlado |
| **Flujograma** | **Actividad 5** | Inicialización completa del TFT ST7735 y despliegue de texto a color |
| **Flujograma** | **Actividad 7** | Lógica del contador compartido para tres dispositivos SPI con botones de control |

---

## Compilación del reporte

```bash
latexmk -pdf main.tex
```

Si prefieres compilar paso a paso:

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
**Fecha de entrega:** 12 de Abril del 2026

---

## Notas importantes

- Esta práctica se centra en la comunicación SPI compartida y el control de pantallas MAX7219 y TFT ST7735.
- Se incorporaron diagramas de flujo en TikZ para las actividades 4, 5 y 7.
- Se actualizó la conclusión personal de *Lara Hernandez Angel Husiel* para reflejar el trabajo realizado en esta práctica.
- Los códigos fuente se ubican listos para ejecución en \Code/\.

---

## Componentes principales
- Raspberry Pi Pico (RP2040)
- Display MAX7219 de 8 dígitos
- Matriz MAX7219 de 4 módulos 8x8
- Display TFT ST7735
- Resistencias, cables y conexiones SPI compartidas
