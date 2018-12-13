import random

def srednia(x):
    suma = 0
    for i in range(len(x)):
        suma += x[i]
    return suma/len(x)

def regresja(x, y):
    if len(x) != len(y):
        raise Exception("tablice x i y sa roznej dlugosci!")
    
    sumx = 0
    sumy = 0
    sumxy = 0
    sumx2 = 0

    for i in range(len(x)):
        sumx += x[i]
        sumy += y[i]
        sumxy += x[i]*y[i]
        sumx2 += (x[i])**2
    
    b = (sumxy - (sumy*sumx)/len(x))/(sumx2 - (sumx ** 2)/len(x))
    
    return srednia(y) - b*srednia(x), b

def E(a, b, x, y):
    suma = 0
    for i in range(len(x)):
        suma += ((a + b*x[i] - y[i]) ** 2)

    return suma
    
def rozklad_liniowy(n, d=10, d2=None):
    if d2 == None: d2 = -d
    x = [random.uniform(d2, d) for i in range(n)]
    return x

def rozklad_normalny(a, b, n, d=10, d2=-10):
    y = [a + b*x[i] + random.normalvariate(0,1) for i in range(n)]
    return y

alpha0 = -0.50
beta0 = 0.17
n = 5

x = rozklad_liniowy(n)
y = rozklad_normalny(alpha0, beta0, n)

regresja1 = regresja(x, y)


alpha1 = regresja1[0] 
beta1 = regresja1[1] 

print(f"E ({alpha0}, {beta0}, x, y) = {E(alpha0, beta0, x, y)}")
print(f"E ({alpha1}, {beta1}, x, y) = {E(alpha1, beta1, x, y)}")

import matplotlib.pyplot as plt
# wykres rozproszenia:
plt.scatter(x, y)
# rysowanie odcinka [xmin, xmax], [ymin, ymax]:
plt.plot([-10, 10], [alpha0+beta0*(-10), alpha0+beta0*10], color="red")
# rysowanie dla mojej funkcji [xmin, xmax], [ymin, ymax]:
plt.plot([-10, 10], [alpha1+beta1*(-10), alpha1+beta1*10], color="green")
# zapis do pliku PNG:
plt.savefig("zadanie_3_0.png")



