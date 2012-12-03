# -*- encoding: utf-8 -*-

import pilas
import Menu
import Puntos

class Pausa(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def ir_a_escena_anterior(self):
        pilas.recuperar_escena()

    def terminar(self):
        pilas.cambiar_escena(Puntos.Puntos())

    def salir(self):
        pilas.cambiar_escena(Menu.Menu())

    def iniciar(self):
        fondo = pilas.fondos.Nubes()
        texto = pilas.actores.Texto("Juego Pausado", y=150)
        texto.escala = 2
        opciones = [
            ('Reanudar', self.ir_a_escena_anterior),
            (u'Terminar (no se contarán los puntos de este nivel)', self.terminar),
            ('Salir (al menu)', self.salir)]
        menu = pilas.actores.Menu(opciones, y=50)
