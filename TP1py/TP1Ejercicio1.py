#75.26 Simulación - TP1
#Grupo 5
#79979 – González, Juan Manuel (juanmg0511@gmail.com)<br />
#92028 – Tusca, Bautista (bautista.tusca@gmail.com)<br />
#93272 – Zapico, Rodrigo (rodri.zapico@gmail.com)<br />
#96749 – Bosch, Martín (martinbosch17@gmail.com)

#Ejercicio 1
import numpy as np
import matplotlib.pyplot as plt

from gcl import GCL, GCL01
from constantes import m, a, c, x0


#Tamaño gráficos
plt.style.use('default')
plt.rcParams['figure.figsize'] = (15, 10)


gcl = GCL(m, a, c, x0)
tam_muestra = 10
primeros_diez = gcl.generar_muestra(tam_muestra)
print("Primeros 10 números generados:")
print(primeros_diez)
print("\n")


gcl01 = GCL01(m, a, c, x0)
tam_muestra = 100000
print("Generando secuencia de "+str(tam_muestra)+" valores")
muestra = gcl01.generar_muestra(tam_muestra)

print("Generando histograma...")
plt.hist(muestra, 'sturges')
plt.show()
