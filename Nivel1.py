# -*- encoding: utf-8 -*-

import pilas
import mis_personajes_rpg
import mi_caja
import mi_actor
import Pausa
import Perdiste
from Pasos import Pasos

class Nivel1(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):

        self.pasos = Pasos()
        pilas.actores.Texto("Pulsa 'Esc' para menu y 'Q' para comprobar\n'a' para autoresolver(leer antes las instrucciones)",y=-160)

#PARA SALIR, COMPROBAR Y AUTORESOLVER:

        self.pulsa_tecla_escape.conectar(self.cuando_se_presione_escape)
        pilas.eventos.pulsa_tecla.conectar(self.cuando_pulsa_tecla)
        pilas.eventos.pulsa_tecla.conectar(self.autoresolver)
        pilas.eventos.pulsa_tecla.conectar(self.cuando_pulsa_tecla_p)

#MAPA:

        grilla = pilas.imagenes.cargar_grilla("grillas/plataformas_10_10.png", 10, 10)
        mapa = pilas.actores.Mapa(filas=20, columnas=20)
        pilas.fondos.Pasto()
        mapa.pintar_bloque(8, 0, 40)
        mapa.pintar_bloque(9, 0, 40)
        mapa.pintar_bloque(10, 0, 40)
        mapa.pintar_bloque(11, 0, 40)
        mapa.pintar_bloque(11, 1, 40)
        mapa.pintar_bloque(11, 2, 40)
        mapa.pintar_bloque(11, 3, 40)
        mapa.pintar_bloque(11, 4, 40)
        mapa.pintar_bloque(12, 4, 40)
        mapa.pintar_bloque(13, 4, 40)
        mapa.pintar_bloque(13, 5, 40)
        mapa.pintar_bloque(13, 6, 40)
        mapa.pintar_bloque(13, 7, 40)
        mapa.pintar_bloque(13, 8, 40)
        mapa.pintar_bloque(13, 9, 40)
        mapa.pintar_bloque(13, 10, 40)
        mapa.pintar_bloque(11, 6, 40)
        mapa.pintar_bloque(11, 7, 40)
        mapa.pintar_bloque(11, 8, 40)
        mapa.pintar_bloque(11, 10, 40)
        mapa.pintar_bloque(11, 12, 40)
        mapa.pintar_bloque(12, 10, 40)
        mapa.pintar_bloque(12, 11, 40)
        mapa.pintar_bloque(12, 12, 40)
        mapa.pintar_bloque(12, 13, 40)
        mapa.pintar_bloque(12, 14, 40)
        mapa.pintar_bloque(12, 15, 40)
        mapa.pintar_bloque(12, 16, 40)
        mapa.pintar_bloque(12, 17, 40)
        mapa.pintar_bloque(12, 18, 40)
        mapa.pintar_bloque(11, 18, 40)
        mapa.pintar_bloque(10, 18, 40)
        mapa.pintar_bloque(9, 18, 40)
        mapa.pintar_bloque(8, 18, 40)
        mapa.pintar_bloque(8, 17, 40)
        mapa.pintar_bloque(8, 16, 40, es_bloque_solido=True)
        mapa.pintar_bloque(8, 15, 40)
        mapa.pintar_bloque(8, 14, 40)
        mapa.pintar_bloque(8, 13, 40)
        mapa.pintar_bloque(9, 13, 40)
        mapa.pintar_bloque(9, 12, 40)
        mapa.pintar_bloque(9, 11, 40)
        mapa.pintar_bloque(9, 10, 40)
        mapa.pintar_bloque(9, 9, 40)
        mapa.pintar_bloque(8, 9, 40)
        mapa.pintar_bloque(7, 9, 40)
        mapa.pintar_bloque(6, 9, 40)
        mapa.pintar_bloque(6, 8, 40)
        mapa.pintar_bloque(5, 8, 40)
        mapa.pintar_bloque(4, 8, 40)
        mapa.pintar_bloque(3, 8, 40)
        mapa.pintar_bloque(3, 7, 40)
        mapa.pintar_bloque(3, 6, 40)
        mapa.pintar_bloque(3, 5, 40)
        mapa.pintar_bloque(3, 4, 40)
        mapa.pintar_bloque(4, 4, 40)
        mapa.pintar_bloque(5, 4, 40)
        mapa.pintar_bloque(6, 4, 40)
        mapa.pintar_bloque(8, 7, 40)#cuadrado
        mapa.pintar_bloque(9, 7, 40)#cuadrado
        mapa.pintar_bloque(8, 6, 40)#cuadrado
        mapa.pintar_bloque(9, 6, 40)#cuadrado
        mapa.pintar_bloque(8, 4, 40)#rectangulo chico
        mapa.pintar_bloque(9, 4, 40)#rectangulo chico
        mapa.pintar_bloque(6, 3, 40)
        mapa.pintar_bloque(6, 2, 40)
        mapa.pintar_bloque(7, 2, 40)
        mapa.pintar_bloque(8, 2, 40)
        mapa.pintar_bloque(8, 1, 40)

