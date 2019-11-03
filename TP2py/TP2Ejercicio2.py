import numpy as np
from random import random
import matplotlib.pyplot as plt

cantidad_solicitudes = 0
estados = [cantidad_solicitudes]
veces_cero_solicitudes = 1

N = int(1000/0.01)
for i in range(1, N+1):
    u = random()
    if cantidad_solicitudes == 0:
        if u < 1/40: # ingresa una solicitud
            cantidad_solicitudes += 1
        else:
            veces_cero_solicitudes += 1
    else:
        prob_no_ingresa_solicitud_y_siga_procesando = (39/40)*(29/30) + (1/40)*(1/30)
        prob_ingresa_solicitud_y_siga_procesando = (1/40)*(29/30)
        prob_no_ingresa_solicitud_y_termina_procesar = (39/40)*(1/30)
        if u < prob_no_ingresa_solicitud_y_termina_procesar: # no ingreso solicitud y termina de procesar
            cantidad_solicitudes -= 1
        elif prob_no_ingresa_solicitud_y_termina_procesar <= u < prob_no_ingresa_solicitud_y_termina_procesar+prob_ingresa_solicitud_y_siga_procesando: # ingresa solicitud y sigue procesando
            cantidad_solicitudes += 1
        else: # si no ingresa solicitud y sigue procesando o si ingresa solicitud y termino de procesar
              # la cantidad de solicitudes se mantiene
            pass

    estados.append(cantidad_solicitudes)

plt.title('Cantidad de solicitudes en cada instante')
plt.plot(estados)
plt.show()

plt.xticks(np.arange(0, max(estados), step=1))
plt.hist(estados, np.arange(0, max(estados), step=1))
plt.show()

print('Porcentaje de tiempo que el servidor estuvo sin procesar solicitudes:', veces_cero_solicitudes / N * 100, '%')
