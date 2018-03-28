import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('MUV.csv')

names = ['Victor', 'Yurick', 'Kaique']

cheat = [0]

# CONSTANTES E MAGIC NUMBERS

s = [0, 5, 10, 15, 20, 25, 30]
delta_s = 30
time_plot = [i for i in range(20)]

# FUNCOES - CALCULOS

# velocidade
def vel(ds, dt):
    return ds/dt

# aceleracao
def a(dv, dt):
    return dv/dt

# retorna s(t), em MU
def eq_horaria(s_0, t, vel):
    return t*vel

# retorna s(t), em MUV
def eq_horariaMUV(s_0, t, acel):
    return (eq_horaria(s_0, t, acel*t) + ((t ^ 2)/2) * acel)


def format_to_float(arr):
    return np.array([s.replace(',', '.') for s in arr])


def calc_vel(dataset, coord_x, coord_y, name, plot_color):
    subdataset = format_to_float(
        dataset.iloc[coord_x, coord_y[0]:coord_y[1]].values)
    timeline = [float(i) for i in subdataset]
    delta_t = np.sum(timeline)
    velocity = vel(delta_s, delta_t)
    aceleration = a(velocity, delta_t)
    print(("Aceleration %s: %s m/s^2") % (name, aceleration))

    cheat[0] = aceleration

    Y = [10, 20, 30]
    Y_2 = [5, 10, 15, 20, 25, 30]
    X = timeline
    for index, value in enumerate(X):
        if (index == 0):
            continue
        else:
            X[index] = X[index-1] + value
    try:
        plt.plot(X, Y, '.', color=plot_color)
    except ValueError:
        plt.plot(X, Y_2, '.', color=plot_color)

    positions_plot = [eq_horariaMUV(s[0], i, aceleration) for i in range(20)]
    plt.plot(time_plot, positions_plot, color=plot_color)


def setup_and_save_plot(legend, title, filename, xlabel="Tempo (s)", ylabel="Espaço (m)"):
    plt.legend(legend, loc='upper left')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # plt.show()
    plt.savefig(filename)
    plt.clf()

def plot_vel(title, xlabel="Tempo (s)", ylabel="Velocidade (m/s)"):
    velocity_plot = [cheat[0] * t for t in range(20)]
    plt.plot(time_plot, velocity_plot, color='purple')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

for index,name in enumerate(names):
    calc_vel(dataset, (4 + index*8),
                      [2, 5], '{} - Pareado 1'.format(name), 'blue')
    calc_vel(dataset, (8 + index*8),
                      [2, 5], '{} - Pareado 2'.format(name), 'red')
    calc_vel(dataset, (27 + index*2),
                      [2, 8], '{} - Alternado'.format(name), 'green')
    setup_and_save_plot(['Valores experimentais - Pareado 1', 'Pareado 1', 'Valores experimentais - Pareado 2', 'Pareado 2',
                         'Valores experimentais - Alternado', 'Alternado'],
                        "{} - MUV: Experimental x Teorico".format(name),
                        "MUV-Plot-{}.png".format(name))
    plot_vel("{} - Velocidade X Tempo".format(name))
    
