#Juego del ahorcado en Python

import random

# Dibujo del ahorcado
AHORCADO = [
    '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    '''
]

# Lista de palabras
palabras = 'valor aprenderpython comida jugar python web programacion videojuegos computador perros mascota pies arbol libros dinero lapiz telefono amor discos software libre propio cancion collar sol luna juguete españa escuela universidad'.split()

def buscarPalabraAleat(listaPalabras):
    # Devuelve una palabra elegida aleatoriamente
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]

def main():
    print("¡Bienvenido al juego del ahorcado!")
    palabra = buscarPalabraAleat(palabras)
    intentos = 8
    letras_adivinadas = []

    while intentos > 0:
        # Mostrar la palabra con las letras adivinadas
        palabra_mostrada = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                palabra_mostrada += letra
            else:
                palabra_mostrada += "_ "
        print(f"Palabra: {palabra_mostrada}")

        # Pedir al jugador que ingrese una letra
        letra_ingresada = input("Ingresa una letra: ").lower()

        if letra_ingresada in palabra:
            print("¡Correcto! La letra está en la palabra.")
            letras_adivinadas.append(letra_ingresada)
        else:
            print("Incorrecto. Pierdes un intento.")
            intentos -= 1
            print(AHORCADO[8 - intentos])

        if palabra_mostrada.replace(" ", "") == palabra:
            print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
            break

    if intentos == 0:
        print(f"¡Oh no! Te has quedado sin intentos. La palabra era: {palabra}")

if __name__ == "__main__":
    main()
