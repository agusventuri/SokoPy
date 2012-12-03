# -*- encoding: utf-8 -*-

import pilas

class Nivel5(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        pilas.fondos.Pasto()
        texto = pilas.actores.Texto(u"Todavía en desarrollo")
        pilas.avisar("Pulsa 'Esc' para volver al menu")
        self.pulsa_tecla_escape.conectar(self.cuando_se_presione_escape)

    def cuando_se_presione_escape(self, *k, **kv):
        "Regresa al menu principal"
        import Juego
        pilas.cambiar_escena(Juego.Juego())
