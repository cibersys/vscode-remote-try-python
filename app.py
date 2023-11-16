#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")


# Crear un juego bajo las siquientes especificaciones:
# Reglas del juego:
#     La piedra gana a las tijeras (las rompe).
#     Las tijeras han ganado al papel (lo cortan).
#     El papel gana a la piedra (la envuelve).
#     El minijuego es multijugador y el equipo juega el papel del oponente y elige un elemento aleatorio de la lista de elementos
# 
# Interacción con el jugador:
#     La consola se usa para interactuar con el jugador.
#     El jugador puede elegir una de las tres opciones: rock, paper o scissors.
#     El jugador puede elegir si vuelve a jugar.
#     Se debe advertir al jugador si introduce una opción no válida.
#     El jugador ve su puntuación al final del juego.
# 
# Validación de la entrada del usuario:
#     En cada ronda, el jugador debe entrar en una de las opciones de la lista y ser informado de si ganó, perdió o empató con el oponente.
#     El minijuego debe controlar las entradas del usuario, colocarlas en minúsculas e informar al usuario si la opción no es válida.
#     Al final de cada ronda, el jugador debe responder si quiere jugar de nuevo o no.

import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")

    # validar la entrada del usuario
    # si es diferente a r, p o s, entonces es una entrada no válida
    if user not in ['r', 'p', 's']:
        return 'Invalid input!'

    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True
    return False

# Agregar a la función debajo una característica para controlar la cantidad de rondas jugadas
# y mostrar el resultado final de las rondas jugadas
rounds = 0
scores = {'player': 0, 'computer': 0}
while True:
    result = play()
    print(result)

    # mantener un registro de la puntuación del jugador y la computadora
    if result == 'You won!':
        scores['player'] += 1
        rounds += 1
    elif result == 'You lost!':
        scores['computer'] += 1
        rounds += 1
 
    play_again = input('Play again? (y/n): ')
    if play_again.lower() != 'y':
        print('\n')
        print('Final scores:')
        print(f"Rounds played: {rounds}")
        print(f"Player score: {scores['player']}")
        print(f"Computer score: {scores['computer']}")
        print('\n')
        break

# Imprimir un mensaje con mi nombre de GitHub y el año actual
print('Bye! Thanks for playing')
print('\n')
print('Author: @cibersys & GitHub Copilot', 2023)
print('\n')