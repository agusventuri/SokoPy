# -*- encoding: utf-8 -*-

import pilas
import Nivel1
import Nivel2
import Nivel3
import Nivel4
import Nivel5

class Juego(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def nivel1(self):
        pilas.cambiar_escena(Nivel1.Nivel1())

    def nivel2(self):
        pilas.cambiar_escena(Nivel2.Nivel2())

    def nivel3(self):
        pilas.cambiar_escena(Nivel3.Nivel3())

    def nivel4(self):
        pilas.cambiar_escena(Nivel4.Nivel4())

    def nivel5(self):
        pilas.cambiar_escena(Nivel5.Nivel5())

    def iniciar(self):
        fondo = pilas.fondos.Pasto()
        opciones = [
('Nivel 1', self.nivel1),
            ('Nivel 2', self.nivel2),
            ('Nivel 3', self.nivel3),
            ('Nivel 4', self.nivel4),
            ('Nivel 5', self.nivel5)]
        menu = pilas.actores.Menu(opciones, y=100)
        pilas.avisar("Pulsa 'Esc' para volver al menu")
        self.pulsa_tecla_escape.conectar(self.cuando_se_presione_escape)

    def cuando_se_presione_escape(self, *k, **kv):
        "Regresa al menu principal"
        import Menu
        pilas.cambiar_escena(Menu.Menu())
