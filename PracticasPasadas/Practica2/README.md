# Practica 2 - Laboratorio de Microcomputadoras

Reporte en LaTeX para la Practica 2: Programacion en Ensamblador. Direccionamiento Indirecto.

## Objetivo

Programar las variantes del modo de direccionamiento indirecto existentes para los procesadores ARM.

## Instrucciones

Las instrucciones completas para la elaboracion del reporte se encuentran en:

```
in/Reporte_02_RPi_ProgramaciónEnEnsamblador_direccionamientoIndirecto.pdf
```

## Actividades

- Actividad 1: Escribir, comentar, compilar y comprobar el funcionamiento del programa base.
- Actividad 2: Modificar la actividad 1 usando direccionamiento indexado con el doble de datos.
- Actividad 3: Copiar un arreglo de 32 bits con 16 elementos en sentido inverso.
- Actividad 4: Generar un arreglo de 20 elementos (i, 2i, 4i, ...), y sumar el resultado.
- Actividad 5: Multiplicar dos matrices de 2x2 con datos de 8 bits.
- Actividad 6: Encontrar el valor mayor en un arreglo de 20 elementos y su direccion.
- Actividad 7: Ordenar ascendentemente un arreglo de 32 elementos de 32 bits y copiarlo.

## Estructura del proyecto

```
Practica1/
├── Codigos/          # Archivos fuente en ensamblador (.s)
│   ├── Act1.s
│   ├── Act2.s
│   ├── Act3.s
│   ├── Act4.s
│   ├── Act5.s
│   ├── Act6.s
│   └── Act7.s
├── img/              # Imagenes utilizadas en el reporte
│   ├── Actividad/
│   ├── Actividad1/
│   ├── Actividad2/
│   ├── Actividad3/
│   ├── Actividad4/
│   ├── Actividad5/
│   ├── Actividad6/
│   └── Actividad7/
├── in/               # Instrucciones del reporte
│   └── Reporte_02_RPi_ProgramaciónEnEnsamblador_direccionamientoIndirecto.pdf
├── portada_img/      # Imagenes de la portada (escudos UNAM/FI)
├── %OUTDIR%/         # Archivos generados de compilacion
├── Practica1/        # Subcarpeta con archivos duplicados del proyecto
├── main.tex          # Documento principal de LaTeX
├── portada.tex       # Portada del reporte
├── referencias.bib   # Bibliografias del reporte
├── main.pdf          # PDF generado
├── main.bbl
├── main.fdb_latexmk
└── main.synctex.gz
```

## Uso

Compilar el reporte con:

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

O usar `latexmk`:

```bash
latexmk -pdf main.tex
```

## Notas importantes

- Las actividades y sus codigos se encuentran en la carpeta `Codigos/`.
- La portada y el objetivo ya corresponden a la Practica 2.
