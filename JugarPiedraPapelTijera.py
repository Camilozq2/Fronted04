from Modulo.PiedraPapelTijera import *

def jugarPiedraPapelTijera(turnos=3):
    ganadorPorRonda = []
    for ronda in range(1,turnos+1):
        valorJugador = seleccionJugador()
        valorMaquina = seleccionMaquina()
        ganadorDeLaRonda = ganadorRonda(valorJugador, valorMaquina)
        ganadorPorRonda.append(ganadorDeLaRonda)
        anunciarGanadorPorRonda(valorJugador, valorMaquina, ronda)
    anunciarGanadorPartida(ganadorPorRonda)

if __name__ == '__main__':
    jugarPiedraPapelTijera()
    