## \emoji{snake} NumPy[^1]

### Comunicación (8:00 - 8:50)

Python permite dos formas de comentarios

\footnotesize
\inputminted[firstline=1, lastline=1]{python}{2022-11-06/main.py}

\normalsize

Un *objeto* puede ser pensado como una región de la memoria RAM de la computadora que contiene algún dato e información asociada con estos datos.
Esta información consiste de su *tipo* y su *identificador*

\footnotesize
\inputminted[firstline=3, lastline=8]{python}{2022-11-06/main.py}

Esta lista es llamado espacio de nombre, y como este es un objeto, tiene su identificador.

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