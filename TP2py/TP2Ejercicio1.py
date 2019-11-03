import matplotlib.pyplot as plt
import numpy as np
from scipy import stats as sp
from random import random, uniform


## 1.a
tiempos_entre_arribos_file = open('datosTP2EJ1.txt', 'r')

tiempos_entre_arribos = tiempos_entre_arribos_file.readlines()
tiempos_entre_arribos = [float(t.rstrip()) for t in tiempos_entre_arribos]

tam_muestra = len(tiempos_entre_arribos)

# grafico un histograma para ver que distribucion siguen los valores de la muestra
plt.title('Histograma tiempo entre arribos')
plt.hist(tiempos_entre_arribos, 100)
plt.show()

# calculo la media de la muestra para saber cual de las dos propuestas se asemeja mas a la
# distribucion de la muestra
media_tiempo_entre_arribos = np.mean(tiempos_entre_arribos)
print('Media de los tiempos entre arribos:', media_tiempo_entre_arribos)

# otra forma de decidir cual de las dos propuestas se asemeja mas a la distribucion de la muestra es
# aplicar un test de Kolmogorov-Smirnov (ya que la distribucion es continua) a la muestra

# Aplicamos el test
D2, p = sp.kstest(tiempos_entre_arribos, 'expon', args=(0, 180), N=tam_muestra)
print('Test de Kolmogorov-Smirnov para exponencial de media 180')
print('D^2:', D2, 'p:', p)

# como p = 0.57 es mayor a 0.01 no rechazamos H0 (que dice que ambas distribuciones son idénticas). Es decir,
# la muestra dada sigue una distribucion exponencial de media 180

# Propuesta 2: exponencial con media 240

D2, p = sp.kstest(tiempos_entre_arribos, 'expon', args=(0, 240), N=tam_muestra)
print('Test de Kolmogorov-Smirnov para exponencial de media 240')
print('D^2:', D2, 'p:', p)

# como p = 3.95e-12 es menor a 0.01 rechazamos H0 (que dice que ambas distribuciones son idénticas). Es decir,
# la muestra dada no sigue una distribucion exponencial de media 240


## 1.b
def simular_un_dia():
    # clientes_info: es una lista de tuplas del tipo (t, t_uso_cajero, cantidad_billetes) que
    # representa la informacion de un cliente en el sistema, siendo:
    # t: tiempo del dia en que arribo el cliente
    # t_uso_cajero: tiempo que el cliente uso el cajero
    # cantidad_billetes: cantidad de billetes que el cliente retiro o deposito

    clientes_info = []
    t = 0
    dia = 24*60*60
    while t <= dia:
        # arribo un cliente: tiempo entre clientes sigue una distribucion exponencial de media 180
        t1 = sp.expon.rvs(0, 180)
        t += t1

        # u: para decidir si el cliente que arribo es del grupo 1 o grupo 2
        u = random()
        if u <= 0.75: # grupo 1
            # el cliente usa el cajero
            t_uso_cajero = sp.expon.rvs(0, 90)
            # el cliente retira dinero
            cantidad_billetes = -uniform(3, 50)
        else: # grupo 2
            # el cliente usa el cajero
            t_uso_cajero = sp.expon.rvs(0, 300)
            # el cliente deposita dinero
            cantidad_billetes = uniform(10, 100)

        clientes_info.append( (t, t_uso_cajero, cantidad_billetes) )

    return clientes_info

## 1.c
TIEMPO_DE_ARRIBO = 0
TIEMPO_USO_CAJERO = 1
CANTIDAD_DE_BILLETES = 2

cajero_cantidad_billetes = 2000
billetes_en_el_cajero = []
cantidad_clientes_no_pudo_retirar = 0
cantidad_clientes_quisieron_retirar = 0

