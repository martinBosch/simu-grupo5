#75.26 Simulación - TP1
#Grupo 5
#79979 – González, Juan Manuel (juanmg0511@gmail.com)<br />
#92028 – Tusca, Bautista (bautista.tusca@gmail.com)<br />
#93272 – Zapico, Rodrigo (rodri.zapico@gmail.com)<br />
#96749 – Bosch, Martín (martinbosch17@gmail.com)

#Ejercicio 1
import numpy as np
import matplotlib.pyplot as plt

#Tamaño gráficos
plt.style.use('default')
plt.rcParams['figure.figsize'] = (15, 10)

#GCL

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

tam_muestra = 10
primeros_diez = generar_secuencia(tam_muestra)
print("Primeros 10 números generados:")
print(primeros_diez)
print("\n")


class GCL_01(GCL):
    """Generador Lineal Congruente con distribucion [0, 1]
    """

    def generar_numero_aleatorio(self):
        return super().generar_numero_aleatorio()/m

    def generar_secuencia(secuencia_largo):
        gcl = GCL_01(m, a, c, x0)
        secuencia = []
        for i in range(secuencia_largo):
            secuencia.append(gcl.generar_numero_aleatorio())

        return secuencia

tam_muestra = 100000
print("Generando secuencia de "+str(tam_muestra)+" valores")
muestra = generar_secuencia(tam_muestra)

print("Generando histograma...")
plt.hist(muestra, 'sturges')
plt.show()