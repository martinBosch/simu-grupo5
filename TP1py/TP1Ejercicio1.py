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


# GCL
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

    def generar_muestra(self, muestra_largo):
        muestra = []
        for i in range(muestra_largo):
            muestra.append(self.generar_numero_aleatorio())

        return muestra


m = 2**32
a = 1013904223
c = 1664525
padrones = [93272, 92028, 79979, 96749]
x0 = int(sum(padrones)/len(padrones))


gcl = GCL(m, a, c, x0)
tam_muestra = 10
primeros_diez = gcl.generar_muestra(tam_muestra)
print("Primeros 10 números generados:")
print(primeros_diez)
print("\n")


class GCL01(GCL):
    """Generador Lineal Congruente con distribucion [0, 1]
    """

    def generar_numero_aleatorio(self):
        return super().generar_numero_aleatorio()/m


gcl01 = GCL01(m, a, c, x0)
tam_muestra = 100000
print("Generando secuencia de "+str(tam_muestra)+" valores")
muestra = gcl01.generar_muestra(tam_muestra)

print("Generando histograma...")
plt.hist(muestra, 'sturges')
plt.show()
