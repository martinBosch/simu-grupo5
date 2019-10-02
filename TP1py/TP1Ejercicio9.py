#75.26 Simulación - TP1
#Grupo 5
#79979 – González, Juan Manuel (juanmg0511@gmail.com)<br />
#92028 – Tusca, Bautista (bautista.tusca@gmail.com)<br />
#93272 – Zapico, Rodrigo (rodri.zapico@gmail.com)<br />
#96749 – Bosch, Martín (martinbosch17@gmail.com)

#Ejercicio 9
from scipy import stats as sp
from gcl import GCL01
from constantes import m, a, c, x0


gcl01 = GCL01(m, a, c, x0)
tam_muestra = 100000
muestra = []
for i in range(tam_muestra):
    u = gcl01.generar_numero_aleatorio()
    if u >= 0 and u <= 0.1:
        muestra.append(1)
    elif u > 0.1 and u <= 0.6:
        muestra.append(2)
    elif u > 0.6 and u <= 0.9:
        muestra.append(3)
    elif u > 0.9 and u <= 1:
        muestra.append(4)


# cuento las apariciones
obs_values = [0 for i in range(4)]
for i in muestra:
    obs_values[i-1] += 1
print('observados:', obs_values)


expected_p_values = [0.1, 0.5, 0.3, 0.1]
expected_values = [100000*i for i in expected_p_values]
print('esperados:', expected_values)


D2, p = sp.chisquare(obs_values, f_exp=expected_values)
print('D^2:', D2, 'p:', p)
