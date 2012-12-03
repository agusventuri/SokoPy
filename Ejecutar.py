# -*- encoding: utf-8 -*-

import pilas
import Menu

pilas.iniciar(titulo = "SokoPy")

# ejecuta escena actual.
import Menu
pilas.cambiar_escena(Menu.Menu())

pilas.ejecutar()
