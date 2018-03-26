import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# constantes
s = [0, 5, 10, 15, 20, 25, 30]
ds = 30
t_plot = [i for i in range(20)]

# velocidade
def vel (ds, dt):
    return ds/dt

# aceleracao
def a (dv, dt):
    return dv/dt

# retorna s(t)
def eq_horaria(s_0, t, vel):
    return t*vel

# recebe uma lista de str; troca virgulas por pontos
def format_to_float(arr):
    return [s.replace(',', '.') for s in arr]

dataset = pd.read_csv('Movimento Uniforme.csv')

dataset_lucas_1 = format_to_float(dataset.iloc[2:5, 4].values)
tempos_lucas_1 = [float(i) for i in dataset_lucas_1]
dt_lucas_1 = np.sum(tempos_lucas_1)
vel_lucas_1 = vel(ds, dt_lucas_1)
print("Vel media - Lucas 1: %s m/s") % (vel_lucas_1)

s_lucas = [eq_horaria(s[0], i, vel_lucas_1) for i in range(20)]
plt.plot(s_lucas, t_plot, color = 'blue')

dataset_lucas_2 = format_to_float(dataset.iloc[6:9, 4].values)
tempos_lucas_2 = [float(i) for i in dataset_lucas_2]
dt_lucas_2 = np.sum(tempos_lucas_2)
vel_lucas_2 = vel(ds, dt_lucas_2)
print("Vel media - Lucas 2: %s m/s") % (vel_lucas_2)

s_lucas = [eq_horaria(s[0], i, vel_lucas_2) for i in range(20)]
plt.plot(s_lucas, t_plot, color = 'red')

vel_lucas_media = np.mean([vel_lucas_1, vel_lucas_2])
print("Vel media - Lucas: %s m/s") % (vel_lucas_media)

s_lucas = [eq_horaria(s[0], i, vel_lucas_media) for i in range(20)]
plt.plot(s_lucas, t_plot, color = 'green')

# plt.scatter(s_lucas, t_plot, color = 'red')
# plt.plot(s_lucas, t_plot, color = 'blue')
plt.title("Exemplo - Lucas")
plt.xlabel("Espaco")
plt.ylabel("Tempo")
plt.show()