# -*- encoding: utf-8 -*-

import pilas
import Menu
import Puntos
import Nivel1
import Nivel2
import Nivel3
import Nivel4
import Nivel5

class Ganaste(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def siguiente(self):
        arch = open('save.txt','r')
        archr = arch.read()
        if archr=='Nivel1':
            pilas.cambiar_escena(Nivel2.Nivel2())

        if archr=='Nivel2':
            pilas.cambiar_escena(Nivel3.Nivel3())

        if archr=='Nivel3':
            pilas.cambiar_escena(Nivel4.Nivel4())

        if archr=='Nivel4':
            pilas.cambiar_escena(Nivel5.Nivel5())

    def de_nuevo(self):
        arch = open('save.txt','r')
        archr = arch.read()
        if archr=='Nivel1':
            pilas.cambiar_escena(Nivel1.Nivel1())

        if archr=='Nivel2':
            pilas.cambiar_escena(Nivel2.Nivel2())

        if archr=='Nivel3':
            pilas.cambiar_escena(Nivel3.Nivel3())

        if archr=='Nivel4':
            pilas.cambiar_escena(Nivel4.Nivel4())

        if archr=='Nivel5':
            pilas.cambiar_escena(Nivel5.Nivel5())


    def guardar_puntos(self):
        pilas.cambiar_escena(Puntos.Puntos())

    def salir(self):
        pilas.cambiar_escena(Menu.Menu())

    def iniciar(self):
        fondo = pilas.fondos.Nubes()
        texto = pilas.actores.Texto(u"Ganasteeeeeeeeeee",y=200)
        opciones = [
            ('Siguiente', self.siguiente),
            ('Jugar de nuevo', self.de_nuevo),
            ('Salir (al menu) y guardar puntaje',self.guardar_puntos),
            ('Salir (al menu)', self.salir)]
        menu = pilas.actores.Menu(opciones, y=50)

