import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('MU.csv')

names = ['Lucas', 'Ricardo', 'Kaique']

# CONSTANTES E MAGIC NUMBERS

s = [0, 5, 10, 15, 20, 25, 30]
s_pareado = [10, 20, 30]
s_alternado = [5, 10, 15, 20, 25, 30]
delta_s = 30
time_plot = [i for i in range(20)]

# FUNCOES - CALCULOS

# velocidade
def vel (ds, dt):
    return ds/dt

# retorna s(t), em MU
def eq_horaria(s_0, t, vel):
    return t*vel

def eq_horario_tempo(s_0, s, vel):
    return (s-s_0)/vel

# FUNCOES AUXILIARES

# recebe uma lista de str; troca virgulas por pontos
def format_to_float(arr):
    return [s.replace(',', '.') for s in arr]

# printa s(t) para cada t tal que 0s <= t <= 19s
def print_s_t(positions_plot):
    print("[", positions_plot[0], end="")
    for i in range (1,20):
        print (", ", positions_plot[i], end="")
    print("]")

# calcula velocidade media, printa e plota dados teoricos (previsao)
def calc_vel_and_plot(dataset, coord_x, coord_y, name, plot_color):
    subdataset = format_to_float(dataset.iloc[coord_x, coord_y[0]:coord_y[1]].values)
    timeline = [float(i) for i in subdataset]
    delta_t = np.sum(timeline)
    velocity = vel(delta_s, delta_t)
    print(("Vel %s: %s m/s") % (name ,velocity))

    Y = s_pareado
    Y_2 = s_alternado
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

    positions_plot = [eq_horaria(s[0], i, velocity) for i in range(20)] # s[0] comes from constants   
    plt.plot(time_plot, positions_plot, color = plot_color)

    # #CALCULO E PLOT DE ERRO (tempo)
    # tempo_esperado = []
    # erro = []
    # for i in range(len(X)):
    #     if(len(X) == 3):
    #         t = eq_horario_tempo(s[0], Y[i], velocity)
    #     else:
    #         t = eq_horario_tempo(s[0], Y_2[i], velocity)
    #     tempo_esperado.append(t)
    # for i in range(len(tempo_esperado)):
    #     erro.append(tempo_esperado[i] - X[i])
    # if(len(X) == 3):
    #     plt.plot(Y, erro, color = plot_color)
    # else:
    #     plt.plot(Y_2, erro, color = plot_color)
    # setup_and_save_plot(['Erro'],
    #                     "{} - Erro MU: Experimental x Teorico".format(name),
    #                     "Erro-MU-Plot-{}.png".format(name),
    #                     xlabel='Espaco (m)', ylabel='Tempo(s)')

    # print_s_t(positions_plot) #para printar s(t) apenas descomentar

# adiciona informacoes ao plot e salva em um arquivo
def setup_and_save_plot(legend, title, filename, xlabel="Tempo (s)", ylabel="Espaco (m)"):
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
    setup_and_save_plot(['Valores experimentais - Pareado 1','Pareado 1', 'Valores experimentais - Pareado 2', 'Pareado 2', 
                        'Valores experimentais - Alternado', 'Alternado'],
                        "{} - MU: Experimental x Teorico".format(name),
                        "MU-Plot-{}.png".format(name))
