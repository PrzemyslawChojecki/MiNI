"""
Wczytujemy date i sprawdzamy, jaka to pora roku i dzien tygodnia
i podajemy dokladny wiek w latach, miesiacach i dniach

Podajemy roznice medzy 2 datami
"""

ru = int(input("Podaj w jakim roku sie urodziles: "))
mu = int(input("Podaj w jakim miesiacu sie urodziles: "))
du = int(input("Podaj w jakim dniu miesiaca sie urodziles: "))

r = int(input("Podaj aktualny rok: "))
m = int(input("Podaj aktualny miesiac: "))
d = int(input("Podaj aktualny dzien miesiaca: "))

#poprawdnosc roku, miesiaca i nie za maly dzien i nie za duzy dzien dla 31
if ru>r or ru<=1900 or r<=1900 or mu<1 or m<1 or mu>12 or m>12 or du<0 or d<0 or du>31 or d>31:
    print("Podales bledne dane! #poprawdnosc roku, miesiaca i nie za maly dzien i nie za duzy dzien dla 31")
    exit()

#urodzinowa data po aktualnej
if ru == r and (mu > m or (mu == m and du > d)):
    print("Podales bledne dane! #urodzinowa data po aktualnej")
    exit()

#za duzy dzien dla lutego dla urodzinowej daty
if ((ru%4 == 0 and ru%100 != 0) or ru%400 == 0) and mu == 2 and du > 29:
    print("Podales bledne dane! #za duzy dzien dla lutego przestepnego dla urodzinowej daty")
    exit()
elif not ((ru%4 == 0 and ru%100 != 0) or ru%400 == 0) and mu == 2 and du > 28:
    print("Podales bledne dane! #za duzy dzien dla lutego NIEprzestepnegoo dla urodzinowej daty")
    exit()

#za duzy dzien dla lutego dla aktuanej daty
if ((r%4 == 0 and r%100 != 0) or r%400 == 0) and m == 2 and d > 29:
    print("Podales bledne dane! #za duzy dzien dla lutego przestepnego dla aktuanej daty")
    exit()
elif not ((r%4 == 0 and r%100 != 0) or r%400 == 0) and m == 2 and d > 28:
    print("Podales bledne dane! #za duzy dzien dla lutego Nieprzestepnego dla aktuanej daty")
    exit()

#za duzy dzien dla 30-dniowych miesiecy dla urodzinowych
if (mu == 4 or mu == 6 or mu == 9 or mu == 11) and du > 30:
    print("Podales bledne dane! #za duzy dzien dla 30-dniowych miesiecy dla urodzinowych")
    exit()

#za duzy dzien dla 30-dniowych miesiecy dla aktualnych
if (m == 4 or m == 6 or m == 9 or m == 11) and d > 30:
    print("Podales bledne dane! #za duzy dzien dla 30-dniowych miesiecy dla aktualnych")
    exit()

PRu = "jesien"
PR = "jesien"

#przypisanie pory roku dla urodzin
if mu < 3 or (mu == 3 and du < 21) or (mu == 12 and du > 21):
    PRu = "zima"
elif mu < 6 or (mu == 6 and du < 22):
    PRu = "wiosna"
elif mu < 9 or (mu == 9 and du < 23):
    PRu = "lato"

#przypisanie pory roku dla dzis
if m < 3 or (m == 3 and d < 21) or (m == 12 and d > 21):
    PR = "zima"
elif m < 6 or (m == 6 and d < 22):
    PR = "wiosna"
elif m < 9 or (m == 9 and d < 23):
    PR = "lato"

#wypisanie pory roku dla urodzin i dzis
print(f"Urodziles sie w: {PRu}\nA dzis jest: {PR}")

#poprawka roku dla urodzinowych
if mu < 3:
    zu = ru - 1
    cu = 0
else:
    zu = ru
    cu = 2

#poprawka roku dla aktualnych
if m < 3:
    z = r - 1
    c = 0
else:
    z = r
    c = 2

#kodowanie dnia tygodnia
wu = (((23*mu)//9)+du+4+ru+(zu//4)+(zu//100)+(zu//400)-cu)%7
w = (((23*m)//9)+d+4+r+(z//4)+(z//100)+(z//400)-c)%7

#Zamiana wu z int na string
if wu == 0:
    wu = "wtorek"
elif wu == 1:
    wu = "sroda"
elif wu == 2:
    wu = "czwartek"
elif wu == 3:
    wu = "piatek"
elif wu == 4:
    wu = "sobota"
elif wu == 5:
    wu = "niedziela"
else :
    wu = "poniedzialek"

#Zamiana w z int na string
if w == 0:
    w = "wtorek"
elif w == 1:
    w = "sroda"
elif w == 2:
    w = "czwartek"
elif w == 3:
    w = "piatek"
elif w == 4:
    w = "sobota"
elif w == 5:
    w = "niedziela"
else :
    w = "poniedzialek"

#wypisanie dni tygodnia
print(f"\nDzien tygodnia urodzenia: {wu}\nDzien tygodnia dzis: {w}")

#Poprawka dla dnia miesiaca mniejszego niz dzien urodzenia
if d < du:
    if (m == 5 or m == 7 or m == 10 or m == 12):
        d += 30
    elif (m == 3) and ((r%4 == 0 and r%100 != 0) or r%400 == 0):
        d += 29
    elif m == 3:
        d += 28
    else:
        d += 31
    m -= 1

#Poprawka dla miesiaca mniejszego niz miesiac urodzenia
if m < mu:
    m += 12
    r -= 1

#wypisanie roznicy
print(f"\nUrodziles sie {r-ru} lat, {m-mu} miesiecy i {d-du} dni temu :)")