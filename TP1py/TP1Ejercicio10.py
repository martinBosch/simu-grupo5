#75.26 Simulación - TP1
#Grupo 5
#79979 – González, Juan Manuel (juanmg0511@gmail.com)<br />
#92028 – Tusca, Bautista (bautista.tusca@gmail.com)<br />
#93272 – Zapico, Rodrigo (rodri.zapico@gmail.com)<br />
#96749 – Bosch, Martín (martinbosch17@gmail.com)

#Ejercicio 9
from scipy.stats import kstest
from TP1Ejercicio3_helper import generar_muestra_normal


media, desvio_estandar = 15, 3
tam_muestra = 100000
muestra = generar_muestra_normal(tam_muestra, media, desvio_estandar)


stat, p = kstest(muestra, 'norm', args=(media, desvio_estandar), N=tam_muestra)
print('Statistic:', stat, 'p:', p)
