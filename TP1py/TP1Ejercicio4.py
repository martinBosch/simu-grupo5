from matplotlib import pyplot as plt
# from matplotlib import pyplot as plt
import numpy as np

#Generamos los puntos
tam_muestra = 1000
u1 = np.random.uniform(0, 1, tam_muestra)
u2 = np.random.uniform(0, 1, tam_muestra)

#Definimos el angulo de rotacion
alpha = np.radians(45)

#La matriz de rotacin es
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
Fu1 = Fu1 * 10 + 10
Fu2 = Fu2 * 10 + 3

#Graficamos
plt.scatter(u1, u2)
plt.show()
plt.scatter(Fu1,Fu2)
plt.show()
