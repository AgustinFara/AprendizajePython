## **Python Aprendizaje**


<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png" alt="logo python" width="200" height="200"></img>

Este repositorio contiene código python de aprendizaje. 

Autor: Agustín Fara

---

#### Listado de Archivos

1. 01-holamundo.py
    - *Primer práctica de todo lenguaje de programación, print de holamundo en consola.*
    
2. 02-variables.py
    - *Definición de difernetes tipos de variables(str,int, float, bool y clase date).*
    
3. 03-funciones.py
    - *Función que toma dos argumentos e imprime un string.*
        
4. 04-funcionconretorno.py
    - *Función que retorna un valor. Funcion que devuelve porcentual y función que calcula cotización del dólar.*
    - *Algunas operaciones con valores numericos*

5. 05-list(array).py
    - *Ejemplo videoclub donde Genero 2 list (de peliculas y stock) para luego imprimir un listado con las alquiladas y las disponibles.*
    - *Ordeno list Peliculas y lo imprimo.*

6. 06-Iteradores.py
    - *Distintas formas de ejecutar un for*

7. 07-condicionales.py
    - *if, else, elif, distintos ejemplos* 

8. 08-dics(objetos).py
    - *crear diccionario, modificar y eliminar valores* 


```
Metallica
Enter Sandman
Black Album
1992
{'artista': 'Metallica', 'nombre': 'Enter Sandman', 'album': 'Black Album', 'año de Lanzamiento': 1992, 'genero': 'Heavy Metal'}
{'artista': 'Metallica', 'nombre': 'Nothing else Matters', 'album': 'Black Album', 'año de Lanzamiento': 1992, 'genero': 'Heavy Metal'}
Heavy Metal
No existe el Valor

VALORES CANCIÓN
artista : Metallica
nombre : Nothing else Matters
album : Black Album
año de Lanzamiento : 1992
```


9. 09-input.py
    - *distintas operaciones con input de datos* 


```
Cual es tu nombre:
Donald
¡Hola Donald!
Donald, ¿Cual es tu edad?:
44
Donald, ya puedes votar
Donald, ¿Cual es tu día de nacimiento?:
21
Donald, tu día de nacimiento es inpar
```


10. 10-mySqlConnect.py
    - *Accede a la base Mysql local y hace un select * de la tabla tipeada* 


```
que tabla quiere consultar?:
libros
(1, 'OTRAS INQUISICIONES', 'OTRAS INQUISICIONES', 1952, 2005, 288, 19, '9500427001', None, 1, 1, 1, 'AJF', datetime.datetime(2020, 11, 19, 17, 28, 17), 'AJF', datetime.datetime(2020, 11, 19, 17, 28, 17))
(2, 'LA CASA DE LAS BELLAS DURMIENTES', 'NEMURERU BIJO', 1961, 2011, 128, 1, None, '9789500433273', 2, 1, 1, 'AJF', datetime.datetime(2020, 11, 19, 17, 40, 34), 'AJF', datetime.datetime(2020, 11, 19, 17, 40, 34))
(3, 'BESTIARIO', 'BESTIARIO', 1951, 2006, 136, 2, None, '9879870406044', 3, 2, 1, 'AJF', datetime.datetime(2020, 11,
19, 17, 53, 12), 'AJF', datetime.datetime(2020, 11, 19, 17, 53, 12))
```


11. 08-dics(objetos).py
    - *Conección con la API de Wikipedia para tomar el extracto del articulo sobre Jorge Luis Borges* 


