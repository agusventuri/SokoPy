#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pilas

class Pasos(pilas.actores.Texto):
    '''Representa los pasos'''

    def __init__(self, x=-290, y=205):
        pilas.actores.Texto.__init__(self,'0', x=x, y=y)

    def actualizar(self):
        a = int(self.obtener_texto())
        if pilas.escena_actual().control.izquierda:
            a+=1
            self.definir_texto(str(a))
        elif pilas.escena_actual().control.derecha:
            a+=1
            self.definir_texto(str(a))
        elif pilas.escena_actual().control.arriba:
            a+=1
            self.definir_texto(str(a))
        elif pilas.escena_actual().control.abajo:
            a+=1
            self.definir_texto(str(a))
