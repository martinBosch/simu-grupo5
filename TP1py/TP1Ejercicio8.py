

from matplotlib import pyplot as plt
import scipy.stats as stats



class GCL:
    """Generador Lineal Congruente

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


m = 2**32
a = 1013904223
c = 1664525

padrones = [93272, 92028, 79979, 96749]
x0 = int(sum(padrones)/len(padrones))


def generar_secuencia(secuencia_largo):
    gcl = GCL(m, a, c, x0)
    secuencia = []
    for i in range(secuencia_largo):
        secuencia.append(gcl.generar_numero_aleatorio_uniforme())

    return secuencia

tam_muestra = 10000



a,b = 0.3,0.6

#calculo las probabilidades, corto cuando ya no distingo diferencia
probs = [b-a]
termino = False
i = 1
while not termino:
	nuevaProb = probs[0] * ((1-probs[0]) ** i)

	if nuevaProb == probs[i-1]:
		termino = True

	else:
		probs.append(nuevaProb)
		i += 1


muestras = generar_secuencia(tam_muestra)
#calculo cantidad de veces que cai 0 afuera, 1 afuera, 2 afuera...
primero = True
contador_local = 0
numeros = {}
for x in muestras:
	if (x>=a and x<=b and primero):
		primero = False
	if (x>=a and x<=b and not primero):
		veces = numeros.get(contador_local,0)
		numeros[contador_local] = veces + 1
		contador_local = 0
	if ((x<a or x>b) and not primero):
		contador_local+=1


#ajusto para que sean frecuencias
total = sum(numeros.values())
for k in numeros.keys():
	numeros[k] /= total

#lo paso a lista y relleno con 0 donde no tuve apariciones
lista = []
for i in range(2084):
	lista.append(numeros.get(i,0))

Dsquared, p = stats.chisquare(lista, f_exp=probs)

t = stats.chi2.ppf(q=0.99, df=10)

print ("Aplicamos test chi cuadrado a los resultados de test gap.")
print ("t: " + str(t))
print ("D^2 : " + str(Dsquared))

if (Dsquared < t):
	print("ACEPTAMOS la hipotesis con un error del 1% para el gap test con intervalo [{0}, {1}].".format(a, b))
else:
	print("RECHAZAMOS la hipotesis con un error del 1% para el gap test con intervalo [{0}, {1}].".format(a, b))
	t = stats.chi2.ppf(q=0.95, df=10)
	print ("Aplicamos test chi cuadrado a los resultados de test gap.")
	print ("t: " + str(t))
	print ("D^2 : " + str(Dsquared))
	if (Dsquared < t):
		print("ACEPTAMOS la hipotesis con un error del 5% para el gap test con intervalo [{0}, {1}].".format(a, b))
	else:
		print("RECHAZAMOS la hipotesis con un error del 5% para el gap test con intervalo [{0}, {1}].".format(a, b))
