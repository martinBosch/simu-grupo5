

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




class GCL:
    """Generador Lineal Congruente

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



m = 2**32
a = 1013904223
c = 1664525

padrones = [93272, 92028, 79979, 96749]
x0 = int(sum(padrones)/len(padrones))


def generar_secuencia(secuencia_largo):
    gcl = GCL(m, a, c, x0)
    secuencia = []
    for i in range(secuencia_largo):
        secuencia.append(gcl.generar_numero_aleatorio())

    return secuencia


tam_muestra = 10000
resultados_previos = generar_secuencia(tam_muestra)

resultados = resultados_previos[1:]
resultados_previos = resultados_previos[:-2]

resultados_siguientes = resultados[1:]
resultados = resultados[:-1]

plt.scatter(resultados_previos, resultados)

fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(resultados_previos, resultados, resultados_siguientes)

plt.show()