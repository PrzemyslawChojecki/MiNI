"""

print("\nPozwol, ze rozwiaze dla ciebie eklad 2 rownan:\nax + by = c\ndx + ey = f\nPotrzebuje tylko wspolcznynnikow. Moglbys mi je podac?")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))


y = (f*a - d*c)/(-d*b + a*e)
x = (c - b*y)/a

print("X to: ",x)
print("Y to: ",y)

print("\nBo:\n{0} * {1} + {2} * {3} = {4}".format(a, x, b, y, c))
print("{0} * {1} + {2} * {3} = {4}".format(d, x, e, y, f))

"""

print("\nPozwol, ze rozwiaze dla ciebie eklad 2 rownan:\nax + by = c\ndx + ey = f\nPotrzebuje tylko wspolcznynnikow. Moglbys mi je podac?")

a = float(input("a: ")) #podawanie
b = float(input("b: ")) #wartosci
c = float(input("c: ")) #wspolczynnika
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))

Wg = a*e - b*d  #liczenie
Wx = c*e - b*f  #wartosci
Wy = a*f - c*d  #wyznacznikow

y = (f*a - d*c)/(-d*b + a*e)
x = (c - b*y)/a

print("\nX to: ",x)
print("Y to: ",y, "\n")

#print("\n", Wg, Wx, Wy, sep="\n")

if a == 0 and b == 0 and d == 0 and e == 0 and c!=f:
    print("\nxDDZiomus, podany przez ciebie uklad jest sprzeczny")
   #powinno byc jeszcze oddzielny przypadek dla c==f,
   #bo dla niego te wzory tez nie powinny dzialac, ale
   #wynik jes poprawdny dlatego moge zostawic dalszy kod:

if Wg == 0:
    if Wx == 0 and Wy == 0:
        print("\nZiomus, podany przez ciebie uklad jest nieoznaczony")
    else:
        print("\nZiomus, podany przez ciebie uklad jest sprzeczny")
else:
    print("Prosta sprawa ziomus:\nx = {0}\ny = {1}".format(Wx/Wg, Wy/Wg))