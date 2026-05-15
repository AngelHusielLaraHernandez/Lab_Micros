# Práctica 12 — Laboratorio de Microcomputadoras: Uso y Aplicaciones de WiFi

> **Plataforma Raspberry Pi Pico W (RP2040) — Programación en MicroPython con IDE Thonny**

---

## Objetivo

Comprender y aplicar la conectividad WiFi de la Raspberry Pi Pico W para implementar servidores web embebidos que permitan el control remoto de periféricos GPIO a través de interfaces HTML accesibles desde cualquier dispositivo en la red local.

---

## Actividades

| # | Descripción | Estado |
|:-:|-------------|:------:|
| 1 | Escaneo de redes WiFi disponibles | Pendiente |
| 2 | Conexión a una red WiFi existente | Pendiente |
| 3 | Servidor web básico con página HTML personalizada | Pendiente |
| 4 | Servidor web con control de 1 LED (GPIO18) via botones ON/OFF | Completa |
| 5 | Servidor web con control de 4 salidas GPIO independientes | Completa |
| 6 | Servidor web con control de 4 GPIO salida, 2 entrada digital, 1 analógica y PWM | Pendiente |

### Progreso general

Completadas: 2 / 6

---

## Contenido técnico

### Actividades 1-2: Conexión WiFi
- Escaneo de redes disponibles con `wlan.scan()`.
- Conexión en modo estación (STA_IF) a red existente.

### Actividades 3-4: Servidor web básico y control de LED
- Creación de socket TCP en puerto 80 (HTTP).
- Generación de interfaz HTML con botones de control.
- Análisis de peticiones HTTP GET para controlar GPIO.

### Actividades 5-6: Control múltiple y avanzado
- Control de 4 salidas GPIO desde interfaz web dinámica.
- Generación de HTML con bucles para escalabilidad.
- Integración de entradas digitales, analógicas y PWM.

---

## Estructura del proyecto

```text
Practica1/
├── Code/
│   ├── Act1.py          # Escaneo de redes WiFi
│   ├── Act2.py          # Conexión a red WiFi
│   ├── Act3.html        # Página HTML de la actividad 3
│   ├── Act4.py          # Servidor web control 1 LED
│   ├── Act5.py          # Servidor web control 4 LEDs
│   └── Act6.py          # Servidor web control avanzado
├── img/
│   ├── Actividad4/      # Evidencias actividad 4 (4 imágenes)
│   └── Actividad5/      # Evidencias actividad 5 (9 imágenes)
├── document/
│   └── Reporte_12_RPi_UsoyAplicacionesDeWiFi.pdf  # Rúbrica de evaluación
├── portada_img/         # Imágenes de la portada
├── PracticasPasadas/    # Prácticas anteriores (1-11)
│   ├── Practica1/
│   ├── Practica2/
│   ├── Practica3/
│   ├── Practica4/
│   ├── Practica5/
│   ├── Practica6/
│   ├── Practica7/
│   ├── Practica8/
│   ├── Practica9/
│   ├── Practica10/
│   └── Practica11/
├── main.tex             # Documento principal LaTeX
├── portada.tex          # Portada del reporte
├── referencias.bib      # Referencias bibliográficas
├── main.pdf             # Reporte compilado
└── README.md            # Este archivo
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
**Práctica:** 12 (Uso y Aplicaciones de WiFi)

---

## Notas importantes

- Este README corresponde a la práctica 12: Uso y Aplicaciones de WiFi.
- Las actividades 4 y 5 están completamente documentadas con propuesta de solución, diagramas de flujo TikZ, código comentado, evidencias fotográficas y análisis de resultados.
- Las prácticas anteriores (1-11) se encuentran archivadas en la carpeta `PracticasPasadas/`.
