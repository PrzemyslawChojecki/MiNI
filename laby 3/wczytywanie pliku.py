"""
Wczytywanie pliczkow i zapisywanie ich
"""

#podstawy napisowania
"""
f = open("Plik_testowy.txt", tryb)

f.close()

gdzie tryby:
"r" - do odczytu
"w" - do zapisu
"a" - dopisanie nowych rzeczy do pliku
"""

#wczytanie z pliku
"""
f = open("test.txt", "r")

zawartosc = f.read()

print(zawartosc)

f.close()
"""


#wszystkie wiersze
"""
f = open("test.txt", "r")

for line in f:
    print(str.strip(line))

f.close()
"""

#tylko drugi wiersz
"""
f = open("test.txt", "r")

f.readline()
print(f.readline(), end = " ")
"""

# with
"""
with open("test.txt", "r") as f:
    while True:
        line = f.readline()
        print(line, end = "")
        if line == "": break
#Nie trzeba zamykac pliku, bo with sam to robi
"""

# Zapisywanie do pliku
"""
f = open("nowy.txt", "w")

f.write("Pliczek szybki :D xDDD")

f.close()
"""

# Dopisywanie do pliku
"""
f = open("nowy.txt", "a")

f.write("Najnowsza sprawa Pliczek szybszy  :D xDDD\nLOL\nPojebana akcja Xd")

f.close()
"""

# Formatowanie napisow
"""
f = open("dopisywanie.txt", "a")

print(str.format("{0:12.02f}",  1.2345), file = f)
print(str.format("{0:^12.02f}", 1.2345), file = f)
print(str.format("{0:<12.02f}", 1.2345), file = f)

f.close()
"""




