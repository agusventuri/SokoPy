# -*- encoding: utf-8 -*-

import pilas
import mis_personajes_rpg
import mi_caja
import mi_actor
import Pausa
import Perdiste
from Pasos import Pasos

class Nivel2(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):

        self.pasos = Pasos()

#PARA SALIR Y COMPROBAR:

        pilas.avisar("Pulsa 'Esc' para menu y 'Q' para comprobar")
        self.pulsa_tecla_escape.conectar(self.cuando_se_presione_escape)
        pilas.eventos.pulsa_tecla.conectar(self.cuando_pulsa_tecla)
        pilas.eventos.pulsa_tecla.conectar(self.cuando_pulsa_tecla_p)

#MAPA:

        grilla = pilas.imagenes.cargar_grilla("grillas/plataformas_10_10.png", 10, 10)
        mapa = pilas.actores.Mapa(filas=20, columnas=20)
        pilas.fondos.Pasto()
        mapa.pintar_bloque(6,3,40)
        mapa.pintar_bloque(7,3,40)
        mapa.pintar_bloque(8,3,40)
        mapa.pintar_bloque(9,3,40)
        mapa.pintar_bloque(10,3,40)
        mapa.pintar_bloque(11,3,40)
        mapa.pintar_bloque(12,3,40)
        mapa.pintar_bloque(12,4,40)
        mapa.pintar_bloque(12,5,40)
        mapa.pintar_bloque(13,5,40)
        mapa.pintar_bloque(14,5,40)
        mapa.pintar_bloque(15,5,40)
        mapa.pintar_bloque(15,6,40)
        mapa.pintar_bloque(15,7,40)
        mapa.pintar_bloque(15,8,40)
        mapa.pintar_bloque(15,9,40)
        mapa.pintar_bloque(15,10,40)
        mapa.pintar_bloque(15,11,40)
        mapa.pintar_bloque(15,12,40)
        mapa.pintar_bloque(15,13,40)
        mapa.pintar_bloque(15,14,40)
        mapa.pintar_bloque(15,15,40)
        mapa.pintar_bloque(15,16,40)
        mapa.pintar_bloque(14,16,40)
        mapa.pintar_bloque(13,16,40)
        mapa.pintar_bloque(12,16,40)
        mapa.pintar_bloque(11,16,40)
        mapa.pintar_bloque(10,16,40)
        mapa.pintar_bloque(9,16,40)
        mapa.pintar_bloque(8,16,40)
        mapa.pintar_bloque(7,16,40)
        mapa.pintar_bloque(7,15,40)
        mapa.pintar_bloque(7,14,40)
        mapa.pintar_bloque(11,15,40)
        mapa.pintar_bloque(10,13,40)
        mapa.pintar_bloque(9,13,40)
        mapa.pintar_bloque(10,12,40)
        mapa.pintar_bloque(9,12,40)
        mapa.pintar_bloque(9,11,40)
        mapa.pintar_bloque(9,10,40)
        mapa.pintar_bloque(11,10,40)
        mapa.pintar_bloque(12,10,40)
        mapa.pintar_bloque(12,11,40)
        mapa.pintar_bloque(14,10,40)
        mapa.pintar_bloque(7,8,40)
        mapa.pintar_bloque(8,8,40)
        mapa.pintar_bloque(9,8,40)
        mapa.pintar_bloque(11,8,40)
        mapa.pintar_bloque(12,8,40)
        mapa.pintar_bloque(12,7,40)
        mapa.pintar_bloque(12,6,40)
        mapa.pintar_bloque(6,4,40)
        mapa.pintar_bloque(6,5,40)
        mapa.pintar_bloque(6,6,40)
        mapa.pintar_bloque(6,7,40)
        mapa.pintar_bloque(6,8,40)
        mapa.pintar_bloque(6,9,40)
        mapa.pintar_bloque(6,10,40)
        mapa.pintar_bloque(6,11,40)
        mapa.pintar_bloque(6,12,40)
        mapa.pintar_bloque(6,13,40)
        mapa.pintar_bloque(6,14,40)

#TEMPORIZADOR:

        t = pilas.actores.Temporizador(x=150, y=150)
        def perdiste():
            pilas.cambiar_escena(Perdiste.Perdiste())
        a = t.ajustar(600, perdiste)
        t.iniciar()

