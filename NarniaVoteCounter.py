import os
import sys

def leer_contador():
    try:
        with open("NarniaVotes.txt", "r") as archivo:
            contenido = archivo.read()
            return int(contenido) if contenido else 0
    except FileNotFoundError:
        return 0
    except ValueError:
        print("Error: Fichero corrupto")
        sys.exit()

def guardar_contador(contador):
    with open("NarniaVotes.txt", "w") as archivo:
        archivo.write(str(contador))

def mostrar_votos():
    contador = leer_contador()
    print(f"Número actual de votos: {contador}")

def incrementar_votos():
    contador = leer_contador()
    contador += 1
    guardar_contador(contador)
    print(f"Número actual de votos: {contador}")

def decrementar_votos():
    contador = leer_contador()
    if contador > 0:
        contador -= 1
        guardar_contador(contador)
        print(f"Número actual de votos: {contador}")
    else:
        print("No se pueden decrementar más votos, el contador ya está en 0.")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "add":
            incrementar_votos()
        elif sys.argv[1] == "remove":
            decrementar_votos()
        else:
            mostrar_votos()
    else:
        mostrar_votos()