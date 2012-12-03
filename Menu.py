# -*- encoding: utf-8 -*-

import pilas
import Juego
import Instrucciones
import Creditos
import Ranking

pilas.iniciar(titulo="Sokoban")

class Menu(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar_juego(self):
        pilas.cambiar_escena(Juego.Juego())

    def instrucciones(self):
        pilas.cambiar_escena(Instrucciones.Instrucciones())

    def ranking(self):
        pilas.cambiar_escena(Ranking.Ranking())

    def creditos(self):
        pilas.cambiar_escena(Creditos.Creditos())

    def salir_del_juego(self):
        pilas.terminar()

    def iniciar(self):
        fondo = pilas.fondos.Noche()
        opciones = [
('Comenzar a jugar', self.iniciar_juego),
            ('Instrucciones', self.instrucciones),
            ('Ranking', self.ranking),
            (u'Créditos', self.creditos),
            ('Salir', self.salir_del_juego)]
        menu = pilas.actores.Menu(opciones, y=100)

pilas.cambiar_escena(Menu())
pilas.ejecutar()
