"""
Mamy budynek o wymiarach a, b, h
i rolki papieru zakrywajace 2.548 kosztujace 1.37zl

jesli kupimy ponad 400 rolek trza doplacic 100zl
"""

a = float(input("Podaj dlugosc budynku: "))
b = float(input("Podaj szerokosc budynku: "))
h = float(input("Podaj wysokosc budynku: "))

if a<=0 or b<=0 or h<=0:
    print("Tosz to bez sensu!!!")
    exit()

r = (2*h*(a+b))/2.548

print(f"Potrzeba {r} rolek.")

if r<400:
    print(f"I trzeba za nie zaplacic {r*1.37} zlociszy")
else:
    print(f"I trzeba za nie zaplacic {(r*1.37)+100} zlociszy")
