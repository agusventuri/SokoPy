# -*- encoding: utf-8 -*-

import pilas

class Instrucciones(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        fondo = pilas.fondos.Pasto()
        texto = pilas.actores.Texto(u"Hola, bienvenido a Sokoban. Este es un juego\ndel tipo rompecabezas, donde tendrás que\npensar antes de actuar.\nEste juego consiste en llevar las cajas a la \nzona pintada de verde. Hasta ahí es simple, pero\n ten en cuenta el tiempo y\nque solo puedes empujar, no traer.\nY solo puedes empujar de a una caja")
        texto.y = [0,250,200]
        pilas.avisar("Pulsa 'Esc' para volver al menu")
        self.pulsa_tecla_escape.conectar(self.cuando_se_presione_escape)

    def cuando_se_presione_escape(self, *k, **kv):
        "Regresa al menu principal"
        import Menu
        pilas.cambiar_escena(Menu.Menu())
