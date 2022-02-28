# Computacion-Evolutiva - Gradiente descendente con diferencias finitas
# Práctica 1
### Paul Eduardo Mejia Rosales - A00354759

Programen el algoritmo de gradiente descendente con diferencias finitas para optimizar las funciones de

---

**Sphere:**

f = (x+2).^2 + (y+2).^2

<p align="center"><img src="https://github.com/PaulMejia2526/Computacion-Evolutiva/blob/main/Captura%20de%20Pantalla%202022-02-28%20a%20la(s)%2013.12.32.png?raw=true" alt="sphere image"/></p>

---

**Rastrigin:**

f = 10*2 + x.^2 + y.^2 - 10*cos(2*pi*x) - 10*cos(2*pi*y)


<p align="center"><img src="https://github.com/PaulMejia2526/Computacion-Evolutiva/blob/main/Captura%20de%20Pantalla%202022-02-28%20a%20la(s)%2013.14.19.png?raw=true"></p>

---

Escriban un reporte de práctica con las siguientes secciones:
1. __Una breve descripción del algoritmo (incluyan ecuaciones y su código del algoritmo de GD, mencionen el lenguaje de programación en el que lo desarrollaron).__

El lenguaje de programación usado es Python:

- Se inicia con una posición random dentro del área a graficar y con un ciclo if para elegir entre la función Sphere o Rastrigin:

```python
for j in range(iter):
    x = random.randint(-5,5)
    y = random.randint(-5,5)
    if Function == "Rastrigin":
        def f(x, y):
            return 10*2 + x**2 + y**2 - 10*np.cos(2*np.pi*x) - 10*np.cos(2*np.pi*y)
    elif Function =="Sphere":
        def f(x,y):
            return (x+2)**2 + (y+2)**2
```
-Enseguida se definen las funciones para evaluar con diferencias finitas y tambien se escribe el gradiente descendente:

```python
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
    )
```
-Una vez cumplidas las 10 ejecuciones se muestran los resultados, media y varianza:

```python
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
```


2. Reporte de resultados, evaluaciones óptimas obtenidas en cada función en 10 ejecuciones, varianza de sus resultados, valor medio obtenido

**Sphere:**

![Sphere](https://github.com/PaulMejia2526/Computacion-Evolutiva/blob/main/Captura%20de%20Pantalla%202022-02-28%20a%20la(s)%2013.16.36.png?raw=true)

![Mean&Var](https://github.com/PaulMejia2526/Computacion-Evolutiva/blob/main/Captura%20de%20Pantalla%202022-02-28%20a%20la(s)%2013.48.14.png?raw=true)



**Rastrigin:**

![rastrigin](https://github.com/PaulMejia2526/Computacion-Evolutiva/blob/main/Captura%20de%20Pantalla%202022-02-28%20a%20la(s)%2013.18.42.png?raw=true)

![Mean&Var](https://github.com/PaulMejia2526/Computacion-Evolutiva/blob/main/Captura%20de%20Pantalla%202022-02-28%20a%20la(s)%2013.49.03.png?raw=true)



3. **Contesten las siguientes preguntas:**

    - **¿Para qué se estima el gradiente de una función en este algoritmo?**
    - Nos permite optimizar una función al encontrar los mínimos por medio de iteraciones y aproximaciones que son baratas computacionalmente, dependiendo de la función se pueden encontrar mínimos globales (como en el caso de la función objetivo Sphere) o mínimos locales (como en el caso de la función de Rastrigin).

    - **¿Por qué tiene un desempeño tan bueno en la función Sphere pero no en Rastrigin?**
    - Porque la función Sphere tiene un sólo fondo, es decir, que sólo tiene un mínimo local que a su vez sería un mínimo global. Para la función de Rastrigin es una historia difente porque tiene infinididad de mínimos locales, lo cual hace que no siempre encuentre el punto más bajo en la función.

    - **¿Cuál es la complejidad asintótica de este algoritmo (usa O(f(x)) para definir la complejidad de la función objetivo)?**
    - O(n)