#TEMPORIZADOR:

        t = pilas.actores.Temporizador(x=150, y=150)
        def perdiste():
            pilas.cambiar_escena(Perdiste.Perdiste())
        a = t.ajustar(200, perdiste)
        t.iniciar()

#JUGADOR:

        jugador = mis_personajes_rpg.Maton(mapa)
        jugador.x = 48
        jugador.y = -48
        jugador.z = -1

#ACTOR INVISIBLE:

        invisible = mi_actor.Actor(imagen='invisible.png')

#INVISIBLE VA DELANTE:

        invisible.imitar(jugador)

#CAJAS:

        self.caja1 = mi_caja.Caja(x = -144, y = -16)
        self.caja1.escala = 0.65
        self.caja1.radio_de_colision = 14.5

        self.caja2 = mi_caja.Caja(x = -240, y = -16)
        self.caja2.escala = 0.65
        self.caja2.radio_de_colision = 14.5

        self.caja3 = mi_caja.Caja(x = -144, y = 80)
        self.caja3.escala = 0.65
        self.caja3.radio_de_colision = 14.5

        self.caja4 = mi_caja.Caja(x = -144, y = 144)
        self.caja4.escala = 0.65
        self.caja4.radio_de_colision = 14.5

        self.caja5 = mi_caja.Caja(x = -80, y = 80)
        self.caja5.escala = 0.65
        self.caja5.radio_de_colision = 14.5

        self.caja6 = mi_caja.Caja(x = -80, y = 112)
        self.caja6.z = 0
        self.caja6.escala = 0.65
        self.caja6.radio_de_colision = 14.5

#COLISIONES

#CAJA1

        def caja1_mueve(invisible,caja1):
            if pilas.escena_actual().control.izquierda==True:
                self.caja1.x -= 32

            if pilas.escena_actual().control.derecha==True:
                self.caja1.x += 32

            if pilas.escena_actual().control.abajo==True:
                self.caja1.y -= 32

            if pilas.escena_actual().control.arriba==True:
                self.caja1.y += 32

#CAJA2

        def caja2_mueve(invisible,caja2):
            if pilas.escena_actual().control.izquierda==True:
                self.caja2.x -= 32

            if pilas.escena_actual().control.derecha==True:
                self.caja2.x += 32

            if pilas.escena_actual().control.abajo==True:
                self.caja2.y -= 32

            if pilas.escena_actual().control.arriba==True:
                self.caja2.y += 32

#CAJA3

        def caja3_mueve(invisible,caja3):
            if pilas.escena_actual().control.izquierda==True:
                self.caja3.x -= 32

            if pilas.escena_actual().control.derecha==True:
                self.caja3.x += 32

            if pilas.escena_actual().control.abajo==True:
                self.caja3.y -= 32

            if pilas.escena_actual().control.arriba==True:
                self.caja3.y += 32

#CAJA4

        def caja4_mueve(invisible,caja4):
            if pilas.escena_actual().control.izquierda==True:
                self.caja4.x -= 32

            if pilas.escena_actual().control.derecha==True:
                self.caja4.x += 32

            if pilas.escena_actual().control.abajo==True:
                self.caja4.y -= 32

            if pilas.escena_actual().control.arriba==True:
                self.caja4.y += 32

#CAJA5

        def caja5_mueve(invisible,caja5):
            if pilas.escena_actual().control.izquierda==True:
                self.caja5.x -= 32

            if pilas.escena_actual().control.derecha==True:
                self.caja5.x += 32

            if pilas.escena_actual().control.abajo==True:
                self.caja5.y -= 32

            if pilas.escena_actual().control.arriba==True:
                self.caja5.y += 32

#CAJA6

        def caja6_mueve(invisible,caja6):
            if pilas.escena_actual().control.izquierda==True:
                self.caja6.x -= 32

            if pilas.escena_actual().control.derecha==True:
                self.caja6.x += 32

            if pilas.escena_actual().control.abajo==True:
                self.caja6.y -= 32

            if pilas.escena_actual().control.arriba==True:
                self.caja6.y += 32

        pilas.escena_actual().colisiones.agregar(invisible, self.caja1, caja1_mueve)
        pilas.escena_actual().colisiones.agregar(invisible, self.caja2, caja2_mueve)
        pilas.escena_actual().colisiones.agregar(invisible, self.caja3, caja3_mueve)
        pilas.escena_actual().colisiones.agregar(invisible, self.caja4, caja4_mueve)
        pilas.escena_actual().colisiones.agregar(invisible, self.caja5, caja5_mueve)
        pilas.escena_actual().colisiones.agregar(invisible, self.caja6, caja6_mueve)

