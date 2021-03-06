"""
Pierwsze punktowane laby 2018
"""

import math

#wczytanie danych
n = int(input("Podaj liczbe bokow stolu:"))
a = int(input("Podaj dlugosc boku(w cm):"))
h = int(input("Podaj wysokosc stolu(w cm):"))



#sprawdzenie poprawdnosci danych
#Warunek z polecenia, to n < 5 or a < 30 or a > 70 or h < 50 or h > 100, ale Pani Cena powiedziala, ze mozna go oslabic
if n < 5 or a < 30 or a > 70 or h < 50 or h > 100:
    print("1. Niepoprawne dane")
    exit()
else:
    print("1. Poprawne dane")



#Dlugosc promienia opisanego i podwojenie go
R = a / (2 * math.sin((math.pi)/n))
R *= 2

#sprawdzenie, czy blat sie zmiesci
if R > 305:
    print("2. Nie uda sie wyciac takiego blatu.")
    exit()
else:
    print("2. Mozna wyciac taki blat.")



#belka to ilosc nog zrobionych z jednej belki
belka = math.floor(390/h)

#wypisanie ilosci potrzebnych belek
if n%belka == 0:
    print("3. Potrzeba {} belek".format(str(n//belka)))
else:
    print("3. Potrzeba {} belek".format(str((n//belka)+1)))




#znalezienie indeksu najdluzszej przekatnej
k = (n//2)-1

#policzenie dlugosci najdluzszej przekatnej
d = (a*math.sin(((k+1)*math.pi)/n)/math.sin((math.pi)/n))

#Aby blat sie zmiescil wysokosc blatu ma byc mniejsza niz przekatna drzwi
if n%2 == 0:
    h = math.sqrt(d**2-a**2)
else:
    h = math.sqrt(d**2-(a/2)**2)

print(h, "\n", math.sqrt(200**2+80**2))

#porownanie i wypisanie wyniku
if h > (math.sqrt(200**2+80**2)):
    print("4. Blat sie nie zmiesci!")
else:
    print("4. Blat sie zmiesci!")

