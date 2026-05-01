# Práctica 9 — Laboratorio de Microcomputadoras: Comunicación One Wire

> **Plataforma Raspberry Pi Pico (RP2040) — Programación en MicroPython con IDE Thonny**

---

## Objetivo

Conocer diversos protocolos de comunicación One Wire para el control de dispositivos a través de la plataforma Raspberry Pi Pico.

---

## Actividades

| # | Descripción | Estado |
|:-:|-------------|:------:|
| 1 | Estudio de librería para control de tira Neopixel | Completada |
| 2 | Secuencia de 8 LEDs RGB en patrón ascendente/descendente | Completada |
| 3 | Implementación de reloj con display TM1637 | Completada |
| 4 | Contador descendente con activación de zumbador | Completada |
| 5 | Lectura base de sensor DS18B20 | Completada |
| 6 | Lectura DS18B20 en °C y conversión a °F | Completada |
| 7 | Estudio de librería y lectura con sensor DHT11 | Completada |
| 8 | Detección de incremento térmico de referencia con DHT11 | Completada |
| 9 | Integración final: semáforos, sensores y display TM1637 | Completada |

### Progreso general

Completadas: 9 / 9

> **Nota:** El reporte incluye propuesta, desarrollo y análisis por actividad. En esta versión se integraron diagramas de flujo TikZ completos para las actividades 3, 6 y 9, alineados con su implementación en código.

---

## Contenido técnico

### Actividades 1-2: Neopixel y secuencias RGB
- Configuración de tira direccionable en Raspberry Pi Pico.
- Manejo de patrones temporizados con cambios de color.

### Actividades 3-4: Control con TM1637 y actuadores
- Reloj digital con parpadeo de separador central.
- Temporización de cuenta regresiva y activación de zumbador.

### Actividades 5-6: Sensado de temperatura con One Wire
- Detección de dispositivos DS18B20 por dirección ROM.
- Conversión de temperatura de °C a °F y visualización por consola.

### Actividades 7-8: Sensado ambiental con DHT11
- Lectura de temperatura/humedad con librería dedicada.
- Comparación con umbral térmico para control de salida.

### Actividad 9: Integración de sistema embebido
- Secuencia de semáforos con Neopixel.
- Ventana de monitoreo térmico con DS18B20 y DHT11.
- Cambio de modo de sensor mediante interrupción por botón.
- Despliegue de temperatura en TM1637 con identificación de fuente.

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
│   └── Act9.py
├── img/
│   ├── Actividad1/
│   ├── Actividad2/
│   ├── Actividad3/
│   ├── Actividad4/
│   ├── Actividad5/
│   ├── Actividad6/
│   ├── Actividad7/
│   ├── Actividad8/
│   └── Actividad9/
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

## Diagramas de flujo incluidos

| Tipo | Actividad | Descripción |
|------|-----------|-------------|
| Flujograma | Actividad 3 | Lógica de reloj MM:SS en TM1637 con acarreo de segundos y minutos |
| Flujograma | Actividad 6 | Lectura DS18B20, conversión térmica y salida en °C/°F |
| Flujograma | Actividad 9 | Integración de semáforos, doble ruta de sensores y manejo de excepción |

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
**Práctica:** 9 (Comunicación One Wire)

---

## Notas importantes

- Este README corresponde a la práctica 9 y sustituye la descripción previa de SPI.
- Se actualizaron las secciones de propuesta para actividades 3, 6 y 9 con diagramas TikZ y flujo de datos.
- La conclusión de Lara Hernandez Angel Husiel fue completada en la sección de conclusiones del reporte.
