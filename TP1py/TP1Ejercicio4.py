#75.26 Simulación - TP1
#Grupo 5
#79979 – González, Juan Manuel (juanmg0511@gmail.com)<br />
#92028 – Tusca, Bautista (bautista.tusca@gmail.com)<br />
#93272 – Zapico, Rodrigo (rodri.zapico@gmail.com)<br />
#96749 – Bosch, Martín (martinbosch17@gmail.com)

#Ejercicio 4
from matplotlib import pyplot as plt
import numpy as np

#Tamaño gráficos
plt.style.use('default')
plt.rcParams['figure.figsize'] = (15, 10)

#Generamos los puntos
tam_muestra = 1000
u1 = np.random.uniform(0, 1, tam_muestra)
u2 = np.random.uniform(0, 1, tam_muestra)

#Acotamos al intervalo requerido
u1 = u1 * 5
u2 = u2 * 5

#Definimos el angulo de rotacion
alpha = np.radians(45)

#La matriz de rotación es
R = np.array(( (np.cos(alpha), -np.sin(alpha)),
               (np.sin(alpha),  np.cos(alpha)) ))

#Calculamos los vectores finales, rotados 45º
F = list()
for i in range(999):
    V = np.array((u1[i],u2[i]))
    F.append(R.dot(V))
    
Fu1,Fu2 = zip(*F)
Fu1 = np.array(Fu1)
Fu2 = np.array(Fu2)

#Desplazamos el rombo
Fu1 = Fu1 + 10
Fu2 = Fu2 + (13/2)

#Graficamos
plt.scatter(u1,u2)
plt.show()

plt.scatter(Fu1,Fu2)
plt.show()
