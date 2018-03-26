import numpy as numpy
import matplotlib.pyplot as plt
import pandas as pd

# constantes
s = [0, 5, 10, 15, 20, 25, 30]
t_plot = [i for i in range(20)]

# recebe uma lista de str; troca virgulas por pontos
def format_to_float(arr):
    return [s.replace(',', '.') for s in arr]

str = "kaique2"
title = "MU: Kaique 2"

dataset = pd.read_csv('PhysicsToolBoxData/'+str+'.csv', delimiter=';')
subdataset_time = format_to_float(dataset.iloc[0:, 0].values)
subdataset_ax = format_to_float(dataset.iloc[0:, 1].values)
subdataset_ay = format_to_float(dataset.iloc[0:, 2].values)
subdataset_az = format_to_float(dataset.iloc[0:, 3].values)
subdataset_at = format_to_float(dataset.iloc[0:, 4].values)

time = [float(i) for i in subdataset_time]
ax = [float(i) for i in subdataset_ax]
ay = [float(i) for i in subdataset_ay]
az = [float(i) for i in subdataset_az]
at = [float(i) for i in subdataset_at]

plt.plot(time, ax, color = 'red')
plt.plot(time, ay, color = 'blue')
plt.plot(time, az, color = 'yellow')
plt.plot(time, at, color = 'green')

plt.title("Acelerômetro - " + title)
plt.xlabel("Tempo")
plt.ylabel("Aceleração")
plt.savefig(str + ".png")
#plt.show()