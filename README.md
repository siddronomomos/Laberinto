# Laberinto-

**Fernando Daniel Padilla Gonzalez, hace front end **

Representación visual del laberinto:

Utilizarpy game para mostrar visualmente el laberinto en la pantalla.

Representar cada tipo de celda con colores o símbolos distintivos:
Camino (0): Blanco o un color claro.
Pared (1): Negro o un color oscuro.
Salida (2): Verde o un color de destino.
Teletransportación (3 y 4): Colores brillantes para destacar su función especial.
Celda de acertijo (111): Un símbolo especial o color distintivo.

Interacción con el usuario:

Implementar la interfaz gráfica que permita al usuario iniciar la exploración del laberinto.
Añadir una opción para que el usuario ingrese las respuestas de los acertijos cuando llegue a una celda especial (111).
Mostrar los movimientos en tiempo real a medida que el algoritmo explora el laberinto.

Animación y visualización de la búsqueda:

Desarrollar una animación para visualizar cómo el algoritmo va explorando el laberinto, mostrando cada paso del proceso.
Marcar el camino explorado por el algoritmo con una línea o colores que se actualicen conforme avance.

Indicadores de progreso:

Implementar un indicador visual para mostrar si el explorador está en una celda teletransportadora, acertijo, o si se ha quedado sin salida.
Añadir mensajes que indiquen al usuario cuando ha llegado a la salida o cuando ha fallado en encontrar una ruta.

Mensajes de éxito o error:

Mostrar un mensaje cuando el algoritmo haya encontrado la salida o si ha fallado en su búsqueda.
En el caso de las celdas de acertijo, mostrar un cuadro de diálogo que permita al usuario interactuar con la pregunta.

GUI y controles:

Crear una interfaz gráfica que permita al usuario:
Reiniciar el laberinto.
Cargar diferentes laberintos.
Ver soluciones paso a paso.
Agregar botones o teclas de acceso rápido para pausar, avanzar, o retroceder en la exploración del laberinto.

Compatibilidad y usabilidad:

Asegurarse de que la interfaz sea compatible con diferentes tamaños de pantalla y dispositivos (computadora, tablet, móvil).
Probar la usabilidad de la interfaz y hacer ajustes según sea necesario para mejorar la experiencia del usuario.

**Entregables**

Frontend

Interfaz gráfica que muestre el laberinto y permita visualizar la solución.
Controles para interactuar con la solución y visualizar la exploración paso a paso.
Animaciones que muestren el progreso del algoritmo y las reglas especiales.

**Cronograma de Commits**

Commit 1 (9 de octubre):

Backend: Creación de la estructura del laberinto, matriz y reglas básicas.
Frontend: Primera representación gráfica del laberinto.

Commit 2 (14 de octubre):

Backend: Implementación del algoritmo recursivo y manejo de teletransportación.
Frontend: Interacción inicial con el usuario y visualización de los movimientos.

Commit 3 (16 de octubre):

Backend: Implementación de acertijos y manejo de condiciones especiales.
Frontend: Mejora de la visualización con animaciones y controles.

Commit 4 (21 de octubre):

Backend: Optimización del algoritmo, pruebas con laberintos complejos.
Frontend: Finalización de la interfaz gráfica y visualización completa del proceso.





**Christopher Alcocer Hace Backend **

Definición y representación del laberinto:
Crear una matriz que represente el laberinto, asignando valores específicos:
0: Camino.
1: Pared.
2: Salida.
3: Teletransportación (lleva a otra celda especial).
4: Teletransportación (destino de la celda 3).
111: Celda de acertijo.
Algoritmo de programación dinámica:

Diseñar una estructura de datos para almacenar las soluciones parciales del laberinto (por ejemplo, una matriz auxiliar para marcar caminos ya explorados).
Implementar el algoritmo recursivo de exploración que utilice programación dinámica para evitar recalcular caminos ya explorados.
Manejo de reglas especiales:

Teletransportación: 
Implementar la lógica para que, al llegar a una celda 3, se transporte al jugador a la celda 4, y viceversa.
Acertijos: Programar una función que, al llegar a la celda 111, genere una pregunta de trivia y verifique si la respuesta es correcta para permitir el paso.
Exploración recursiva del laberinto:

Desarrollar una función recursiva que divida el laberinto en secciones más pequeñas y explore las rutas disponibles hacia la salida.
Integrar reglas dinámicas que puedan cambiar el estado de las celdas (paredes que se vuelven caminos o viceversa, etc ).
Condiciones de éxito y manejo de errores:
Definir cuándo el algoritmo ha encontrado la salida (2) o si se ha explorado todo el laberinto sin éxito.
Manejar casos especiales como caminos cerrados, falta de solución, o acertijos mal respondidos.
Pruebas y optimización:

Implementar varios escenarios de prueba (laberintos simples y complejos, con y sin reglas especiales).
Optimizar el algoritmo para mejorar el rendimiento en laberintos más grandes.

**Entregables** 

Backend

Código fuente del algoritmo de programación dinámica que resuelve el laberinto.
Implementación de las reglas especiales (teletransportación, acertijos).
Documentación detallada con comentarios sobre el código y las secciones importantes.

**Cronograma de Commits**

Commit 1 (9 de octubre):

Backend: Creación de la estructura del laberinto, matriz y reglas básicas.
Frontend: Primera representación gráfica del laberinto.

Commit 2 (14 de octubre):

Backend: Implementación del algoritmo recursivo y manejo de teletransportación.
Frontend: Interacción inicial con el usuario y visualización de los movimientos.

Commit 3 (16 de octubre):

Backend: Implementación de acertijos y manejo de condiciones especiales.
Frontend: Mejora de la visualización con animaciones y controles.

Commit 4 (21 de octubre):

Backend: Optimización del algoritmo, pruebas con laberintos complejos.
Frontend: Finalización de la interfaz gráfica y visualización completa del proceso.

