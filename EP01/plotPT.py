import numpy as numpy
import matplotlib.pyplot as plt
import pandas as pd

# recebe uma lista de str; troca virgulas por pontos
def format_to_float(arr):
    return [s.replace(',', '.') for s in arr]

#nome do arquivo de entrada e nome do arquivo de saida
str = " nome "
#titulo do grafico
title = "  "

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

plt.title("Acelerometro - " + title)
plt.xlabel("Tempo")
plt.ylabel("Aceleracao")
plt.savefig(str + ".png")
#plt.show()