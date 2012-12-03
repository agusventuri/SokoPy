import pilas
import mis_personajes_rpg

class Jugador(mis_personajes_rpg.Maton):

    def __init__(self):
        maton = mis_personajes_rpg.Maton()

    def actualizar(self):
        print 'hola'
        if pilas.escena_actual().control.izquierda==True:
            print 'izquierda'
            if colcaja6==True:
                caja6.x -= 32

        if pilas.escena_actual().control.derecha==True:
            print 'derecha'
            if colcaja6==True:
                caja6.x += 32

        if pilas.escena_actual().control.abajo==True:
            print 'abajo'
            if colcaja6==True:
                caja6.y -= 32

        if pilas.escena_actual().control.arriba==True:
            print 'arriba'
            if colcaja6==True:
                caja6.y += 32

