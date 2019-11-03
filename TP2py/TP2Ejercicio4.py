import simpy
import random

#Unidad de tiempo: milisegundo
#0.7s son  700ms
#0.8s son  800ms
#1.0s son 1000ms
#4.0s son 4000ms

#Configuracion
#Cantidad de solicitudes a procesar
cantidad_solicitudes = 100000
#Cantidad de bases de datos a utilizar 1 o 2
cantidad_bases = 2

#Listas para guardar los tiempos
tiemposEsperas=[]
tiemposTotales=[]

#Modo DEBUG, imprime las listas de tiempos
modo_debug = False

def atenderSolicitud(env, baseDatos, mu, id_solicitud): 
    
    global tiemposEsperas
    global tiemposTotales

    t_atencion = random.expovariate(mu)

    tiempoInicio = env.now
    db = baseDatos.request()
    yield db
    tiempoEspera = env.now - tiempoInicio
    tiemposEsperas.append(tuple((id_solicitud, tiempoEspera)))
    yield env.timeout(t_atencion)
    baseDatos.release(db)
    tiempoTotal = env.now - tiempoInicio
    tiemposTotales.append(tuple((id_solicitud, tiempoTotal)))

class generadorSolicitudes:
    
    def __init__(self, env, cantidad, bases):
        
        self.env = env
        self.action = env.process(self.generarSolicitudes(env, cantidad, bases))

    def generarSolicitudes(self, env, cantidad, bases):

        baseDatos1 = simpy.Resource(env, capacity=1)
        baseDatos2 = simpy.Resource(env, capacity=1)
        
        id_solicitud = 0
        for i in range(cantidad):
            
            if (bases == 1):

                mu1 = 800
                solicitud = env.process(atenderSolicitud(env, baseDatos1, mu1, id_solicitud))

            else:
                
                mu1 =  700
                mu2 = 1000

                if (random.uniform(0, 1) > 0.6):
                    
                    solicitud = env.process(atenderSolicitud(env, baseDatos2, mu2, id_solicitud))
            
                else:
                    
                    solicitud = env.process(atenderSolicitud(env, baseDatos1, mu1, id_solicitud))

            tiempoEntreSolicitudes = random.expovariate(4000)
            yield env.timeout(tiempoEntreSolicitudes)
            
            id_solicitud = id_solicitud + 1

def generarPrueba(cantBases):
    #Listas para guardar los tiempos
    
    global tiemposEsperas
    global tiemposTotales
    
    tiemposEsperas = []
    tiemposTotales = []

    cantidad_bases = cantBases
    cantidad_solicitudes = 100000

    #Inicializacion del entorno
    env = simpy.Environment()

    #Generacion de solicitudes y ejecucion de la simulacion
    solicitudes = generadorSolicitudes(env, cantidad_solicitudes, cantidad_bases)
    env.run()

    #Calculo de elementos con tiempo de espera 0
    cantSinEspera = 0
    for t in tiemposEsperas:
        if t[1] == 0:
            cantSinEspera = cantSinEspera + 1

    textBase=" base:"
    if cantBases==2:
        textBase=" bases:"

    #Impresion de resultados
    print("Resultado con " + str(cantBases) + textBase)
    print("Cantidad de solicitudes procesadas: %d" % len(tiemposEsperas))
    print("Cantidad de solicitudes sin espera: %d" % cantSinEspera)
    print("Fracción de solicitudes sin espera: %f" %(cantSinEspera/len(tiemposEsperas)))
    print("Media de espera (ms): %f" %(sum([t[1] for t in tiemposEsperas])/len(tiemposEsperas)))
    print("Media de espera y procesamiento (ms): %f" %(sum([t[1] for t in tiemposTotales])/len(tiemposTotales)))
    print("")

    #Impresion de listas de tiempos
    if (modo_debug == True):
       
        print(tiemposEsperas)
        print(tiemposTotales)    

generarPrueba(1)
generarPrueba(2)