"""
Mamy z piniedzy i km kilometrow do przejechania
placimy 10zl, a potem 2,5zl za kazdy kilometr,
po 20 kilometrach placimy 5zl za kilometr
"""
z  = float(input("Podaj ile masz pieniedzy: "))
km = float(input("Podaj ile masz km do przejechania: "))

if z<0 or km<=0:
    print("Nieprawidlowe dane")
elif z<10:
    print("Nie dasz rady nawet ruszyc :(")
elif z<60:
    print(f"Dasz rade przejechac {(z-10)/2.5} kilometrow.")

    if km > ((z-10)/2.5):
        print("Nie dasz rady przejechac potrzebnego dystansu, musisz sie zaporzyczyc :(")
    else:
        print("Spoko, spoko. Na czilku dasz rade :)")
else:
    print(f"Daszrade przejechac {20+(z-60)/5} kilometrow.")

    if km > (20+(z-60)/5):
        print("Nie daszrady przejechac potrzebnego dystansu, musisz sie zaporzyczyc :(")
    else:
        print("Spoko, spoko. Na czilku dasz rade :)")
