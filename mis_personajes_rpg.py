# -*- encoding: utf-8 -*-
# Pilas engine - A video game framework.
#
# Copyright 2010 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar
# Imagenes del actor de J. M. Silveira Neto - http://silveiraneto.net/tag/pixelart/

import pilas
from pilas.actores import Actor
from pilas.comportamientos import Comportamiento

VELOCIDAD = 100

NORTE = 0
SUR = 2
ESTE = 1
OESTE = 3

class BasePersonajeRPG(Actor):
    def __init__(self, mapa, x=0, y=0, imagen="rpg/calvo.png", velocidad=3):
        Actor.__init__(self, x=x, y=y)
        self.imagen = pilas.imagenes.cargar_grilla(imagen, 3, 4)
        
        self.mapa = mapa
        
        self.direccion = pilas.actores.personajes_rpg.SUR
        self.hacer(Esperando())
        self.velocidad = velocidad

    def definir_cuadro(self, indice):
        self.imagen.definir_cuadro(indice)
        self.definir_centro((18, 32))#SE MODIFICA ESTA LINEA PARA QUE EL PUNTO DE CONTROL QUEDE A LA MISMA ALTURA QUE EL DE LAS CAJAS

    def actualizar(self):
        pass

class Esperando(Comportamiento):
    "Un actor en posicion normal o esperando a que el usuario pulse alguna tecla."

    def iniciar(self, receptor):
        self.receptor = receptor
        if (self.receptor.direccion == pilas.actores.personajes_rpg.NORTE):
            self.receptor.definir_cuadro(1)
        elif (self.receptor.direccion == pilas.actores.personajes_rpg.ESTE):
            self.receptor.definir_cuadro(4)
        elif (self.receptor.direccion == pilas.actores.personajes_rpg.SUR):
            self.receptor.definir_cuadro(7)
        elif (self.receptor.direccion == pilas.actores.personajes_rpg.OESTE):
            self.receptor.definir_cuadro(10)

    def actualizar(self):
        if pilas.escena_actual().control.izquierda:
            self.receptor.hacer(Caminando())
        elif pilas.escena_actual().control.derecha:
            self.receptor.hacer(Caminando())
        elif pilas.escena_actual().control.arriba:
            self.receptor.hacer(Caminando())
        elif pilas.escena_actual().control.abajo:
            self.receptor.hacer(Caminando())

class Caminando(Esperando):

    def __init__(self):
        self._repeticion_cuadro = 3
        
        self.cuadros = [[1,1,1,1,0,0,0,0,1,1,1,1,2,2,2,2],
                        [4,4,4,4,3,3,3,3,4,4,4,4,5,5,5,5],
                        [7,7,7,7,6,6,6,6,7,7,7,7,8,8,8,8],
                        [10,10,10,10,9,9,9,9,10,10,10,10,11,11,11,11]]
                
        self.paso = 0

    def iniciar(self, receptor):
        self.receptor = receptor

    def actualizar(self):
        self.avanzar_animacion()
        salto = 32#ESTO ES LO QUE AVANZA AL PRESIONAR UNA TECLA, COSA DE QUE NO SEA CONTINUO
        dx = salto
        dy = salto

        if pilas.escena_actual().control.izquierda:
            dx = (dx * (-1))#SE MULTIPLICA EL VALOR POR -1 PARA QUE EL MOVIMIENTO SE PRODUZCA HACIA LA PARTE NEGATIVA DEL EJE
            dy=0#VALE 0 PORQUE SINO LA FUNC DE MOVIMIENTO TOMA EL VALOR DE 32 Y SE MUEVE TAMBIEN EN EL OTRO EJE
            self.receptor.direccion = pilas.actores.personajes_rpg.OESTE
            pilas.escena_actual().control.izquierda=False#ESTA LINEA ES LA QUE NO PERMITE UNA REPETICION AL PRESIONAR LAS TECLAS
        elif pilas.escena_actual().control.derecha:
            dy=0#VALE 0 PORQUE SINO LA FUNC DE MOVIMIENTO TOMA EL VALOR DE 32 Y SE MUEVE TAMBIEN EN EL OTRO EJE
            self.receptor.direccion = pilas.actores.personajes_rpg.ESTE
            pilas.escena_actual().control.derecha=False#ESTA LINEA ES LA QUE NO PERMITE UNA REPETICION AL PRESIONAR LAS TECLAS
        elif pilas.escena_actual().control.arriba:
            dx=0#VALE 0 PORQUE SINO LA FUNC DE MOVIMIENTO TOMA EL VALOR DE 32 Y SE MUEVE TAMBIEN EN EL OTRO EJE
            self.receptor.direccion = pilas.actores.personajes_rpg.NORTE
            pilas.escena_actual().control.arriba=False#ESTA LINEA ES LA QUE NO PERMITE UNA REPETICION AL PRESIONAR LAS TECLAS
        elif pilas.escena_actual().control.abajo:
            dx=0#VALE 0 PORQUE SINO LA FUNC DE MOVIMIENTO TOMA EL VALOR DE 32 Y SE MUEVE TAMBIEN EN EL OTRO EJE
            dy = (dy * (-1))#SE MULTIPLICA EL VALOR POR -1 PARA QUE EL MOVIMIENTO SE PRODUZCA HACIA LA PARTE NEGATIVA DEL EJE       
            self.receptor.direccion = pilas.actores.personajes_rpg.SUR
            pilas.escena_actual().control.abajo=False#ESTA LINEA ES LA QUE NO PERMITE UNA REPETICION AL PRESIONAR LAS TECLAS
        else:
            dx=0#VALE 0 PARA QUE EL ACTOR NO SE MUEVA
            dy=0#VALE 0 PARA QUE EL ACTOR NO SE MUEVA
            self.receptor.hacer(Esperando())

        if not(self.receptor.mapa.es_punto_solido(self.receptor.x + dx, self.receptor.y + dy)):
            self.receptor.x += dx
            self.receptor.y += dy

    def avanzar_animacion(self):
        self.paso += 1

        if self.paso >= len(self.cuadros[self.receptor.direccion]):
            self.paso = 0

        self.receptor.definir_cuadro(self.cuadros[self.receptor.direccion][self.paso])

class Maton(BasePersonajeRPG):

    def __init__(self, mapa, x=0, y=0):
        BasePersonajeRPG.__init__(self, mapa, x=x, y=y, imagen="rpg/maton.png", velocidad=2)
