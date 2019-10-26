
import matplotlib.pyplot as plt
import numpy as np

a=10
b=1
c=0.4
d=0.9
P0=10

evolucion_qs = [a-b*P0]
evolucion_ps = [P0]

for i in range(100):
 
	Qt = d * evolucion_ps[i-1] - c
	Pt = (a - Qt)/b


	evolucion_qs.append(Qt)
	evolucion_ps.append(Pt)


print(evolucion_ps, evolucion_qs)
#Evolucion del precio en funcion del tiempo en 100 periodos
plt.plot(evolucion_ps)
plt.show()

#INCLUIR COBWEB PLOT
def f(c,x): return x**2 + c
n = 100
c = -1.2
x0 = 1.23
x1 = x0
cobweb_xs = [x1]
cobweb_ys = [x1]
for i in range(n):
    x2 = f(c,x1)
    cobweb_xs.append(x1)
    cobweb_ys.append(x2)
    x1 = x2
    cobweb_xs.append(x1)
    cobweb_ys.append(x2)
graph_xs = np.linspace(-2,2,100)
graph_ys = f(c, graph_xs)
start = x1
end = x2

for i in range(1,len(cobweb_xs)):
    plt.plot([cobweb_xs[i-1],cobweb_xs[i]],[cobweb_ys[i-1],cobweb_ys[i]],'k', alpha=0.2, linewidth=0.5)
plt.plot([-2,2],[-2,2], 'k', linewidth=2)
plt.plot(graph_xs,graph_ys, 'k', linewidth=3)
plt.plot(x0,x0, 'go', zorder=5)
plt.plot(x2,x2, 'ro', zorder=5)

ax = plt.gca()
ax.set_aspect(1)
ax.set_ylim(-2,2)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-2,2)

fig = ax.figure
fig.set_figwidth(8)
fig.set_figheight(8)
plt.show()