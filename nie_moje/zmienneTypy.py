"""
Lab. 01
Wprowadzenie: zmienne, typy, operacje arytmetyczne,
relacyjne, logiczne, instrukcje warunkowe, formatowanie napisow
"""

x = 1     # integer (int)
y = 1.5   # float
z = True  # bool (False)
s = "kot" # string (str)

print("x = ", x, "i jest typu", type(x)) # funkcja type() zwraca tym obiektu ...
print("y = ", y, "i jest typu", type(y)) # ... podanego jej jako argument
print("z = ", z, "i jest typu", type(z))
print("s = ", s, "i jest typu", type(s))


## operacje arytmetyczne
# +, -, *, /, //, %, **

# dodawanie
print("x + 1 =", x + 1) # wynik jest typu int
print("x + y =", x + y) # wynik jest typu float
print("z + x =", z + x) # wynik jest typu int
print("z + y =", z + y) # wynik jest typu float

# co sie stanie w przypadku napisow?
# print("s + x =", s + x)         # blad!
print("s + str(x) =", s + str(x)) # musimy skorzystac z jawnej konwersji
# funkcje do konwersji jawnej: bool(), int(), str(), float()

# co sie stanie w przypadku mnozenia napisu przez liczbe?
print("s * 5 =", s * 5)      # dla zmiennych typu int mamy powielenie napisu
#print("s * 5.5 =", s * 5.5) # dla zmiennych typu float mamy blad!

# dzielenie calkowite i reszta z dzielenia modulo
print("-11//4 =", -11//4)
print("11//-4 =", 11//-4)

print("-11%4 =", -11%4)
print("11%-4 =", 11%-4)

print("6.3 // 2.2=", 6.3 // 2.2)
print("6.3 % 2.2=", 6.3 % 2.2)

# += -= *= /=

print("x =", x)
x = x + 1  # zwiakszamy wartosc x o 1
print("x =", x)

x += 1     # zwiakszamy wartosc x o 1
print("x =", x)

## operatory porownania
# < > <= >= == !=

print(2 < 3)
print(2.0 == "2.0")
print(3 != 3.0)
print(4.5 >= True)
# w przypadku porownywania napisow mamy porzadek leksykograficzny
print("anna" < "zbigniew")
print("anna" < "abc")
print("anna" < "5")

## operatory logiczne (posortowane rosnaco wzgledem piorytetu)
# or  (lub)
# and (i)
# not (zaprzeczenie)

print("2 < 3 and 3 > 4 :", 2 < 3 and 3 > 4)
print("not 2 < 3 and 3 > 4 :", not 2 < 3 and 3 > 4)
print("not (2 < 3 and 3 > 4) :", not (2 < 3 and 3 > 4))
print("not False or True :", not False or True)
print("not (False or True) :", not (False or True))
print("not 2 < 3 and 3 <= 4 :", not 2 < 3 and 3 <= 4)
print("not 2 < 3 or 3 <= 4 :", not 2 < 3 or 3 <= 4)


## Instrukcje warunkowe

"""
if warunek_logiczny:
    instrukcja 1a
    instrukcja 1b

------------------------------

if warunek_logiczny:
    instrukcja 1a
else:
    instrukcja 2a
    instrukcja 2b

------------------------------

if warunek_logiczny_1:
    instrukcja 1a
    instrukcja 1b
    instrukcja 1c
elif warunek_logiczny2:
    instrukcja 2a
    instrukcja 2b
else:
    instrukcja 3a

"""

## wczytywanie zmiennych + instrukcje sterujace

# wczytujemy wartosc pierwszej zmiennej
zm1 = input("Podaj wartosc pierwszej zmiennej (int): ")
# wczytujemy wartosc drugiej zmiennej
zm2 = input("Podaj wartosc drugiej zmiennej (int): ")

# wynik funkcji input() zawsze jest napisem (str)
# jesli chcemy miec zmienna typu int musimy dokonac jawnego rzutowania
zm1 = int(zm1)
zm2 = int(zm2)

## Przyklad grupa 17.15
if zm1 < zm2:
    print(":-)")
elif zm1 > zm2:
    print(":-(")
else:
    print("xD")

## Przyklad grupa 14.15
"""
if zm1 < zm2:
    print(":-)")
else:
    print(":-(")
"""

## o funkcji print() dwa slowa jeszcze:
print("Ala", "ma", "kotow", 4, ".")
print("Ala", "ma", "kotow", 4, ".", sep = " ")             # to samo co wyzej
print("Ala", "ma", "kotow", 4, ".", end = "\n")            # to samo co wyzej
print("Ala", "ma", "kotow", 4, ".", sep = " ", end = "\n") # to samo co wyzej
# argumenty:
# sep = " " (domyslnie spacja) - oddzielenie poszczegolnych elementow napisu
# end = "\n" (domyslnie znak przejscie do nowej linii \n) - jak konczymy napis

# np. jak zmienimy:
print("Ala", "ma", "kotow", 4, ".", sep="-", end = ":-)")
# to wtedy nastepna informacja wyswietli sie tak:
print("I jestesmy w tej samej linii")

## ladne formatowanie napisow:
print(str.format("pierwszy element to {0} a drugi to {1}, a tu znowu damy pierwszy {0}", 1, 2))
print(str.format("pierwszy napis to {0} a drugi to {1} , a tu znowu damy pierwszy {0}",
                 "a", "b", "c")) # niewykorzystane argumenty sa pomijane

# sposoby formatowania zmiennych typu float
print(str.format("domyslnie wartosc zmiennej to {0:f}", 7.98))
print(str.format("gdy chcemy 2 miejsca po przecinku wtedy mamy {0:0.2f}", 7.98))
print(str.format("gdy chcemy 9 miejsc wypisac to mamy {0:0.9f}", 7.98))
print(str.format("gdy chcemy 20 miejsc wypisac to mamy{0:0.20f}", 7.98)) # 20 miejsc po przecinku

# sposoby formatowania zmiennych typu int
print(str.format("Liczba dni roboczych w tygodniu wynosi {0:d}", 5))

print(str.format("|{0:d}|", 5))
print(str.format("|{0:8d}|", 5))  # zmiana szerokosci (8 znakow)
print(str.format("|{0:08d}|", 5)) # 8 znakow + wypelnienie zerami

# sposoby formatowania zmiennych typu str
print(str.format("Silicon {0:s} (HBO)", "Valley")) # domyslnie

print(str.format("|{0:s}|", "kot"))
print(str.format("|{0:10s}|", "kot")) # zmiana szerokosci (10 znakow)

# wysrodkowanie, przesuniecie

print(str.format("|{0:<10s}|", "A")) # to samo co: print(str.format("|{0:10s}|", "kot"))
print(str.format("|{0:^10s}|", "A"))
print(str.format("|{0:>10s}|", "A"))

# inne przyklady
print(str.format("|{0:010d}|", 5))
print(str.format("|{0:^10d}|", 5))
print(str.format("|{0:<010d}|", 5))


print(str.format("{0} podac {{1}} bez odwolania do elementu {1}.", "Aby", 2))
# podwojne nawiasy klamrowe aby uzyskac w napisie po prostu nawias klamrowy