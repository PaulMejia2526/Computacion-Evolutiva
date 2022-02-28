import string
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import statistics
import random

#xStart = random.randint(-10,5)
#yStart = random.randint(-10,5)
eta = 0.1
d = 0.000001
iter= 10
#x = xStart
#y = yStart
results = []

Function = input('Cual función deseas? Sphere o Rastrigin?: ')

for j in range(iter):
    x = random.randint(-5,5)
    y = random.randint(-5,5)
    if Function == "Rastrigin":
        def f(x, y):
            return 10*2 + x**2 + y**2 - 10*np.cos(2*np.pi*x) - 10*np.cos(2*np.pi*y)
    elif Function =="Sphere":
        def f(x,y):
            return (x+2)**2 + (y+2)**2






    def g(x,y):
        gx = (f(x+0.5*d, y)-f(x-0.5*d, y))/d
        gy = (f(x ,y+0.5*d)-f(x ,y-0.5*d))/d
        return (gx, gy)

    def improve(x, y):
        gx, gy = g(x , y)
        x = x - eta*gx
        y = y - eta*gy
        return (x,y)

    history_x = [x]
    history_y = [y]
    history_f = [f(x,y)]


    for i in range(20):
        x,y = improve(x,y)
        history_x.append(x)
        history_y.append(y)
        history_f.append(f(x,y))
        if i == 19:
            results.append(f(x,y))




    EjeX = np.linspace(-10, 5, 100)
    EjeY = np.linspace(-10, 5, 100)
    EjeX, EjeY = np.meshgrid(EjeX, EjeY)
    EjeZ = f(EjeX, EjeY)
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(EjeX, EjeY, EjeZ,  cmap=cm.coolwarm, alpha=0.3)
    ax.plot(x,y,f(x,y), 'ro')
    plt.show()
    print("Mínimo en el punto X: ", x,"punto Y: ",y,"y punto Z: " ,f(x,y))


print("Con una media: ",statistics.mean(results), "Y una varianza de: ", statistics.variance(results))


