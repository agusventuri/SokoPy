# -*- encoding: utf-8 -*-

import pilas

class Creditos(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        fondo = pilas.fondos.Pasto()
        texto = pilas.actores.Texto(u"Hola, bienvenido a Sokoban. Este es un juego\ndesarrollado en el colegio secundario ITS Villada\npor los alumnos:\n \bAgustín Venturi\n \bAgustín Bertea\nEsta es la versión 0.1 del juego. Si vas a usar\nalgo del código no hay problema, pero por favor\nmenciona a los autores.\nNuestros mejores agradecimientos a:\n \bMarcelo Venturi, ya que gracias a el terminé\n \bHugo Ruscitti, por Pilas y por su ayuda\n \bPablo y Javi, por su paciencia")
        texto.y = [0,350]
        pilas.avisar("Pulsa 'Esc' para volver al menu")
        self.pulsa_tecla_escape.conectar(self.cuando_se_presione_escape)

    def cuando_se_presione_escape(self, *k, **kv):
        "Regresa al menu principal"
        import Menu
        pilas.cambiar_escena(Menu.Menu())
