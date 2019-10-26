#75.26 Simulación - TP1
#Grupo 5
#79979 – González, Juan Manuel (juanmg0511@gmail.com)<br />
#92028 – Tusca, Bautista (bautista.tusca@gmail.com)<br />
#93272 – Zapico, Rodrigo (rodri.zapico@gmail.com)<br />
#96749 – Bosch, Martín (martinbosch17@gmail.com)

#Ejercicio 7
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from gcl import GCL
from constantes import m, a, c, x0


#Tamaño gráficos
plt.style.use('default')
plt.rcParams['figure.figsize'] = (15, 10)


gcl = GCL(m, a, c, x0)
tam_muestra = 10000
resultados_previos = gcl.generar_muestra(tam_muestra)

resultados = resultados_previos[1:]
resultados_previos = resultados_previos[:-2]

resultados_siguientes = resultados[1:]
resultados = resultados[:-1]

plt.scatter(resultados_previos, resultados)

fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(resultados_previos, resultados, resultados_siguientes)

plt.show()