```
Jorge Francisco Isidoro Luis Borges (Buenos Aires, 24 de agosto de 1899-Ginebra, 14 de junio de 1986) fue un escritor de cuentos, ensayos y poemas argentino, extensamente considerado una figura clave tanto para la literatura en habla
hispana como para la literatura universal.[2]​ Sus dos libros más conocidos, Ficciones y El Aleph, publicados en los
años cuarenta, son recopilaciones de cuentos conectados por temas comunes, como los sueños, los laberintos, las bibliotecas, los espejos, los autores ficticios y la mitología europea, con argumentos que exploran ideas filosóficas relacionadas, por ejemplo, con la memoria, la eternidad, la posmodernidad y la metaficción.[3]​ Las obras de Borges han c
ontribuido ampliamente a la literatura filosófica, al género fantástico y al posestructuralismo. Según marcan numerosos críticos, el comienzo del realismo mágico en la literatura hispanoamericana del siglo XX se debe en gran parte a su obra.[4]​
Habiendo nacido en un suburbio de Buenos Aires, Borges se mudó a Suiza con su familia en 1914, donde estudió en el Collège de Genève. La familia viajaría extensamente por Europa, incluyendo España. Tras su regreso a Argentina en 1921, Borges empezó a publicar sus poemas y ensayos en revistas literarias surrealistas mientras trabajaba como bibliotecario, profesor y conferencista. En 1955 fue nombrado director de la Biblioteca Nacional de la República Argentina y profesor de literatura inglesa en la Universidad de Buenos Aires. A la edad de 55 años quedó completamente ciego; numerosos investigadores han sugerido que su ceguera progresiva lo motivó a crear símbolos literarios innovadores a través de la imaginación.[5]​
Durante los años sesenta, su trabajo fue traducido y publicado en los Estados Unidos y en Europa. En 1961 llegó a la
fama internacional al obtener el primer Premio Formentor, que recibió junto a Samuel Beckett. En 1971 ganó el Premio
Jerusalén; su reputación internacional se consolidó entre estos años, ayudado por la disponibilidad de las traducciones al inglés de su obra, por el éxito de Cien años de soledad de García Márquez y por el boom latinoamericano, aunque su participación en él es relativa.[6]​[7]​ Borges dedicó su último libro, Los conjurados, a la ciudad de Ginebra, d
onde moriría en 1986.[8]​ El escritor y ensayista J. M. Coetzee dijo en su libro sobre Borges que: «Él, más que nadie
, renovó el lenguaje de la ficción, abriendo así el camino a una generación de novelistas hispanoamericanos».[9]​
Galardonado con numerosas distinciones,[10]​ fue también polémico por sus posturas políticas conservadoras; su import
ancia continúa siendo causa de debate, particularmente por la posibilidad de que estas le hayan impedido obtener el Premio Nobel de Literatura,[11]​[12]​ al que fue candidato durante casi treinta años.
```


12. 12-configinigenerator.py
    - *Genera un nuevo archivo config.ini con los parametros pedidos* 

13. 13-sendmail.py
    - *Envia un mail con HTML* 


email_raw.eml
```HTML
From: Private Person <from@smtp.smtpman.com> 
To: A Test User <to@smtp.smtpman.com> 
MIME-Version: 1.0 
Content-type: text/html 
Subject: Email HTML enviado desde Python 

Hola!<br/> <br/> 
Este es un <b>e-mail</b> enviando desde <b>Python</b> 
```

14. 14-getapiisbn.py
    - *Llama a la API de openlibrary para tomar los datos de un libro a partir del ISBN* 

```
ingrese un ISBN 13:
9788492966790
Una breve historia de casi todo - 6. edicion
['R B A']
2018
['9788492966790']
```

15. 15-classes.py
    - *Definición de clases, atributos y métodos en Python* 
    - *Ejemplos de encapsulamiento, getters y setters, herencia y polimorfismo* 

```
clase Restaurant objeto 1
Me construyo con el constructor
Nombre: Spiagge di Napoli

clase Restaurant objeto 2
Me construyo con el constructor
Nombre: McPython's

clase Banco objeto 1
Nombre: Banco ITAU de Brasil, totaliza el 12% del porcentaje de clientes de la Argentina

clase Banco objeto 2
Nombre: Banco Macro de Argentina, totaliza el 10% del porcentaje de clientes de la Argentina

clase Banco objeto 1(Se cambiaron los atributos por medio de métodos)
Nombre: Banco Piano de Argentina, totaliza el 7% del porcentaje de clientes de la Argentina

clase Banco objeto 2(metodos get de atributos)
Banco Macro
Argentina
10%

clase Restaurant accedida desde fuera del objeto(Atributos public)
Mostrar: Spiagge di Napoli
Mostrar: McPython's

clase Hotel, herencia de clase Banco
Nombre: Hyatt de USA, totaliza el 2% del porcentaje de clientes de la Argentina

clase Hotel, accedo a atributo nuevo clase hotel
Hotel de ***** estrellas
```


16. 16-archivos.py
    - *Generar archivo y luego leerlo* 

```
Esta es la linea: 1
Esta es la linea: 2
Esta es la linea: 3
Esta es la linea: 4
Esta es la linea: 5
Esta es la linea: 6
Esta es la linea: 7
Esta es la linea: 8
Esta es la linea: 9
Esta es la linea: 10
Esta es la linea: 11
Esta es la linea: 12
Esta es la linea: 13
Esta es la linea: 14
Esta es la linea: 15
Esta es la linea: 16
Esta es la linea: 17
Esta es la linea: 18
Esta es la linea: 19
Esta es la linea: 20
```
17 Proyecto Consola (Agenda.py)
        - *Una aplicacion de consola que guarda contactos(nombre, telefono y cumpleaños) en distintos archivos y permite todas las opciones de CRUD (Create, Read, Update y Delete*)
    