#UBICACIONES CORRECTAS:

        ubi1 = mapa.pintar_bloque(9, 17, 19, es_bloque_solido=False)
        ubi2 = mapa.pintar_bloque(10, 17, 19, es_bloque_solido=False)
        ubi3 = mapa.pintar_bloque(11, 17, 19, es_bloque_solido=False)
        ubi4 = mapa.pintar_bloque(9, 16, 19, es_bloque_solido=False)
        ubi5 = mapa.pintar_bloque(10, 16, 19, es_bloque_solido=False)
        ubi6 = mapa.pintar_bloque(11, 16, 19, es_bloque_solido=False)

#COMPROBAR:

    def cuando_pulsa_tecla(self, evento):
        if evento.texto == u'q':
            if self.caja1.colisiona_con_un_punto(208,16) or self.caja1.colisiona_con_un_punto(240,16) or self.caja1.colisiona_con_un_punto(208,-13) or self.caja1.colisiona_con_un_punto(240,-13) or self.caja1.colisiona_con_un_punto(208,-46) or self.caja1.colisiona_con_un_punto(240,-46):
                if self.caja2.colisiona_con_un_punto(208,16) or self.caja2.colisiona_con_un_punto(240,16) or self.caja2.colisiona_con_un_punto(208,-13) or self.caja2.colisiona_con_un_punto(240,-13) or self.caja2.colisiona_con_un_punto(208,-46) or self.caja2.colisiona_con_un_punto(240,-46):
                    if self.caja3.colisiona_con_un_punto(208,16) or self.caja3.colisiona_con_un_punto(240,16) or self.caja3.colisiona_con_un_punto(208,-13) or self.caja3.colisiona_con_un_punto(240,-13) or self.caja3.colisiona_con_un_punto(208,-46) or self.caja3.colisiona_con_un_punto(240,-46):
                        if self.caja4.colisiona_con_un_punto(208,16) or self.caja4.colisiona_con_un_punto(240,16) or self.caja4.colisiona_con_un_punto(208,-13) or self.caja4.colisiona_con_un_punto(240,-13) or self.caja4.colisiona_con_un_punto(208,-46) or self.caja4.colisiona_con_un_punto(240,-46):
                            if self.caja5.colisiona_con_un_punto(208,16) or self.caja5.colisiona_con_un_punto(240,16) or self.caja5.colisiona_con_un_punto(208,-13) or self.caja5.colisiona_con_un_punto(240,-13) or self.caja5.colisiona_con_un_punto(208,-46) or self.caja5.colisiona_con_un_punto(240,-46):
                                if self.caja6.colisiona_con_un_punto(208,16) or self.caja6.colisiona_con_un_punto(240,16) or self.caja6.colisiona_con_un_punto(208,-13) or self.caja6.colisiona_con_un_punto(240,-13) or self.caja6.colisiona_con_un_punto(208,-46) or self.caja6.colisiona_con_un_punto(240,-46):
                                    arch = open('save.txt','w')
                                    arch.write('Nivel1')
                                    arch.close()#PARA PASAR AL SIGUIENTE NIVEL (HAY QUE SABER DE CUAL VENGO)
                                    pun = open('puntos.txt','w')
                                    pasosHechos=int(self.pasos.obtener_texto())
                                    pun.write(str(pasosHechos))
                                    pun.close()
                                    import Ganaste
                                    pilas.cambiar_escena(Ganaste.Ganaste())
                                else:
                                    pilas.avisar(u'No están colocados en la zona marcada')
                            else:
                                pilas.avisar(u'No están colocados en la zona marcada')
                        else:
                            pilas.avisar(u'No están colocados en la zona marcada')
                    else:
                        pilas.avisar(u'No están colocados en la zona marcada')
                else:
                    pilas.avisar(u'No están colocados en la zona marcada')
            else:
                pilas.avisar(u'No están colocados en la zona marcada')

    def cuando_pulsa_tecla_p(self, evento):        
        if evento.texto == u'p':
            pilas.almacenar_escena(Pausa.Pausa())

#AUTORESOLVER:

    def autoresolver(self,evento):
        if evento.texto==u'a':
            print 'vamos'

#SALIR:

    def cuando_se_presione_escape(self, *k, **kv):
        "Regresa al menu principal"
        import Juego
        pilas.cambiar_escena(Juego.Juego())
