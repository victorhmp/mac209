import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# CONSTANTES E MAGIC NUMBERS

s = [0, 5, 10, 15, 20, 25, 30]
delta_s = 30
time_plot = [i for i in range(20)]

# FUNCOES - CALCULOS

# velocidade
def vel (ds, dt):
    return ds/dt

# aceleracao
def a (dv, dt):
    return dv/dt

# retorna s(t)
def eq_horaria(s_0, t, vel):
    return t*vel

# FUNCOES AUXILIARES

# recebe uma lista de str; troca virgulas por pontos
def format_to_float(arr):
    return [s.replace(',', '.') for s in arr]

# calcula velocidade media, printa e plota
def calc_vel_and_plot(dataset, coord_x, coord_y, name, plot_color):
    subdataset = format_to_float(dataset.iloc[coord_x, coord_y[0]:coord_y[1]].values)
    timeline = [float(i) for i in subdataset]
    delta_t = np.sum(timeline)
    velocity = vel(delta_s, delta_t)
    print("Vel %s: %s m/s") % (name ,velocity)

    positions_plot = [eq_horaria(s[0], i, velocity) for i in range(20)] # s[0] comes from constants
    plt.plot(positions_plot, time_plot, color = plot_color)

# adiciona informacoes ao plot e salva em um arquivo
def setup_and_save_plot(legend, title, filename, xlabel="Espaco", ylabel="Tempo"):
    plt.legend(legend, loc='upper left')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # plt.show()
    plt.savefig(filename)

# MU

dataset = pd.read_csv('Movimento Uniforme.csv')

calc_vel_and_plot(dataset, 4, [2,5], 'Lucas - Pareado 1', 'blue')
calc_vel_and_plot(dataset, 8, [2,5], 'Lucas - Pareado 2', 'red')
calc_vel_and_plot(dataset, 27, [2,8], 'Lucas - Alternado', 'green')
setup_and_save_plot(['Pareado 1', 'Pareado 2', 'Alternado'],
    "Exemplo - Lucas",
    "MU-Plot-Lucas.png")

# MUV