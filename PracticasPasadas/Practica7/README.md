# Práctica 7 — Laboratorio de Microcomputadoras: Comunicación Serial Asíncrona y Módulo Bluetooth

> **Plataforma Raspberry Pi Pico (RP2040) — Programación en MicroPython con IDE Thonny**

---

## Objetivo

Aprender el funcionamiento de la comunicación serial en la modalidad asíncrona para la transferencia de información entre diferentes dispositivos por medios alámbricos e inalámbricos.

---

## Actividades

| # | Descripción | Estado |
|:-:|-------------|:------:|
| 1 | Lectura asíncrona no bloqueante de puerto serie usando `sys.stdin` y `select.poll` | Completada |
| 2 | Uso y configuración del puerto COM del microcontrolador con una terminal serial | Completada |
| 3 | Control de LED integrado (GPIO25) enviando comandos ASCII ('0' y '1') por UART | Completada |
| 4 | Comunicación serial mediante módulo USB-TTL externo (CP2102) | Completada |
| 5 | Menú serial complejo: Lectura de sensores (ADC, Temp) y control de salidas | Completada |
| 6 | Configuración e implementación de control inalámbrico a través de módulo Bluetooth | Completada |
| 7 | Control de motores de Corriente Directa (giro y paro) vía Bluetooth en puente H | Completada |

### Progreso general

\Completadas : [####         ] 2 / 7
Pendientes  : [ ##########   ] 5 / 7
\
> **Nota:** Todas las actividades incluyen códigos fuente en MicroPython comentados, análisis de resultados (incluyendo redacción actualizada y natural) y se elaboraron **diagramas de flujo funcionales en TikZ para las actividades 1 y 3**, detallando el funcionamiento del flujo de datos en el reporte LaTeX.

---

## Contenido técnico

### Actividades 1-3: Comunicación UART Alámbrica y Polling Asíncrono
- Recepción de datos \sys.stdin.read()- Implementación de bucles no bloqueantes usando el módulo \select- Control de estados digitales locales mediante el envío de caracteres

### Actividades 4-5: Interfaz Avanzada y Módulos Externos USB-Serial
- Implementación e integración del módulo CP2102
- Enrutamiento complejo de comandos ASCII hacia componentes periféricos (ADC, Temp, Zumbador, LEDs)

### Actividades 6-7: Conectividad Inalámbrica (Bluetooth) y Potencia
- Integración de módulo serial Bluetooth (tipo HC)
- Parseo de arrays y strings provenientes de la App ('A', 'T', 'S', 'D', 'I')
- Interfaz inalámbrica aplicada al manejo lógico de Motores C.D.

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

## Diagramas incluidos

El reporte incluye los siguientes diagramas lógicos actualizados elaborados en **TikZ**:

| Tipo | Actividad | Descripción |
|------|-----------|-------------|
| **Flujograma** | **Actividad 1** | Representación del ciclo infinito asíncrono para detección de teclas en buffer |
| **Flujograma** | **Actividad 3** | Lógica computacional del parseo de comandos '0' y '1' para estado bidireccional del PIN 25 |

---

## Compilación del reporte

\\ash
# Compilación completa utilizando bibliografías y dependencias (recomendada)
latexmk -pdf main.tex
\
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

- Esta práctica reemplaza los conceptos de PWM pasados y corresponde de forma íntegra a comunicaciones asíncronas y configuración de módulos Bluetooth.
- Se modificaron los análisis de resultados para mayor ligereza.
- Se adaptó la conclusión y perspectiva individual de *Angel Husiel Lara Hernandez* en formato estructurado de párrafos.
- Los códigos fueron depurados y se ubican listos para ejecución en \Code/\.

---

## Componentes principales
- Raspberry Pi Pico (RP2040)
- Módulo Interfaz USB-TTL CP2102
- Módulo Bluetooth Inalámbrico (Recepción serial)
- Puente H para Motores C.D.
- Sensores y actuadores secundarios (TMP36, Zumbador, LEDs, Resistencias)
