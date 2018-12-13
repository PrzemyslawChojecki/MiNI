"""
Przyblizamy pi z pol pi/4
"""

import random
import math

n = int(input("Podaj dokladnosc przyblizenia: "))

ilosc = 0

#losowanie floutow
for i in range(n):
    if (random.uniform(-1, 1))**2 + (random.uniform(-1, 1))**2 < 1:
        ilosc += 1


#liczenie pi
pi = (ilosc/n)*4

print(pi)

print(pi-math.pi)