import os
from datetime import datetime
from time import sleep

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_reloj():
    while True:
        limpiar_pantalla()
        ahora = datetime.now()
        hora = ahora.strftime("%H:%M:%S")
        print("Reloj Mágico de Hogwarts")
        print("Hora actual de Hogwarts:", hora)
        sleep(1)

if __name__ == "__main__":
    mostrar_reloj()
