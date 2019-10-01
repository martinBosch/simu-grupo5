#75.26 Simulación - TP1
#Grupo 5
#79979 – González, Juan Manuel (juanmg0511@gmail.com)<br />
#92028 – Tusca, Bautista (bautista.tusca@gmail.com)<br />
#93272 – Zapico, Rodrigo (rodri.zapico@gmail.com)<br />
#96749 – Bosch, Martín (martinbosch17@gmail.com)

#Ejercicio 2
import numpy as np
from matplotlib import pyplot as plt
from math import exp
from math import log

from gcl import GCL, GCL01
from constantes import m, a, c, x0


#Tamaño gráficos
plt.style.use('default')
plt.rcParams['figure.figsize'] = (15, 10)


def f(t):
    lambda_ = 1/15
    if t >= 0 and t < 10:
        return 1/25
    elif t >= 10:
        return 3/5 * lambda_ * exp(-1 * lambda_ * (t - 10))


x = np.arange(0.0, 100.0, 1)
y = np.array(list(map(f, x)))
print("Graficando función de densidad de probabilidad del 2.a:")
plt.title('f(t)')
plt.plot(x, y)
plt.show()


def F(t):
    lambda_ = 1/15
    if t >= 0 and t < 10:
        return t/25
    elif t >= 10:
        return (10/25) + (3/5) - (3/5) * exp(-1 * lambda_ * (t - 10))


x = np.arange(0.0, 100.0, 1)
y = np.array(list(map(F, x)))
print("Graficando función de probabilidad acumulada del 2.b:")
plt.title('F(t)')
plt.plot(x, y)
plt.show()


def F_inversa(t):
    lambda_ = 1/15
    if t >= 0 and t < 10/25:
        return 25*t
    elif t >= 10/25:
        return (-1/lambda_) * log( (5/3) - (5/3) * t) + 10


x = np.arange(0.0, 1.0, 0.05)
y = np.array(list(map(F_inversa, x)))
print("Graficando función inversa de la función de probabilidad acumulada del 2.b:")
plt.title('F_inversa(t)')
plt.plot(x, y)
plt.show()


gcl01 = GCL01(m, a, c, x0)
tam_muestra = 100000
# muestra de numeros aleatorios con distrib uniforme [0, 1]
muestra = gcl01.generar_muestra(tam_muestra)

print("Aplicando método de la transformada")
y = np.array(list(map(F_inversa, muestra)))

print("Generando histograma")
plt.hist(y, 100)
plt.show()
