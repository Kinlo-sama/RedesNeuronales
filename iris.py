import pandas as pd
import numpy as np
from ucimlrepo import fetch_ucirepo 
import matplotlib.pyplot as plt
import random 
# fetch dataset 
iris = fetch_ucirepo(id=53)

# datos como dataframes
data_num = iris.data.features #Caracteristicas 
data_label = iris.data.targets  #Etiquetas

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

marca = ['o', 'v', '*']
color = ['b', 'r', 'g' ]
caract = [0, 1, 3]
total = len(data_num)
for i in range(3):
    ejes = []
    for j in range(3):
        inicio = i * 50
        fin = 50 + 50 * i 
        ejes.append(np.array(data_num.iloc[inicio:fin, caract[j]]))
    ax.scatter(ejes[0], ejes[1], ejes[2], 
               marker=marca[i], color=color[i], linewidths=6)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
    