#JUGADOR:

        jugador = mis_personajes_rpg.Maton(mapa)
        jugador.x = 16
        jugador.y = -16
        jugador.z = -1

#ACTOR INVISIBLE:

        invisible = mi_actor.Actor(imagen='invisible.png')

#INVISIBLE VA DELANTE:

        invisible.imitar(jugador)

#CAJAS:

        self.caja1 = mi_caja.Caja(x = -80, y = -112)
        self.caja1.escala = 0.65
        self.caja1.radio_de_colision = 14.5

        self.caja2 = mi_caja.Caja(x = 16, y = -112)
        self.caja2.escala = 0.65
        self.caja2.radio_de_colision = 14.5

        self.caja3 = mi_caja.Caja(x = 80, y = -112)
        self.caja3.escala = 0.65
        self.caja3.radio_de_colision = 14.5

        self.caja4 = mi_caja.Caja(x = 144, y = -112)
        self.caja4.escala = 0.65
        self.caja4.radio_de_colision = 14.5

        self.caja5 = mi_caja.Caja(x = 80, y = -80)
        self.caja5.escala = 0.65
        self.caja5.radio_de_colision = 14.5

        self.caja6 = mi_caja.Caja(x = 144, y = -80)
        self.caja6.escala = 0.65
        self.caja6.radio_de_colision = 14.5

        self.caja7 = mi_caja.Caja(x = 112, y = -48)
        self.caja7.escala = 0.65
        self.caja7.radio_de_colision = 14.5

        self.caja8 = mi_caja.Caja(x = 112, y = 48)
        self.caja8.escala = 0.65
        self.caja8.radio_de_colision = 14.5

        self.caja9 = mi_caja.Caja(x = 16, y = 48)
        self.caja9.escala = 0.65
        self.caja9.radio_de_colision = 14.5

        self.caja10 = mi_caja.Caja(x = -16, y = 16)
        self.caja10.escala = 0.65
        self.caja10.radio_de_colision = 14.5
        self.caja10.z = 0

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

#CAJA7

        def caja7_mueve(invisible,caja7):
            if pilas.escena_actual().control.izquierda==True:
                self.caja7.x -= 32

            if pilas.escena_actual().control.derecha==True:
                self.caja7.x += 32

            if pilas.escena_actual().control.abajo==True:
                self.caja7.y -= 32

            if pilas.escena_actual().control.arriba==True:
                self.caja7.y += 32

#CAJA8

        def caja8_mueve(invisible,caja8):
            if pilas.escena_actual().control.izquierda==True:
                self.caja8.x -= 32

            if pilas.escena_actual().control.derecha==True:
                self.caja8.x += 32

            if pilas.escena_actual().control.abajo==True:
                self.caja8.y -= 32

            if pilas.escena_actual().control.arriba==True:
                self.caja8.y += 32

#CAJA9

        def caja9_mueve(invisible,caja9):
            if pilas.escena_actual().control.izquierda==True:
                self.caja9.x -= 32

            if pilas.escena_actual().control.derecha==True:
                self.caja9.x += 32

            if pilas.escena_actual().control.abajo==True:
                self.caja9.y -= 32

            if pilas.escena_actual().control.arriba==True:
                self.caja9.y += 32

#CAJA10

        def caja10_mueve(invisible,caja10):
            if pilas.escena_actual().control.izquierda==True:
                self.caja10.x -= 32

            if pilas.escena_actual().control.derecha==True:
                self.caja10.x += 32

            if pilas.escena_actual().control.abajo==True:
                self.caja10.y -= 32

            if pilas.escena_actual().control.arriba==True:
                self.caja10.y += 32

        pilas.escena_actual().colisiones.agregar(invisible, self.caja1, caja1_mueve)
        pilas.escena_actual().colisiones.agregar(invisible, self.caja2, caja2_mueve)
        pilas.escena_actual().colisiones.agregar(invisible, self.caja3, caja3_mueve)
        pilas.escena_actual().colisiones.agregar(invisible, self.caja4, caja4_mueve)
        pilas.escena_actual().colisiones.agregar(invisible, self.caja5, caja5_mueve)
        pilas.escena_actual().colisiones.agregar(invisible, self.caja6, caja6_mueve)
        pilas.escena_actual().colisiones.agregar(invisible, self.caja7, caja7_mueve)
        pilas.escena_actual().colisiones.agregar(invisible, self.caja8, caja8_mueve)
        pilas.escena_actual().colisiones.agregar(invisible, self.caja9, caja9_mueve)
        pilas.escena_actual().colisiones.agregar(invisible, self.caja10, caja10_mueve)

