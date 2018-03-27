import numpy as numpy
import matplotlib.pyplot as plt
import pandas as pd
import sys
#exemplo de execucao: python plotPT.py PhysicsToolBoxData/MUKaique1.csv KaiqueMU KaiqueMUImage
#o programa ira plotar o arquivo MUKaique1.csv, com um grafico de titulo "KaiqueMU"e salvar 
# uma imagem KaiqueMUImage.png
# recebe uma lista de str; troca virgulas por pontos
def format_to_float(arr):
    return [s.replace(',', '.') for s in arr]

#caminho do arquivo csv a ser plotado
#exemplo PhysicsToolBoxData/MUKaique1.csv
str = sys.argv[1]
#titulo do grafico
#exemplo Kaique
title = sys.argv[2]
image = sys.argv[3]

dataset = pd.read_csv(str, delimiter=';')
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
plt.savefig(image + ".png")
#plt.show()