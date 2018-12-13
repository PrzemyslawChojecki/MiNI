"""
Stworz plik robiacy szachownice wielkosci n
"""

#wczytanie ilosci wierszy
n = int(input("podaj wielkosc szachownicy: "))
if n < 0:
    print("Bledne Dane!")
    exit()

f = open("szachownica.txt", "a") #pliczek do dopisywania

#petelka dla i wierszy
for i in range(n):
    f.write(str(i+1))
    f.write(". ")
    for j in range(n):
        if (j+i)%2 == 0:
            f.write("#")
        else:
            f.write("O")
    f.write("\n")

f.close()


