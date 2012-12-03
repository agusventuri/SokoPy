# -*- encoding: utf-8 -*-

import pilas
import ConfigParser
import os

class Ranking(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        pilas.fondos.Selva()
        pilas.actores.Texto('Ranking de posiciones',y=200)
        lista = os.listdir('Puntos')
        lista.sort()
#PRIMER POSICIÓN:
        pilas.actores.Texto(lista[0],y=100)
#SEGUNDA POSICIÓN:
        pilas.actores.Texto(lista[1],y=60)
#CUARTA POSICIÓN:
        pilas.actores.Texto(lista[2],y=20)
#QUINTA POSICIÓN:
        pilas.actores.Texto(lista[3],y=-20)
#SEXTA POSICIÓN:
        pilas.actores.Texto(lista[4],y=-60)
        print lista
        pilas.avisar("Pulsa 'Esc' para menu")
        self.pulsa_tecla_escape.conectar(self.cuando_se_presione_escape)

    def cuando_se_presione_escape(self, *k, **kv):
        "Regresa al menu principal"
        import Menu
        pilas.cambiar_escena(Menu.Menu())
