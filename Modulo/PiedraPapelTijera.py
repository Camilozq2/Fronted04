import random

opciones = {
    'piedra': 0,
    'papel':1,
    'tijera':2,
}

def seleccionJugador():
    print("""Seleccione una opcion:
    Piedra
    Papel
    Tijera
    """)
    seleccion = input("Escriba la opcion: ")
    return seleccion.lower()

def seleccionMaquina():
    opcionesMaquina = list(opciones.keys())
    seleccion = random.choice(opcionesMaquina)
    return seleccion

def ganadorRonda(valorJugador, valorMaquina):
    posiblesGanadores = (
        (0, -1, 1),
        (1, 0, -1),
        (-1, 1, 0)
    )
    ganadorDeLaRonda = posiblesGanadores[
        opciones[valorJugador]
        ][
        opciones[valorMaquina]
        ]
    return ganadorDeLaRonda

def anunciarGanador(resultado):
    if resultado < 0:
        print('Gano la maquina')
    elif resultado > 0:
        print('Gano el jugador')
    else:
        print('Empate!!!!!!')

def anunciarGanadorPorRonda(valorJugador, valorMaquina, ronda):
    print('\n'*30)
    print('Ronda no:',ronda)
    print(f'El jugador selecciono: {valorJugador}')
    print('La maquina selecciono:', valorMaquina)
    anunciarGanador(
        ganadorRonda(valorJugador, valorMaquina)
    )
    input()

def anunciarGanadorPartida(registroRondas):
    print('\n'*30)
    print('Ganador de la partida')
    anunciarGanador(sum(registroRondas))

if __name__ == '__main__':
    valor1 = seleccionJugador()
    valor2 = seleccionMaquina()
    resultado = ganadorRonda(valor1, valor2)
    print(valor1, valor2)
    anunciarGanador(resultado)