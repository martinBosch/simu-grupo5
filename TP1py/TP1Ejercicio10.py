from matplotlib import pyplot as plt
from scipy.stats import kstest
from scipy.stats import norm

from random import random
import math
import numpy as np
from math import exp


def normal_estandar(t):
    return 2/(np.sqrt(2 * np.pi)) * np.exp( -1*(t)**2 / 2 )


def exponencial(t, media=1):
    return media * exp(-1*media*t)


media, desvio_estandar = 15, 3
tam_muestra = 100000

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


print('Aplicamos el test chi2 tomando como H0 que los valores observados en la muestra del ejer 3 siguen'
      ' una distribucion normal de media 15 y desvio estandar 3'
      ' Si p < nivel_significancia rechazamos H0 con un error del 1% o %5')

stat, p = kstest(muestra, 'norm', args=(media, desvio_estandar), N=tam_muestra)

print('statistic:', stat, 'p:', p)

if p < 0.05:
    print("Rechazamos H0 con un error del 5%: los valores de la muestra NO siguen la distribucion normal pedida")
    print("Ahora probamos si con menos error podemos llegar a aceptar H0")
    if p < 0.01:
        print("Rechazamos H0 con un error del 1%: los valores de la muestra NO siguen la distribucion normal pedida")
    else:
        print("Aceptamos H0 con un error del 1%: los valores de la muestra siguen la distribucion normal pedida")
else:
    print("Aceptamos H0 con un error del 5%: los valores de la muestra siguen la distribucion normal pedida")
