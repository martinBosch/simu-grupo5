import numpy as np
from matplotlib import pyplot as plt
from math import exp
from math import log

m = 2**32
a = 1013904223
c = 1664525

padrones = [93272, 92028, 79979, 96749]
x0 = int(sum(padrones)/len(padrones))

class GCL_01():

    """Generador Lineal Congruente con distribucion [0, 1]
    atributos:
     m: el modulo
     a: el multiplicador
     c: el incremento
     xn: ultimo valor generado
    """

    def __init__(self, m, a, c, x0):
        self.m = m
        self.a = a
        self.c = c
        self.xn = x0

    def generar_numero_aleatorio(self):
        self.xn = (self.a * self.xn + self.c) % self.m
        return self.xn

    def generar_numero_aleatorio_uniforme(self):
        return self.generar_numero_aleatorio()/m

    def generar_secuencia(secuencia_largo):
        gcl = GCL_01(m, a, c, x0)
        secuencia = []
        for i in range(secuencia_largo):
            secuencia.append(gcl.generar_numero_aleatorio_uniforme())

        return secuencia



def f(t):
    lambda_ = 1/15
    if t >= 0 and t < 10:
        return 1/25
    elif t >= 10:
        return 3/5 * lambda_ * exp(-1 * lambda_ * (t - 10))

x = np.arange(0.0, 100.0, 1)
y = np.array(list(map(f, x)))


print("Graficando función de densidad de probabilidad del 2.a:")
plt.plot(x, y)
plt.show()


print("Graficando función de probabilidad acumulada del 2.b:")
def F(t):
    lambda_ = 1/15
    if t >= 0 and t < 10:
        return t/25
    elif t >= 10:
        return (10/25) + (3/5) - (3/5) * exp(-1 * lambda_ * (t - 10))

x = np.arange(0.0, 100.0, 1)
y = np.array(list(map(F, x)))

plt.plot(x, y)
plt.show()

print("Graficando función inversa de la función de probabilidad acumulada del 2.b:")
def F_inversa(t):
    lambda_ = 1/15
    if t >= 0 and t < 10/25:
        return 25*t
    elif t >= 10/25:
        return (-1/lambda_) * log( (5/3) - (5/3) * t) + 10

x = np.arange(0.0, 1.0, 0.05)
y = np.array(list(map(F_inversa, x)))

plt.plot(x, y)
plt.show()


tam_muestra = 100000
# muestra de numeros aleatorios con distrib uniforme [0, 1]
muestra = GCL_01.generar_secuencia(tam_muestra)

print("Aplicando método de la transformada")
y = np.array(list(map(F_inversa, muestra)))

print("Generando histograma")
plt.hist(y, 100)
plt.show()