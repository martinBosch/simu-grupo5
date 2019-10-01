#75.26 Simulación - TP1
#Grupo 5
#79979 – González, Juan Manuel (juanmg0511@gmail.com)<br />
#92028 – Tusca, Bautista (bautista.tusca@gmail.com)<br />
#93272 – Zapico, Rodrigo (rodri.zapico@gmail.com)<br />
#96749 – Bosch, Martín (martinbosch17@gmail.com)

#Ejercicio 5
from matplotlib import pyplot as plt
import numpy as np

#Tamaño gráficos
plt.style.use('default')
plt.rcParams['figure.figsize'] = (15, 10)

tam_muestra = 100000

u1 = np.random.uniform(0, 1, tam_muestra)
u2 = np.random.uniform(0, 1, tam_muestra)

z1 = np.sqrt(-2*np.log(u1))*np.cos(2*np.pi*u2)
z2 = np.sqrt(-2*np.log(u1))*np.sin(2*np.pi*u2)

plt.hist(z1, 100)
plt.title('Z1')
plt.show()

plt.hist(z2, 100)
plt.title('Z2')
plt.show()

# comparo las normales estandar generadas con la generado por scipy
x = np.arange(-5, 5, 0.1)

plt.plot(x, norm.pdf(x, 0, 1), color='r')
plt.hist(z1, 100, density=True)
plt.title('Z1')
plt.show()

plt.plot(x, norm.pdf(x, 0, 1), color='r')
plt.hist(z2, 100, density=True)
plt.title('Z2')
plt.show()

# Calculo la media y varianza de la distribución obtenida y la comparo contra los valores teóricos.
media_teorica = 0
desvio_estandar_teorico = 1

# Para z1
media_muestra = np.mean(z1)
print('Media de la muestra z1:', media_muestra)
print('Diferencia hasta la media teorica:', media_teorica - media_muestra)
print('')

muestra_desvio_estandar = np.std(z1)
print('Desvio estandar de la muestra z1:', muestra_desvio_estandar)
print('Diferencia hasta el devio estandar teorico:', desvio_estandar_teorico - muestra_desvio_estandar)
print('')

# Para z2
media_muestra = np.mean(z2)
print('Media de la muestra z2:', media_muestra)
print('Diferencia hasta la media teorica:', media_teorica - media_muestra)
print('')

muestra_desvio_estandar = np.std(z2)
print('Desvio estandar de la muestra z2:', muestra_desvio_estandar)
print('Diferencia hasta el devio estandar teorico:', desvio_estandar_teorico - muestra_desvio_estandar)
print('')
