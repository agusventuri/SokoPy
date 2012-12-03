# -*- encoding: utf-8 -*-

import pilas
import Menu

class Puntos(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        fondo = pilas.fondos.Nubes()
        pilas.actores.Texto('Ingresa tu nombre\n"Aceptar para guardar y volver al menu principal"',y=200)
        entrada = pilas.interfaz.IngresoDeTexto()
        b = pilas.actores.Boton()
        b.texto = ""
        b.y = -100

        def cuando_pulsan_el_boton():
            b.pintar_presionado()
            texto = str(entrada.texto)
            archPuntos = open('puntos.txt','r')
            puntaje = archPuntos.read()
            if len(puntaje)==2:
                puntajeOK = '000'+str(puntaje)
            elif len(puntaje)==3:
                puntajeOK = '00'+str(puntaje)
            elif len(puntaje)==4:
                puntajeOK = '0'+str(puntaje)
            elif len(puntaje)==5:
                puntajeOK = str(puntaje)
            guardar = open('Puntos/'+puntajeOK+'_'+texto,'w')
            pilas.cambiar_escena(Menu.Menu())

        def cuando_deja_de_pulsar():
                b.pintar_normal()

        b.conectar_presionado(cuando_pulsan_el_boton)
        b.conectar_normal(cuando_deja_de_pulsar)
        self.pulsa_tecla_escape.conectar(self.cuando_se_presione_escape)

    def cuando_se_presione_escape(self, *k, **kv):
        "Regresa al menu principal"
        import Menu
        pilas.cambiar_escena(Menu.Menu())
