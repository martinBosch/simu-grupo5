from scipy import stats as sp
import matplotlib.pyplot as plt

m = 2**32
a = 1013904223
c = 1664525

padrones = [93272, 92028, 79979, 96749]
x0 = int(sum(padrones)/len(padrones))

class GCL_01():

    """Generador Lineal Congruente con distribucion [0, 1]
    atributos:
     m: el modulo
     a: el multiplicador
     c: el incremento
     xn: ultimo valor generado
    """

    def __init__(self, m, a, c, x0):
        self.m = m
        self.a = a
        self.c = c
        self.xn = x0

    def generar_numero_aleatorio(self):
        self.xn = (self.a * self.xn + self.c) % self.m
        return self.xn

    def generar_numero_aleatorio_uniforme(self):
        return self.generar_numero_aleatorio()/m


tam_muestra = 100000
muestra = []

gcl = GCL_01(m, a, c, x0)
for i in range(tam_muestra):
    u = gcl.generar_numero_aleatorio_uniforme()
    if u >= 0 and u <= 0.1:
        muestra.append(1)
    elif u > 0.1 and u <= 0.6:
        muestra.append(2)
    elif u > 0.6 and u <= 0.9:
        muestra.append(3)
    elif u > 0.9 and u <= 1:
        muestra.append(4)

	

#cuento las apariciones
obs_values = [0 for i in range(4)]
for i in muestra:
	obs_values[i-1] += 1


expected_p_values = [0.1, 0.5, 0.3, 0.1]
expected_values = [100000*i for i in expected_p_values]


statistic, pvalue = sp.chisquare(obs_values, f_exp=expected_values)

print(statistic, pvalue)


#si pvalue <= alfa entonces rechazo H0 (digo que son distintas)

if pvalue <= 0.01:
	print("las distribuciones NO son las mismas con nivel de significación de 0.01")

else:
	if pvalue <= 0.05:
		print("las distribuciones NO son las mismas con nivel de significación de 0.05")
	else:
		print("las distribuciones coinciden")