#UBICACIONES CORRECTAS:

        ubi1 = mapa.pintar_bloque(7, 4, 19, es_bloque_solido=False)
        ubi2 = mapa.pintar_bloque(8, 4, 19, es_bloque_solido=False)
        ubi3 = mapa.pintar_bloque(9, 4, 19, es_bloque_solido=False)
        ubi4 = mapa.pintar_bloque(10, 4, 19, es_bloque_solido=False)
        ubi5 = mapa.pintar_bloque(11, 4, 19, es_bloque_solido=False)
        ubi6 = mapa.pintar_bloque(7, 5, 19, es_bloque_solido=False)
        ubi7 = mapa.pintar_bloque(8, 5, 19, es_bloque_solido=False)
        ubi8 = mapa.pintar_bloque(9, 5, 19, es_bloque_solido=False)
        ubi9 = mapa.pintar_bloque(10, 5, 19, es_bloque_solido=False)
        ubi10 = mapa.pintar_bloque(11, 5, 19, es_bloque_solido=False)

#COMPROBAR:

    def cuando_pulsa_tecla(self, evento):
        if evento.texto == u'q':
            if self.caja1.colisiona_con_un_punto(-176,80) or self.caja1.colisiona_con_un_punto(-176,48) or self.caja1.colisiona_con_un_punto(-176,16) or self.caja1.colisiona_con_un_punto(-176,-16) or self.caja1.colisiona_con_un_punto(-176,-48) or self.caja1.colisiona_con_un_punto(-144,80) or self.caja1.colisiona_con_un_punto(-144,48) or self.caja1.colisiona_con_un_punto(-144,16) or self.caja1.colisiona_con_un_punto(-144,-16) or self.caja1.colisiona_con_un_punto(-144,-48):
                if self.caja2.colisiona_con_un_punto(-176,80) or self.caja2.colisiona_con_un_punto(-176,48) or self.caja2.colisiona_con_un_punto(-176,16) or self.caja2.colisiona_con_un_punto(-176,-16) or self.caja2.colisiona_con_un_punto(-176,-48) or self.caja2.colisiona_con_un_punto(-144,80) or self.caja2.colisiona_con_un_punto(-144,48) or self.caja2.colisiona_con_un_punto(-144,16) or self.caja2.colisiona_con_un_punto(-144,-16) or self.caja2.colisiona_con_un_punto(-144,-48):
                    if self.caja3.colisiona_con_un_punto(-176,80) or self.caja3.colisiona_con_un_punto(-176,48) or self.caja3.colisiona_con_un_punto(-176,16) or self.caja3.colisiona_con_un_punto(-176,-16) or self.caja3.colisiona_con_un_punto(-176,-48) or self.caja3.colisiona_con_un_punto(-144,80) or self.caja3.colisiona_con_un_punto(-144,48) or self.caja3.colisiona_con_un_punto(-144,16) or self.caja3.colisiona_con_un_punto(-144,-16) or self.caja3.colisiona_con_un_punto(-144,-48):
                        if self.caja4.colisiona_con_un_punto(-176,80) or self.caja4.colisiona_con_un_punto(-176,48) or self.caja4.colisiona_con_un_punto(-176,16) or self.caja4.colisiona_con_un_punto(-176,-16) or self.caja4.colisiona_con_un_punto(-176,-48) or self.caja4.colisiona_con_un_punto(-144,80) or self.caja4.colisiona_con_un_punto(-144,48) or self.caja4.colisiona_con_un_punto(-144,16) or self.caja4.colisiona_con_un_punto(-144,-16) or self.caja4.colisiona_con_un_punto(-144,-48):
                            if self.caja5.colisiona_con_un_punto(-176,80) or self.caja5.colisiona_con_un_punto(-176,48) or self.caja5.colisiona_con_un_punto(-176,16) or self.caja5.colisiona_con_un_punto(-176,-16) or self.caja5.colisiona_con_un_punto(-176,-48) or self.caja5.colisiona_con_un_punto(-144,80) or self.caja5.colisiona_con_un_punto(-144,48) or self.caja5.colisiona_con_un_punto(-144,16) or self.caja5.colisiona_con_un_punto(-144,-16) or self.caja5.colisiona_con_un_punto(-144,-48):
                                if self.caja6.colisiona_con_un_punto(-176,80) or self.caja6.colisiona_con_un_punto(-176,48) or self.caja6.colisiona_con_un_punto(-176,16) or self.caja6.colisiona_con_un_punto(-176,-16) or self.caja6.colisiona_con_un_punto(-176,-48) or self.caja6.colisiona_con_un_punto(-144,80) or self.caja6.colisiona_con_un_punto(-144,48) or self.caja6.colisiona_con_un_punto(-144,16) or self.caja6.colisiona_con_un_punto(-144,-16) or self.caja6.colisiona_con_un_punto(-144,-48):
                                    if self.caja7.colisiona_con_un_punto(-176,80) or self.caja7.colisiona_con_un_punto(-176,48) or self.caja7.colisiona_con_un_punto(-176,16) or self.caja7.colisiona_con_un_punto(-176,-16) or self.caja7.colisiona_con_un_punto(-176,-48) or self.caja7.colisiona_con_un_punto(-144,80) or self.caja7.colisiona_con_un_punto(-144,48) or self.caja7.colisiona_con_un_punto(-144,16) or self.caja7.colisiona_con_un_punto(-144,-16) or self.caja7.colisiona_con_un_punto(-144,-48):
                                        if self.caja8.colisiona_con_un_punto(-176,80) or self.caja8.colisiona_con_un_punto(-176,48) or self.caja8.colisiona_con_un_punto(-176,16) or self.caja8.colisiona_con_un_punto(-176,-16) or self.caja8.colisiona_con_un_punto(-176,-48) or self.caja8.colisiona_con_un_punto(-144,80) or self.caja8.colisiona_con_un_punto(-144,48) or self.caja8.colisiona_con_un_punto(-144,16) or self.caja8.colisiona_con_un_punto(-144,-16) or self.caja8.colisiona_con_un_punto(-144,-48):
                                            if self.caja9.colisiona_con_un_punto(-176,80) or self.caja9.colisiona_con_un_punto(-176,48) or self.caja9.colisiona_con_un_punto(-176,16) or self.caja9.colisiona_con_un_punto(-176,-16) or self.caja9.colisiona_con_un_punto(-176,-48) or self.caja9.colisiona_con_un_punto(-144,80) or self.caja9.colisiona_con_un_punto(-144,48) or self.caja9.colisiona_con_un_punto(-144,16) or self.caja9.colisiona_con_un_punto(-144,-16) or self.caja9.colisiona_con_un_punto(-144,-48):
                                                if self.caja10.colisiona_con_un_punto(-176,80) or self.caja10.colisiona_con_un_punto(-176,48) or self.caja10.colisiona_con_un_punto(-176,16) or self.caja10.colisiona_con_un_punto(-176,-16) or self.caja10.colisiona_con_un_punto(-176,-48) or self.caja10.colisiona_con_un_punto(-144,80) or self.caja10.colisiona_con_un_punto(-144,48) or self.caja10.colisiona_con_un_punto(-144,16) or self.caja10.colisiona_con_un_punto(-144,-16) or self.caja10.colisiona_con_un_punto(-144,-48):
                                                    arch = open('save.txt','w')
                                                    arch.write('Nivel2')
                                                    arch.close()#PARA PASAR AL SIGUIENTE NIVEL (HAY QUE SABER DE CUAL VENGO)
                                                    pun = open('puntos.txt','r')
                                                    lectPun = pun.read()
                                                    pasosHechos=int(self.pasos.obtener_texto())+int(lectPun)
                                                    print pasosHechos
                                                    pun = open('puntos.txt','w')
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

    def cuando_se_presione_escape(self, *k, **kv):
        "Regresa al menu principal"
        import Juego
        pilas.cambiar_escena(Juego.Juego())
