#75.26 Simulación - TP1
#Grupo 5
#79979 – González, Juan Manuel (juanmg0511@gmail.com)<br />
#92028 – Tusca, Bautista (bautista.tusca@gmail.com)<br />
#93272 – Zapico, Rodrigo (rodri.zapico@gmail.com)<br />
#96749 – Bosch, Martín (martinbosch17@gmail.com)

#Ejercicio 3
from matplotlib import pyplot as plt
import random
import math
import numpy as np
from math import exp

#Tamaño gráficos
plt.style.use('default')
plt.rcParams['figure.figsize'] = (15, 10)

'''
Para el metodo de aceptacion y rechazo se debe usar una fY() conocida que tenga el mismo dominio que la fX() que se quiere generar.
En este caso fX() es una normal de media 15 y desvio 3, como nosotros sabemos aproximar la normal estandar con una exponencial de media 1 podemos usar los valores de esa muestra sabiendo que:
Z = X-mu/desvío
siendo que X sigue una distribucion N() y Z una N(0, 1). Como nosotros queremos X, la despejamos:
X = Z*desvío + mu
'''

# con 0 < t < infinito (por eso el 2 en el numerador)
def normal_estandar(t):
    return 2/(np.sqrt(2 * np.pi)) * np.exp( -1*(t)**2 / 2 )

x = np.arange(0, 10, 0.1)
y = np.array(list(map(normal_estandar, x)))

plt.plot(x, y)
plt.show()

def exponencial(t, media=1):
    return media * exp(-1*media*t)

x = np.arange(0, 10, 0.1)
y = np.array(list(map(exponencial, x)))

plt.plot(x, y)
plt.show()

# comparo la distribucion normal estandar y la exponencial de media 1
x1 = np.arange(0, 10, 0.1)
y1 = np.array(list(map(normal_estandar, x1)))

y2 = np.array(list(map(exponencial, x1)))

plt.plot(x1, y1, label='fx')
plt.plot(x1, y2, label='fy')
plt.legend()
plt.show()

from random import random

media, desvio_estandar = 15, 3
tam_muestra = 100000

c = np.sqrt(2 * np.e / np.pi)

muestra = []
for i in range(tam_muestra):
    # genero muestras de la variable exponencial de media 1
    u1 = np.random.exponential(1, 1)[0]
    u2 = random()

    if( u2 < normal_estandar(u1)/(c*exponencial(u1, media=1)) ):
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


plt.hist(muestra, 100)
plt.show()

from scipy.stats import norm

x = np.arange(0, 30, 0.1)

plt.plot(x, norm.pdf(x, media, desvio_estandar), color='r')
plt.hist(muestra, 100, density=True)
plt.show()


# media de la muestra
media_muestra = np.mean(muestra)
print('Media de la muestra:', media_muestra)
print('Diferencia hasta la media teorica:', media - media_muestra)

# desvio estandar de la muestra
muestra_desvio_standar = np.std(muestra)
print('Desvio estandar de la muestra:', muestra_desvio_standar)
print('Diferencia hasta el devio estandar teorico:', desvio_estandar - muestra_desvio_standar)


factor_rendimiento = len(muestra) / tam_muestra * 100
print('Factor de rendimiento:', factor_rendimiento, '%')