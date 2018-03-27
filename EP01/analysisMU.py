import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('MU.csv')

names = ['Lucas', 'Ricardo', 'Kaique']

# CONSTANTES E MAGIC NUMBERS

s = [0, 5, 10, 15, 20, 25, 30]
delta_s = 30
time_plot = [i for i in range(20)]

# FUNCOES - CALCULOS

# velocidade
def vel (ds, dt):
    return ds/dt

# retorna s(t), em MU
def eq_horaria(s_0, t, vel):
    return t*vel

# FUNCOES AUXILIARES

# recebe uma lista de str; troca virgulas por pontos
def format_to_float(arr):
    return [s.replace(',', '.') for s in arr]

# calcula velocidade media, printa e plota dados teóricos (previsão)
def calc_vel_and_plot(dataset, coord_x, coord_y, name, plot_color):
    subdataset = format_to_float(dataset.iloc[coord_x, coord_y[0]:coord_y[1]].values)
    timeline = [float(i) for i in subdataset]
    delta_t = np.sum(timeline)
    velocity = vel(delta_s, delta_t)
    print(("Vel %s: %s m/s") % (name ,velocity))

    Y = [10, 20, 30]
    X = dataset.iloc[6, 2:5].values
    X = format_to_float(X)
    for index, value in enumerate(X):
        if (index == 0):
            continue
        else:
            X[index] = X[index-1] + X[index]

    print(X)

    # plt.scatter(X, Y)

    positions_plot = [eq_horaria(s[0], i, velocity) for i in range(20)] # s[0] comes from constants
    plt.plot(time_plot, positions_plot, color = plot_color)

# adiciona informacoes ao plot e salva em um arquivo
def setup_and_save_plot(legend, title, filename, xlabel="Tempo", ylabel="Espaço"):
    plt.legend(legend, loc='upper left')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # plt.show()
    plt.savefig(filename)
    plt.clf()

for index,name in enumerate(names):
    calc_vel_and_plot(dataset, (4 + index*8), [2, 5], '{} - Pareado 1'.format(name), 'blue')
    calc_vel_and_plot(dataset, (8 + index*8), [2, 5], '{} - Pareado 2'.format(name), 'red')
    calc_vel_and_plot(dataset, (27 + index*2), [2, 8], '{} - Alternado'.format(name), 'green')
    setup_and_save_plot(['Pareado 1', 'Pareado 2', 'Alternado'],
                        "{} - Teórico".format(name),
                        "MU-Plot-{}.png".format(name))
