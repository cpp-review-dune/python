# C++ Review DUNE

:::::::::::::: {.columns align=center totalwidth=8em}
::: {.column width="70%" align=center}

Es una _organización_ en GitHub con diversos recursos para aprender a
programar en C++ y Python con la caja de herramientas DUNE Numerics.

- \textcolor{red}{\faIcon{file-pdf}}\textcolor{AmurmapleGreen}{\href{https://cpp-review-dune.github.io/overview-2021/main.pdf}{Resumen del estudio de DUNE Numerics en el año 2021} \emoji{books} \emoji{laptop}}
- \textcolor{AmurmapleGreen}{\faIcon*[regular]{file}}Pad \href{https://hackmd.io/@cpp-review-dune/S1p2a43No}{\texttt{https://hackmd.io/@cpp-review-dune/S1p2a43No}}

\pause

## \textcolor{cyan}{\faIcon{telegram}} Grupo en Telegram Review Python PeC$^{3}$

- Compartir pantalla.
- Preferir los enlaces que los archivos `$(du -sh file.ext) < 5MiB`.
- Audio grupal.

Más información en [`https://telegram.org/blog/group-video-calls`](https://telegram.org/blog/group-video-calls).

:::
::: {.column width="30%" align=center}
\includegraphics[width=0.3\paperwidth]{2022-11-06/telegram.jpeg}
:::
::::::::::::::

:::::::::::::: {.columns align=center totalwidth=8em}
::: {.column width="70%" align=center}

## \textcolor{black}{\faIcon{github}} GitHub Discussions \emoji{speech-balloon}

- Adjuntar imágenes.
- Soporta resaltado de sintáxis de C++/Python.
- Debate de ideas.
- Responder preguntas y votar respuestas.
- [`https://github.com/cpp-review-dune/python/discussions`](https://github.com/cpp-review-dune/python/discussions).

Más información en [`https://docs.github.com/es/discussions`](https://docs.github.com/es/discussions).

:::
::: {.column width="30%" align=center}
\includegraphics[width=0.3\paperwidth]{2022-11-06/discussions.png}
:::
::::::::::::::

# Vistazo general de Python\faIcon{python}

En la actualidad, Python es un _lenguaje de scripting_

- favorito para **iniciarse en la programación**.
- preferido por los especialistas en la **seguridad informática**.
- **más utilizado** en la inteligencia artificial.
- de propósito general, multiparadigma, dinámicamente tipado e
**interpretado**.
- usado como _bindings_
(\textcolor{AmurmapleRed}{\href{https://cython.org}{\texttt{cython}}},
\textcolor{AmurmapleRed}{\href{https://pybind11.readthedocs.io}{\texttt{pybind11}}},
\textcolor{AmurmapleRed}{\href{https://nanobind.readthedocs.io}{\texttt{nanobind}}})
para otros lenguajes como C/C++/Fortran.
- desde la versión \texttt{3.10} está **enfocado en el rendimiento**,
con en el proyecto \textcolor{AmurmapleGreen}{\href{https://github.com/faster-cpython}{\texttt{github.com/faster-cpython}}}.
- prefiere el uso de **nombres en inglés** que símbolos, por ejemplo:
\textcolor{AmurmapleGreen}{\texttt{and}},
\textcolor{AmurmapleGreen}{\texttt{or}},
\textcolor{AmurmapleGreen}{\texttt{not}},
\textcolor{AmurmapleGreen}{\texttt{as}},
\textcolor{AmurmapleGreen}{\texttt{continue}},
\textcolor{AmurmapleGreen}{\texttt{finally}}.

<!-- 
Nació en la navidad de 1989 cuando
\textcolor{AmurmapleRed}{\href{https://www.imo-official.org/participant_r.aspx?id=10303}{Guido van Rossum}}
estudiaba en el Centro de Matemáticas y Computación en Holanda.
-->

\pause

\

Nuetras _reglas de programación_ serán:

1. Piense antes de programar.
2. Un programa es un ensayo legible por humanos sobre la resolución de
problemas que también se ejecuta en una computadora.
1. La mejor forma de mejorar sus habilidades de programación y
resolución de problemas es practicando.
1. Pruebe su código a menudo y a fondo.
2. Si fue difícil de escribir, posiblemente sea difícil de entender.
Agregue un comentario.
1. Toda entrada es mala hasta que se pruebe lo contrario.
2. Una _función_ debe realizar una sola tarea.
3. Asegúrese de que su nueva _clase_ pase las pruebas.

# Elementos especiales en Python\faIcon{python}

Las palabras clave, símbolos y caracteres que pueden ser usado en un
programa de Python son conocidos como *tokens*.

## \emoji{old-key} Palabras clave

Son palabras especiales que **no pueden usarse para nombrar** cosas.
Algunas de ellas son \textcolor{AmurmapleGreen}{\texttt{lambda}},
\textcolor{AmurmapleGreen}{\texttt{class}},
\textcolor{AmurmapleGreen}{\texttt{raise}},
\textcolor{AmurmapleGreen}{\texttt{try}},
\textcolor{AmurmapleGreen}{\texttt{return}},
\textcolor{AmurmapleGreen}{\texttt{import}},
\textcolor{AmurmapleGreen}{\texttt{yield}},
\textcolor{AmurmapleGreen}{\texttt{None}},
\textcolor{AmurmapleGreen}{\texttt{except}},
\textcolor{AmurmapleGreen}{\texttt{global}},
\textcolor{AmurmapleGreen}{\texttt{del}},
\textcolor{AmurmapleGreen}{\texttt{from}},
\textcolor{AmurmapleGreen}{\texttt{pass}},
\textcolor{AmurmapleGreen}{\texttt{with}},
\textcolor{AmurmapleGreen}{\texttt{break}},
\textcolor{AmurmapleGreen}{\texttt{is}},
\textcolor{AmurmapleGreen}{\texttt{def}}.

\pause

## \emoji{pager} Operadores

Son secuencias de caracteres que tiene un significado para el
intérprete de Python.
Su uso implica alguna operación como adición, sustracción o algo
similar.
Algunas de ellas son \textcolor{AmurmapleRed}{\texttt{+}},
\textcolor{AmurmapleRed}{\texttt{**}},
\textcolor{AmurmapleRed}{\texttt{//}},
\textcolor{AmurmapleRed}{\texttt{<>}}
\textcolor{AmurmapleRed}{\texttt{<<}},
\textcolor{AmurmapleRed}{\texttt{>>}},
\textcolor{AmurmapleRed}{\texttt{!=}},
\textcolor{AmurmapleRed}{\texttt{\%=}},
\textcolor{AmurmapleRed}{\texttt{\&=}},
\textcolor{AmurmapleRed}{\texttt{\~}}.

\pause

## \emoji{receipt} Puntuadores y delimitadores

Separan diferentes elementos en declaraciones y expresiones de
Python.
Algunos lo reconocerás de las matemáticas y otras del idioma inglés.
Algunos de ellos son \textcolor{AmurmapleRed}{\texttt{(}},
\textcolor{AmurmapleRed}{\texttt{)}},
\textcolor{AmurmapleRed}{\texttt{[}},
\textcolor{AmurmapleRed}{\texttt{]}},
\textcolor{AmurmapleRed}{\texttt{,}},
\textcolor{AmurmapleRed}{\texttt{:}},
\textcolor{AmurmapleRed}{\texttt{.}},
\textcolor{AmurmapleRed}{\texttt{=}},
\textcolor{AmurmapleRed}{\texttt{'}},
\textcolor{AmurmapleRed}{\texttt{"}},
\textcolor{AmurmapleRed}{\texttt{\textbackslash}},
\textcolor{AmurmapleRed}{\texttt{@}}.

\pause

## \emoji{abc} Literales

Es una notación para **representar un valor fijo**, el cual es un
valor que no puede cambiar en un programa.
En contraste a los literales, las variables y símbolos que puede
asignarse un valor que puede ser modificado durante la ejecución de
un código.
Por ejemplo, \texttt{123} es un literal, este es un valor fijo y no
puede ser modificado.

\pause

> Se recomienda seguir la guía de estilo para el código Python PEP 8
> y el uso de estos ayudantes como dev-dependencias:

- \textcolor{AmurmapleRed}{\href{https://github.com/hhatto/autopep8}{\texttt{autopep8}}}, formats Python code to conform to the PEP 8 style guide.
- \textcolor{AmurmapleRed}{\href{https://black.readthedocs.io}{\texttt{black}}}, _The uncompromising code formatter_.
- \textcolor{AmurmapleRed}{\href{https://beta.ruff.rs}{\texttt{Ruff}}}, _An extremely fast Python linter_.
- \textcolor{AmurmapleRed}{\href{https://mypy-lang.org}{\texttt{mypy}}}, _An optional static type checker for Python_.

# \emoji{bricks} Objetos y tipos

En programación, se habla de _ciudadanos de primera clase_ para
referirse a un elemento del lenguaje que posee la mayor cantidad de
privilegios dentro del mismo lenguaje.
Algunas de sus características son

- Aparecer en una expresión.
- Estar asignado a una variable.
- Ser usado como argumento.
- Ser devuelto por una llamada de función.

\pause

En Python, toda cosa en el sistema es considerado como un objeto.
Un objeto en Python tiene

- una identidad,
- algunos atributos,
- cero o más nombres.

Cada vez que Python crea un objeto, recibe un número de
identificación.

# Funciones Python\faIcon{python}

Las _funciones_ en los lenguajes de programación comparten muchas
características de las _funciones matemáticas_, pero agrega algunas
características que las hagan más útiles en la programación.
En particular, una función Python:

- representa **una sola operación** ha ser desarrollada.
- toma cero o más **argumentos** como entrada.
- **retorna un solo valor** (potencialmente un objeto compuesto) como
salida.

Una función es importante porque representa una _encapsulación_.
Por encapsulación, queremos decir que los detalles de una operación
se pueden ocultar, proporcionando operaciones más gruesas que
nosotros, como programadores, podemos usar sin tener que entender los
detalles internos de la función.

<!-- 
Considere la función $f\left(x\right)=\sqrt{x}$.
Si provee un valor particular de $x$, por ejemplo, $x=9$, la función
realizará el cálculo y retonará el valor asociado, por ejemplo $3$.
Los matemáticos .
 -->

En más detalle, las funciones proveen las siguientes características
que ayudan en la programación:

- Resolución de problema divide y vencerás: dividen los programas en
partes más pequeñas.
- Abstracción: proporcionan una interfaz de operación de nivel
superior que la función.

# \emoji{glowing-star} ¿Cuándo usar una función?

Según [@Punch2017], estas son algunas pautas que pueden resultar útil.

- **Hacer una sola cosa y bien**:
la función debe ser la encapsulación de una única operación,
funciones que intenten hacer también muchas cosas son candidatas a
ser divididas en múltiples funciones (refactorizadas).
- **Legible**.
- **No demasiado largo**:
Si la función es demasiado larga, es posible que debe dividirse en
múltiples funciones.
- **Reutilizable**:
De ser posible, la función debe ser autónoma y no depende de algún
matiz de una llamada del programa.
Si tiene dependencias, estas deben ser explícitas para que otros
puedan usarlo fácilmente.
- **Completo**:
Asegúrse que funcione en todas las situaciones posibles y tenga en
cuenta todos los casos que podría usarse.
- **Refactorización**:
Es el proceso de tomar el código existente y modificarlo de manera
que su estructura mejore de alguna manera conservando la misma
funcionalidad.

\

Algunas veces escribimos funciones sin la declaración return.
Las funciones que no retornan un valor son llamadas procedimientos.
En ese caso retorna None que representa la nada.

## Archivos y excepciones

Un archivo es una colección de bytes que usualmente reside en el
disco.
Los archivos soportan tanto la codificación ASCII como Unicode.

### Referencias

<!--

# NumPy Comunicación (8:00 - 8:50)

Python permite dos formas de comentarios

\footnotesize
\inputminted[firstline=1, lastline=1]{python}{2022-11-06/main.py}

\normalsize

Un *objeto* puede ser pensado como una región de la memoria RAM de
la computadora que contiene algún dato e información asociada con
estos datos.
Esta información consiste de su *tipo* y su *identificador*

\footnotesize
\inputminted[firstline=3, lastline=8]{python}{2022-11-06/main.py}

Esta lista es llamado espacio de nombre, y como este es un objeto,
tiene su identificador.

```python
import foo
from foo import obj1, obj2
from foo import *
import math as re
import cmath as co
```

\footnotesize
\inputminted[firstline=10, lastline=11]{python}{2022-11-06/main.py}

### Descanso (8:50 - 9:00)

```
<identificador> = <objeto>
```

```python
<identificador> = <objeto>
```

\footnotesize
\inputminted[firstline=13, lastline=19]{python}{2022-11-06/main.py}

Las clases son estructuras extremedamente versátiles en Python.
La idea básica es que pueda tener una estructura de datos fija u
objeto que ocurre con frecuencia, junto con operaciones directamente
asociadas en él.
La clase encapsula tanto el objeto como sus operaciones.

### Práctica (9:00 - 9:50)

\footnotesize
\inputminted[firstline=1, lastline=12]{python}{2022-11-06/fraction.py}

### Temario

Repaso de las estructuras del Python

Introducción a la Programación orientada a Objetos

Aplicación

Gestión de errores, buenas prácticas de programación

Operaciones escalares, vectoriales y matriciales

Álgebra lineal y sistema de ecuaciones lineales

Aplicación

Lectura y escritura de datos en diversos formatos

Gráficos en 2D, 3D, simulaciones

Aplicación

Diferenciación e Integración Numérica

Ecuación diferencial

Matemática simbólica

Estadística descriptiva

Regresión lineal simple y multivariada

Python es un lenguaje sencillo y orientado a objetos, que permite el
desarrollo de aplicaciones en diversas áreas, como seguridad, acceso
a bases de datos, aplicaciones cliente-servidor, interfaces gráficas,
páginas Web interactivas, Análisis de Datos y Aplicaciones deIngeniería

Creado por Guido Van Rossum en 1996, como descendiente del lenguaje
ABC e inspirado en otros lenguajes, formalmente propuesto desde 1991

Ciencias e Ingeniería

• Por diversas razones históricas y culturales, Python ha
desarrollado una comunidad de computación científica y análisis de
datos grandes y activa.
En los últimos 20 años, Python ha pasado de ser un lenguaje
informático científico de vanguardia o "bajo su propio riesgo" a uno
de los lenguajes más importantes para la ciencia de datos, el
aprendizaje automático y eldesarrollo de software en general en la
academia y la industria.
• Python inevitablemente se compara con MATLAB, C, C++, Java y otros.
En los últimos años, las bibliotecas de código abierto mejoradas de
Python (como NumPy, SciPy, Matplotlib, SymPy, Statsmodels, etc.) lo
han convertido en una opción popular para las tareas en ciencias e
ingeniería.
-->