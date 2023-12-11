# Ejercicios_Tema5

# Ejercicio 1: Reloj Mágico de Hogwarts
Contexto
Has sido seleccionado como el nuevo aprendiz de hechicería para el desarrollo de artefactos mágicos en Hogwarts. Tu primera tarea es desarrollar un reloj mágico que muestre la hora actual de Hogwarts.

Requerimientos
Crea un script de Python llamado HogwartsClock.py.
Utiliza el módulo datetime para obtener la hora actual.
El reloj debe mostrar horas, minutos y segundos.
Ayuda
Utiliza la función sleep(segundos) del módulo time para actualizar la hora cada segundo.
Puedes utilizar la función system('cls') o system('clear') del módulo os para limpiar la pantalla de la terminal en sistemas Windows y Linux/Unix respectivamente.

# Ejercicio 2: Contador de Votos en la Elección del Nuevo Rey de Narnia
Contexto
Eres el mago responsable de la tecnología en el reino de Narnia. Se están llevando a cabo elecciones para elegir al nuevo Rey, y has sido asignado para desarrollar un contador de votos seguro y eficiente.

Requerimientos
Crea un script de Python llamado NarniaVoteCounter.py.
El script trabajará sobre un fichero llamado NarniaVotes.txt.
Si el fichero no existe o está vacío, crea uno nuevo y establece el contador en 0.
A partir de un argumento en la línea de comando:Si se recibe el argumento add, incrementa el contador en uno y muestra el número actual de votos.
Si se recibe el argumento remove, decrementa el contador en uno y muestra el número actual de votos.
Si no se recibe ningún argumento o se recibe un argumento no válido, muestra el número actual de votos.
Finalmente, guarda el valor actual del contador en el fichero.
Ayuda
Utiliza manejo de excepciones para tratar errores como ficheros corruptos. Puedes mostrar el mensaje: "Error: Fichero corrupto".
