# GCL
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

    def generar_muestra(self, muestra_largo):
        muestra = []
        for i in range(muestra_largo):
            muestra.append(self.generar_numero_aleatorio())

        return muestra


class GCL01(GCL):
    """Generador Lineal Congruente con distribucion [0, 1]
    """

    def generar_numero_aleatorio(self):
        return super().generar_numero_aleatorio()/self.m
