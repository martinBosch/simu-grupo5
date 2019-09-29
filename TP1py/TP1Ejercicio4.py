from matplotlib import pyplot as plt
import numpy as np

tam_muestra = 1000

u1 = np.random.uniform(0, 1, tam_muestra)
u2 = np.random.uniform(0, 1, tam_muestra)

u1 = u1 * 10 +5
u2 = u2 * 10 +5

plt.scatter(u1, u2)
plt.show()