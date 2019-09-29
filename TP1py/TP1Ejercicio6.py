from matplotlib import pyplot as plt

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
        muestra.append('A')
    elif u > 0.1 and u <= 0.6:
        muestra.append('B')
    elif u > 0.6 and u <= 0.9:
        muestra.append('C')
    elif u > 0.9 and u <= 1:
        muestra.append('D')

plt.hist(muestra)
plt.show()