```
Indique la opción deseada
------- -- ------ -------

1 - Agregar nuevo Contacto
2 - Editar contacto
3 - Ver contactos
4 - Buscar contacto
5 - Eliminar contacto
6 - Salir

Ingrese el número deseado: 1
```

```
Ingrese los datos del nuevo Contacto
------- --- ----- --- ----- --------
Nombre completo: Neurus
Teléfono: 12-123-4567
Ingrese una fecha de cumpleaños formato AAAA.MM.DD: 1967.1.1
```

```
El contacto: Neurus se guardo correctamente
Presione una tecla para continuar...
```

```
Indique la opción deseada
------- -- ------ -------

1 - Agregar nuevo Contacto
2 - Editar contacto
3 - Ver contactos
4 - Buscar contacto
5 - Eliminar contacto
6 - Salir

Ingrese el número deseado: 2
```
```
Ingrese los datos del  Contacto a Editar
------- --- ----- ---  -------- - ------
Nombre completo: Neurus
```

```
PRESIONE ENTER SI DESEA MANTENER EL DATO GUARDADO
Nombre completo(Neurus), escriba el nuevo: profesor neurus
```

```
PRESIONE ENTER SI DESEA MANTENER EL DATO GUARDADO
Teléfono(12-123-4567), escriba el nuevo:
```

```
PRESIONE ENTER SI DESEA MANTENER EL DATO GUARDADO
Cumpleaños(01/01/1967), escriba el nuevo AAAA.MM.DD:
```

```
El contacto: Profesor Neurus se modificó correctamente
Presione una tecla para continuar...
```

```
Indique la opción deseada
------- -- ------ -------

1 - Agregar nuevo Contacto
2 - Editar contacto
3 - Ver contactos
4 - Buscar contacto
5 - Eliminar contacto
6 - Salir

Ingrese el número deseado: 3
```

```
Daisy Duck
----- ----
Teléfono: 10-333-4321
Cumpleaños: 07/06/1940

Presione una tecla para continuar...
```

```
Donald Fauntleroy Duck
------ ---------- ----
Teléfono: 10-123-4567
Cumpleaños: 03/05/1934

Presione una tecla para continuar...
```

```
Dumbella Duck
-------- ----
Teléfono: 08-005-7876
Cumpleaños: 17/10/1937

Presione una tecla para continuar...
```

```
Fethry Duck
------ ----
Teléfono: 12-1111-1567
Cumpleaños: 02/08/1964

Presione una tecla para continuar...
```

```
Gladstone Gander
--------- ------
Teléfono: 77-777-2020
Cumpleaños: 15/01/1948

Presione una tecla para continuar...
```

```
Profesor Neurus
-------- ------
Teléfono: 12-123-4567
Cumpleaños: 01/01/1967

Presione una tecla para continuar...
```

```
Professor Ludwig Von Drake
--------- ------ --- -----
Teléfono: 18-111-2020
Cumpleaños: 24/09/1961

Presione una tecla para continuar...
```

```
Scrooge Mcduck
------- ------
Teléfono: 12-222-1234
Cumpleaños: 01/12/1947

Presione una tecla para continuar...
```

```
Indique la opción deseada
------- -- ------ -------

1 - Agregar nuevo Contacto
2 - Editar contacto
3 - Ver contactos
4 - Buscar contacto
5 - Eliminar contacto
6 - Salir

Ingrese el número deseado: 4
```

```
Ingrese los datos del  Contacto a Buscar
------- --- ----- ---  -------- - ------
Nombre completo: profesor NeUruS
```

```
Profesor Neurus
-------- ------
Teléfono: 12-123-4567
Cumpleaños: 01/01/1967

Presione una tecla para continuar...
```

```
Indique la opción deseada
------- -- ------ -------

1 - Agregar nuevo Contacto
2 - Editar contacto
3 - Ver contactos
4 - Buscar contacto
5 - Eliminar contacto
6 - Salir

Ingrese el número deseado: 5
```

```
Ingrese los datos del  Contacto a Borrar
------- --- ----- ---  -------- - ------
Nombre completo: profesor neurus
```

```
Profesor Neurus
-------- ------
Teléfono: 12-123-4567
Cumpleaños: 01/01/1967

Esta seguro que desea eliminar este contacto? S o N: S
```

```
El contacto: profesor neurus fue eliminado
Presione una tecla para continuar...
```

```
Indique la opción deseada
------- -- ------ -------

1 - Agregar nuevo Contacto
2 - Editar contacto
3 - Ver contactos
4 - Buscar contacto
5 - Eliminar contacto
6 - Salir

Ingrese el número deseado: 6
```

```
Saliendo de la aplicación
Presione una tecla para continuar...
```




