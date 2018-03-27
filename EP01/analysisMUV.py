import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('MUV.csv')

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
    positions_plot = [eq_horariaMUV(s[0], i, aceleration) for i in range(20)]
    plt.plot(time_plot, positions_plot, color=plot_color)


calc_vel(dataset, 4, [2, 5], 'Victor - Pareado 1', 'blue')


def setup_and_save_plot(title, filename, xlabel="Tempo", ylabel="Espaço"):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # plt.show()
    plt.savefig(filename)


setup_and_save_plot('VictorAcelerado', "MUV-Plot-Victor.png")