clientes_info = simular_un_dia()
for i in range(len(clientes_info)):
    cliente_actual = clientes_info[i]
    cantidad_billetes_cliente_actual = cliente_actual[CANTIDAD_DE_BILLETES]
    if cantidad_billetes_cliente_actual < 0: #retira dinero
        cantidad_clientes_quisieron_retirar += 1

    cajero_cantidad_billetes_despues_transcaccion = cajero_cantidad_billetes + cantidad_billetes_cliente_actual
    if cajero_cantidad_billetes_despues_transcaccion < 0 or cajero_cantidad_billetes_despues_transcaccion > 2000:
        # el cliente no pudo realizar la transaccion
        if cantidad_billetes_cliente_actual < 0: #retira dinero
            cantidad_clientes_no_pudo_retirar += 1
    else:
        cajero_cantidad_billetes += cantidad_billetes_cliente_actual

    billetes_en_el_cajero.append(cajero_cantidad_billetes)

plt.title('cantidad de billetes en el cajero luego de cada trancaccion')
plt.plot(billetes_en_el_cajero)
plt.show()

#1.d
tiempo_en_el_sistema = []

billetes_en_el_cajero = []
cantidad_clientes_no_pudo_retirar = 0
cantidad_clientes_quisieron_retirar = 0


for i in range(1000):
    cajero_cantidad_billetes = 2000

    clientes_info = simular_un_dia()
    for i in range(len(clientes_info)):
        cliente_actual = clientes_info[i]
        # el primer cliente no espera
        if i == 0:
            t_uso_cajero = cliente_actual[TIEMPO_USO_CAJERO]
            tiempo_en_el_sistema.append(t_uso_cajero)
        else:
            cliente_anterior = clientes_info[i-1]
            # cliente anterior
            t_arribo_cliente_anterior = cliente_anterior[TIEMPO_DE_ARRIBO]
            t_uso_cajero_cliente_anterior = cliente_anterior[TIEMPO_USO_CAJERO]
            t_salida_cliente_anterior = t_arribo_cliente_anterior + tiempo_en_el_sistema[i-1]

            # cliente actual
            t_arribo_cliente_actual = cliente_actual[TIEMPO_DE_ARRIBO]
            t_uso_cajero_cliente_actual = cliente_actual[TIEMPO_USO_CAJERO]

            t_espera_cliente_actual = t_salida_cliente_anterior - t_arribo_cliente_actual
            # si el cliente anterior termino antes que arribe el actual no hay espera
            if t_espera_cliente_actual < 0:
                t_espera_cliente_actual = 0
            tiempo_en_el_sistema.append(t_espera_cliente_actual + t_uso_cajero_cliente_actual)

        cantidad_billetes_cliente_actual = cliente_actual[CANTIDAD_DE_BILLETES]
        if cantidad_billetes_cliente_actual < 0: #retira dinero
            cantidad_clientes_quisieron_retirar += 1

        cajero_cantidad_billetes_despues_transcaccion = cajero_cantidad_billetes + cantidad_billetes_cliente_actual
        if cajero_cantidad_billetes_despues_transcaccion < 0 or cajero_cantidad_billetes_despues_transcaccion > 2000:
            # el cliente no pudo realizar la transaccion
            if cantidad_billetes_cliente_actual < 0: #retira dinero
                cantidad_clientes_no_pudo_retirar += 1
        else:
            cajero_cantidad_billetes += cantidad_billetes_cliente_actual

        billetes_en_el_cajero.append(cajero_cantidad_billetes)


t_medio_cliente_en_sistema = np.mean(tiempo_en_el_sistema)
print('tiempo medio que los clientes demoraron en el sistema:', t_medio_cliente_en_sistema)

#1.e
# porcentaje clientes no pudieron retirar dinero
porcentaje_cliente_no_pudo_retirar = cantidad_clientes_no_pudo_retirar * 100 / cantidad_clientes_quisieron_retirar
print('porcentaje de clientes que no pudieron retirar dinero:', porcentaje_cliente_no_pudo_retirar, '%')
