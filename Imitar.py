# -*- encoding: utf-8 -*-

import random
import pilas
import math

class Habilidad(object):

    def __init__(self, receptor):
        self.receptor = receptor

    def actualizar(self):
        pass

    def eliminar(self):
        pass

class Imitar(Habilidad):

    def __init__(self, receptor, objeto_a_imitar, con_rotacion=True):
        Habilidad.__init__(self, receptor)
        self.objeto_a_imitar = objeto_a_imitar

        # Establecemos el mismo id para el actor y el objeto fisico
        # al que imita. Así luego en las colisiones fisicas sabremos a que
        # actor corresponde esa colisión.
        receptor.id = objeto_a_imitar.id

        # Y nos guardamos una referencia al objeto físico al que imita.
        # Posterormente en las colisiones fisicas comprobaremos si el
        # objeto tiene el atributo "figura" para saber si estamos delante
        # de una figura fisica o no.
        receptor.figura = objeto_a_imitar

        self.con_rotacion = con_rotacion

    def actualizar(self):
        if pilas.escena_actual().control.izquierda:
            x = self.objeto_a_imitar.x-32
            y = self.objeto_a_imitar.y
            self.receptor.x = x
            self.receptor.y = y

        if pilas.escena_actual().control.derecha:
            x = self.objeto_a_imitar.x+32
            y = self.objeto_a_imitar.y
            self.receptor.x = x
            self.receptor.y = y

        if pilas.escena_actual().control.abajo:
            x = self.objeto_a_imitar.x
            y = self.objeto_a_imitar.y-32
            self.receptor.x = x
            self.receptor.y = y

        if pilas.escena_actual().control.arriba:
            x = self.objeto_a_imitar.x
            y = self.objeto_a_imitar.y+32
            self.receptor.x = x
            self.receptor.y = y

        if (self.con_rotacion):
            self.receptor.rotacion = self.objeto_a_imitar.rotacion

    def eliminar(self):
        if isinstance(self.objeto_a_imitar, pilas.fisica.Figura):
            self.objeto_a_imitar.eliminar()
