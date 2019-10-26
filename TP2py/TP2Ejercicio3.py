
import matplotlib.pyplot as plt

evolucion_qs = [0.2]
evolucion_ps = [8]

for i in range(100):
 
	Qt = evolucion_ps[-1] - 0.4
	Pt = (9 - Qt)/1.1


	evolucion_qs.append(Qt)
	evolucion_ps.append(Pt)


print(evolucion_ps, evolucion_qs)
plt.plot(evolucion_ps)
plt.show()
plt.plot(evolucion_qs, evolucion_ps)
plt.show()