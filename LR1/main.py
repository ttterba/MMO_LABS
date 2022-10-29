import numpy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from collections import Counter

dt = np.dtype("f8, f8, f8, f8, f8, f8, f8, f8, f8, f8, f8, i4")
data = np.genfromtxt("winequality-red.csv", delimiter=";", dtype=dt)

# Индексы параметров
FIXED_ACIDITY = 0
VOLATILE_ACIDITY = 1
CITRIC_ACID = 2
RESIDUAL_SUGAR = 3
CHLORIDES = 4
FREE_SULFUR_DIOXIDE = 5
TOTAL_SULFUR_DIOXIDE = 6
DENSITY = 7
PH = 8
SULPHATES = 9
ALCOHOL = 10
QUALITY = 11

params_by_quality = [[[] for j in range(12)] for k in range(6)]

for wine in data:
    for i in range(len(wine)):
        params_by_quality[wine[QUALITY] - 3][i].append(wine[i])

titles = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide",
          "total sulfur dioxide", "density", "pH", "sulphates", "alcohol", "quality"]
colors = ['ro', 'g^', 'bs', 'co', 'm^', 'ys']

for par1 in 1,10:
    for par2 in 10,1:
        plt.figure(par1 * 11 + par2)
        for i in 1,4:
            plt.plot(params_by_quality[i][par1], params_by_quality[i][par2], colors[i],
                     label=f'Качество вина {i + 3}')
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
                   ncol=3, fancybox=True, shadow=True)
        plt.xlabel(titles[par1])
        plt.ylabel(titles[par2])

        plt.show()
