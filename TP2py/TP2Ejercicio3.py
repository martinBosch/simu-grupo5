
import matplotlib.pyplot as plt
import numpy as np

#Parte 1
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

#COBWEB PLOT
n = 100
Qt = d * P0 - c
Pt = (a - (d * P0 - c))/b
x0=P0
cobweb_xs = [P0]
cobweb_ys = [P0]
for i in range(n):
    Pt = (a - (d * P0 - c))/b
    cobweb_xs.append(P0)
    cobweb_ys.append(Pt)
    P0 = Pt
    cobweb_xs.append(P0)
    cobweb_ys.append(Pt)
graph_xs = np.linspace(0,10,100)
graph_ys = (a - (d * graph_xs - c))/b
start = P0
end = Pt

for i in range(1,len(cobweb_xs)):
    plt.plot([cobweb_xs[i-1],cobweb_xs[i]],[cobweb_ys[i-1],cobweb_ys[i]],'k', alpha=0.2, linewidth=0.5)
plt.plot([0,10],[0,10], 'k', linewidth=2)
plt.plot(graph_xs,graph_ys, 'k', linewidth=3)
plt.plot(x0,x0, 'go', zorder=5)
plt.plot(Pt,Pt, 'ro', zorder=5)

ax = plt.gca()
ax.set_aspect(1)
ax.set_ylim(0,10)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0,10)

fig = ax.figure
fig.set_figwidth(8)
fig.set_figheight(8)
plt.show()


#Parte 2
a=0.9
b=0.89
c=0.5
d=0.9
P0=1

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

#COBWEB PLOT
n = 100
Qt = d * P0 - c
Pt = (a - (d * P0 - c))/b
x0=P0
cobweb_xs = [P0]
cobweb_ys = [P0]
for i in range(n):
    Pt = (a - (d * P0 - c))/b
    cobweb_xs.append(P0)
    cobweb_ys.append(Pt)
    P0 = Pt
    cobweb_xs.append(P0)
    cobweb_ys.append(Pt)
graph_xs = np.linspace(0,1.6,100)
graph_ys = (a - (d * graph_xs - c))/b
start = P0
end = Pt

for i in range(1,len(cobweb_xs)):
    plt.plot([cobweb_xs[i-1],cobweb_xs[i]],[cobweb_ys[i-1],cobweb_ys[i]],'k', alpha=0.2, linewidth=0.5)
plt.plot([0,1.6],[0,1.6], 'k', linewidth=2)
plt.plot(graph_xs,graph_ys, 'k', linewidth=3)
plt.plot(x0,x0, 'go', zorder=5)
plt.plot(Pt,Pt, 'ro', zorder=5)

ax = plt.gca()
ax.set_aspect(1)
ax.set_ylim(0,1.6)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0,1.6)

fig = ax.figure
fig.set_figwidth(8)
fig.set_figheight(8)
plt.show()

