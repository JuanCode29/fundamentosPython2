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
    elif usuario == 'Papel' and computador == 'Piedra' or usuario == 'Piedra' and computador == 'Tijera' or usuario == 'Tijera' and computador == 'Papel':
        return 'Usuario'
    else:
        return 'Computador'

#MOSTRANDO RESULTADOS EN PANTALLA
def main():
    puntos_usuario = 0
    puntos_computador = 0
    while True:
        #obtenemos las opcion del usuario y computador
        usuario = obtener_opcion_usuario()
        computador = obtener_opcion_computador()

        print(f'Tú lejiste {usuario}. La computadora eligió {computador}.')

        resultado = obtener_ganador(usuario, computador)
        if resultado == 'Usuario':
            puntos_usuario += 1
            print('¡Ganaste esta ronda!')
        elif resultado == 'computador':
            puntos_computador +=1
            print('La Computadora ganó esta ronda')
        else:
            print('Esta ronda es un empate.')

        if puntos_usuario >= 3:
            print("¡Felicidades! Ganaste el juego")
            break
        if puntos_computador >= 3:
            print("La computadora a ganado el juego")
            break
main()

