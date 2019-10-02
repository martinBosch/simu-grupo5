from random import random
import numpy as np
from math import exp


"""
Para el metodo de aceptacion y rechazo se debe usar una fY() conocida que tenga el mismo dominio que la fX() que se quiere generar.
En este caso fX() es una normal de media 15 y desvio 3, como nosotros sabemos aproximar la normal estandar con una exponencial de media 1 podemos usar los valores de esa muestra sabiendo que:
Z = X-mu/desvío
siendo que X sigue una distribucion N() y Z una N(0, 1). Como nosotros queremos X, la despejamos:
X = Z*desvío + mu
"""


# con 0 < t < infinito (por eso el 2 en el numerador)
def normal_estandar(t):
    return 2/(np.sqrt(2 * np.pi)) * np.exp( -1*(t)**2 / 2 )


def exponencial(t, media=1):
    return media * exp(-1*media*t)


def generar_muestra_normal(tam_muestra, media, desvio_estandar):
    c = np.sqrt(2 * np.e / np.pi)

    muestra = []
    for i in range(tam_muestra):
        # genero muestras de la variable exponencial de media 1
        u1 = np.random.exponential(1, 1)[0]
        u2 = random()

        if u2 < normal_estandar(u1)/(c*exponencial(u1, media=1)):
            # u3 para decidir si el valor es negativo o positivo
            u3 = random()
            if u3 <= 0.5:
                z = u1
            else:
                z = -u1
            # para obtener un valor para la normal con media=15 y desvio=3, a la variable de la normal estandar
            # la multiplico por el devio y le sumo la media
            x = desvio_estandar * z + media
            muestra.append(x)

    return muestra
