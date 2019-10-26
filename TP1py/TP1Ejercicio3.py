#75.26 Simulación - TP1
#Grupo 5
#79979 – González, Juan Manuel (juanmg0511@gmail.com)<br />
#92028 – Tusca, Bautista (bautista.tusca@gmail.com)<br />
#93272 – Zapico, Rodrigo (rodri.zapico@gmail.com)<br />
#96749 – Bosch, Martín (martinbosch17@gmail.com)

#Ejercicio 3
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm

from TP1Ejercicio3_helper import normal_estandar, exponencial, generar_muestra_normal


#Tamaño gráficos
plt.style.use('default')
plt.rcParams['figure.figsize'] = (15, 10)


x = np.arange(0, 10, 0.1)
y = np.array(list(map(normal_estandar, x)))
plt.title('Normal estandar')
plt.plot(x, y)
plt.show()


x = np.arange(0, 10, 0.1)
y = np.array(list(map(exponencial, x)))
plt.title('Exponencial de media 1')
plt.plot(x, y)
plt.show()


# comparo la distribucion normal estandar y la exponencial de media 1
x1 = np.arange(0, 10, 0.1)
y1 = np.array(list(map(normal_estandar, x1)))

y2 = np.array(list(map(exponencial, x1)))

plt.plot(x1, y1, label='fx')
plt.plot(x1, y2, label='fy')
plt.title('Comparación normal estandar y exponencial de media 1')
plt.legend()
plt.show()


media, desvio_estandar = 15, 3
tam_muestra = 100000
muestra = generar_muestra_normal(tam_muestra, media, desvio_estandar)


plt.hist(muestra, 100)
plt.show()


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