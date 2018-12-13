"""
Kalkulator
"""

x = float(input("Podaj x: ")) # wczytujemy pierwszy argument
y: float = float(input("Podaj y: ")) # wczytujemy drugi argument

dzialanie = input("Podaj operacje: ") # wczytujemy dzialanie


if dzialanie == "+":    # dodawanie
    z = x + y
elif dzialanie == "-":  # odejmnowanie
    z = x - y
elif dzialanie == "*":  # mnozenie
    z = x * y
elif dzialanie == "/":  # dzielenie
    if y == 0:  # uwaga: nie mozemy dzielic przez zero
        print("Blad: dzielenie przez 0!")
        exit()
    else:
        z = x / y
elif dzialanie == "%":   # modulo
    z = x % y
elif dzialanie == "//":  # calkowite
    if y == 0:
        print("Blad: dzielenie przez 0!")
        exit()
    else:
        z = x // y
elif dzialanie == "**":
    z = x ** y
else:
    print("Blad: nie podano wlasciwego operatora")
    exit()

# ladnie sformatowanie wypisania wyniku
print(str.format("{0:0.2f} {1:s} {2:0.2f} = {3:0.2f}", x, dzialanie, y, z))
