#75.26 Simulación - TP1
#Grupo 5
#79979 – González, Juan Manuel (juanmg0511@gmail.com)<br />
#92028 – Tusca, Bautista (bautista.tusca@gmail.com)<br />
#93272 – Zapico, Rodrigo (rodri.zapico@gmail.com)<br />
#96749 – Bosch, Martín (martinbosch17@gmail.com)

#Ejercicio 8

from matplotlib import pyplot as plt
import scipy.stats as stats

from gcl import GCL01
from constantes import m, a, c, x0


gcl01 = GCL01(m, a, c, x0)
tam_muestra = 100000
muestra = gcl01.generar_muestra(tam_muestra)


alfa, beta = 0.3, 0.6

#calculo las probabilidades, corto cuando ya no distingo diferencia
esperados = [beta - alfa]
termino = False
i = 1
while not termino:
    nuevaProb = esperados[0] * ((1 - esperados[0]) ** i)

    if nuevaProb == esperados[i - 1]:
        termino = True
    else:
        esperados.append(nuevaProb)
        i += 1


# calculo cantidad de veces que cai 0 afuera, 1 afuera, 2 afuera...
primero = True
contador_veces_cae_afuera = 0
veces_cae_afuera = {}
for x in muestra:
    if (x >= alfa and x <= beta) and primero:
        primero = False
    if (x >= alfa and x <= beta) and not primero:
        veces = veces_cae_afuera.get(contador_veces_cae_afuera, 0)
        veces_cae_afuera[contador_veces_cae_afuera] = veces + 1
        contador_veces_cae_afuera = 0
    if (x < alfa or x > beta) and not primero:
        contador_veces_cae_afuera += 1


# ajusto para que sean frecuencias
total = sum(veces_cae_afuera.values())
for k in veces_cae_afuera.keys():
    veces_cae_afuera[k] /= total


# lo paso a lista y relleno con 0 donde no tuve apariciones
observados = []
for i in range(len(esperados)):
    observados.append(veces_cae_afuera.get(i, 0))


Dsquared, p = stats.chisquare(observados, esperados)
print('D^2:', Dsquared)
print('p:', p)
