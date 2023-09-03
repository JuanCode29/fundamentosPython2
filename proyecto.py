import random
# LISTA DE OPCIONES DE JUEGO
opciones = ['Piedra', 'Papel', 'Tijera']

#OBTENEMOS JUGADA DEL USUARIO CON SU VALIDACIÓN RESPECTIVA
def obtener_opcion_usuario():
    while True:
        opcion = input("Elije Piedra, Papel o Tijera: ").strip().capitalize()
        if opcion in opciones:
            return opcion
        else:
            print("Opción no válida: Elije Piedra, Papel o Tijera.")

#OBTENEMOS JUGADA DEL COMPUTADOR
def obtener_opcion_computador():
    return random.choice(opciones)

#OBTENEMOS GANADOR

def obtener_ganador(usuario, computador):
    if usuario == computador:
        return 'Empate'
    elif usuario == 'Papel' and computador == 'Piedra' | usuario == 'Piedra' and computador == 'Tijera' | usuario == 'Tijera' and computador == 'Papel':
        return 'Usuario'
    else:
        return 'Computador'



