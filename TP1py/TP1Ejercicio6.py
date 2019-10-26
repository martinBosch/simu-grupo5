#75.26 Simulación - TP1
#Grupo 5
#79979 – González, Juan Manuel (juanmg0511@gmail.com)<br />
#92028 – Tusca, Bautista (bautista.tusca@gmail.com)<br />
#93272 – Zapico, Rodrigo (rodri.zapico@gmail.com)<br />
#96749 – Bosch, Martín (martinbosch17@gmail.com)

#Ejercicio 6
from matplotlib import pyplot as plt

from gcl import GCL01
from constantes import m, a, c, x0


#Tamaño gráficos
plt.style.use('default')
plt.rcParams['figure.figsize'] = (15, 10)


gcl01 = GCL01(m, a, c, x0)
tam_muestra = 100000
muestra = []
for i in range(tam_muestra):
    u = gcl01.generar_numero_aleatorio()
    if u >= 0 and u <= 0.1:
        muestra.append('A')
    elif u > 0.1 and u <= 0.6:
        muestra.append('B')
    elif u > 0.6 and u <= 0.9:
        muestra.append('C')
    elif u > 0.9 and u <= 1:
        muestra.append('D')

plt.hist(muestra)
plt.show()
