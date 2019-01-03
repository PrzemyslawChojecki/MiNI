import random

def stworz_plansze(n, liczba, maxiter):
    #sprawdzenie poprawnosci danych
    assert liczba > 0
    assert maxiter > 0
    assert type(liczba) == type(7)
    assert type(maxiter) == type(7)
    assert n > 0
    assert liczba <= n**2

    pola_odkryte = [ [False] * n for i in range(n) ]
    plansza = [ [-1] * n for i in range(n) ]
    """
    -1 -1 -1 -1 ...
    -1 -1 -1 -1 ...
    -1 -1 -1 -1 ...
    -1 -1 -1 -1 ...
    .  .  .  .
    .  .  .  .
    .  .  .  .
    """

    #inicjowanie min
    for i in range(liczba):
        for j in range(maxiter):
            x = random.randint(0, n-1)
            y = random.randint(0, n-1)
            if plansza[x][y] != 9:
                plansza[x][y] = 9
                break
    
    #funkcja wewnetrzna zliczajaca ilosc min dla srodkowych
    def count_miny(x, y):
        miny = 0
        if plansza[x+1][y] == 9: miny += 1
        if plansza[x+1][y+1] == 9: miny += 1
        if plansza[x][y+1] == 9: miny += 1
        if plansza[x-1][y+1] == 9: miny += 1
        if plansza[x-1][y] == 9: miny += 1
        if plansza[x-1][y-1] == 9: miny += 1
        if plansza[x][y-1] == 9: miny += 1
        if plansza[x+1][y-1] == 9: miny += 1

        return miny

    #liczenie w srodku
    for x in range(1, n-1):
        for y in range(1, n-1):
            if plansza[x][y] == -1:  #gdy niema miny
                plansza[x][y] = count_miny(x, y)
    
    #liczenie na scianach
    for x in range(1, n-1):
        if plansza[x][0] == -1:
            miny = 0
            if plansza[x-1][0] == 9: miny += 1
            if plansza[x-1][1] == 9: miny += 1
            if plansza[x][1] == 9: miny += 1
            if plansza[x+1][1] == 9: miny += 1
            if plansza[x+1][0] == 9: miny += 1
            plansza[x][0] = miny
        if plansza[x][n-1] == -1:
            miny = 0
            if plansza[x-1][n-1] == 9: miny += 1
            if plansza[x-1][n-2] == 9: miny += 1
            if plansza[x][n-2] == 9: miny += 1
            if plansza[x+1][n-2] == 9: miny += 1
            if plansza[x+1][n-1] == 9: miny += 1
            plansza[x][n-1] = miny
    for y in range(1, n-1):
        if plansza[0][y] == -1:
            miny = 0
            if plansza[0][y-1] == 9: miny += 1
            if plansza[1][y-1] == 9: miny += 1
            if plansza[1][y] == 9: miny += 1
            if plansza[1][y+1] == 9: miny += 1
            if plansza[0][y+1] == 9: miny += 1
            plansza[0][y] = miny
        if plansza[n-1][y] == -1:
            miny = 0
            if plansza[n-1][y-1] == 9: miny += 1
            if plansza[n-2][y-1] == 9: miny += 1
            if plansza[n-2][y] == 9: miny += 1
            if plansza[n-2][y+1] == 9: miny += 1
            if plansza[n-1][y+1] == 9: miny += 1
            plansza[n-1][y] = miny

    #liczenie w rogach
    if plansza[0][0] == -1:
        miny = 0
        if plansza[0][1] == 9: miny += 1
        if plansza[1][1] == 9: miny += 1
        if plansza[1][0] == 9: miny += 1
        plansza[0][0] = miny
    if plansza[n-1][0] == -1:
        miny = 0
        if plansza[n-2][0] == 9: miny += 1
        if plansza[n-2][1] == 9: miny += 1
        if plansza[n-1][1] == 9: miny += 1
        plansza[n-1][0] = miny
    if plansza[n-1][n-1] == -1:
        miny = 0
        if plansza[n-1][n-2] == 9: miny += 1
        if plansza[n-2][n-2] == 9: miny += 1
        if plansza[n-2][n-1] == 9: miny += 1
        plansza[n-1][n-1] = miny
    if plansza[0][n-1] == -1:
        miny = 0
        if plansza[0][n-2] == 9: miny += 1
        if plansza[1][n-2] == 9: miny += 1
        if plansza[1][n-1] == 9: miny += 1
        plansza[0][n-1] = miny

    return plansza, pola_odkryte

def ile_min(plansza):
    n = len(plansza)
    ilosc_min = 0
    for x in range(n):                              #dla kazdego wiersza
        for y in range(n):                          #dla kazdej kolumny
            if plansza[x][y] == 9: ilosc_min += 1   #jesli jest mina, zwieksz licznik
    
    return ilosc_min #zwraca ilosc min

def odkryj_pole(x, y, plansza, pola_odkryte):
    if pola_odkryte[x][y] == True:              #gdy gracz probuje 2 raz grac na to samo pole
        raise Exception("Odkryto juz to pole")
    pola_odkryte[x][y] = True
    if plansza[x][y] == 9:      #gdy trafil na mine
        return True
    return False

def wypisz(plansza, pola_odkryte):
    n = len(plansza)
    
    # wypisanie numerow kolumn planszy
    for k in range(n):
        if k == 0: print(str.format("{0:^3s}|", " "), end="")
        print(str.format("{0:^3s}", str(k)), end="")
    print("\n"+"-"*(n*3+4))
    
    # wypisanie stanu planszy:
    for i in range(n):     # petla po wierszach
        for j in range(n): # petla po kolumnach
            # wypisywanie numerow wierszy
            if j == 0: print(str.format("{0:^3s}|", str(i)), end=" ") 
            
            if pola_odkryte[i][j] == False: print(" ", end="  ") # jesli pole nie jest odkryte wypisz ' '
            else:
                if plansza[i][j] == 9: print("X", end = "  ") # jesli pole jest odkryte i niezawiera miny wypisz jego wartosc 
                else: print(plansza[i][j], end = "  ") # jesli pole jest odkryte i zawiera mine wypisz 'x'
        print("") #przejscie do nastepnej linii miedzy wierszami
            
def gra(n=10, liczba=10, maxiter=25):
    plansza = stworz_plansze(n, liczba, maxiter)    #wczytanie planszy i pola jako tablicy do jednej zmiennej
    pola = plansza[1]            #przepisanie pola do zmiennej pola
    plansza = plansza[0]         #przepisanie planszy do zmiennej plansza
    ilosc_nie_min = n**2 - ile_min(plansza)         #tyle jest pol do odkrycia przez urzydkownika
    
    #gra sie toczy dopuki nie wypelnimy planszy 
    k = 0
    while k < ilosc_nie_min:
        wypisz(plansza, pola)
        x = input("Podaj wspolrzedne x i y oddzielone spacjami: ")
        x = x.split(" ")    #wczytanie wspolrzednych do tablicy
        y = int(x[1])       #przerobienie wspolrzednych z str na int
        x = int(x[0])

        czy_trafil_na_mine = odkryj_pole(x, y, plansza, pola)   #funkcja odkryj_pole zwraca True gdy gracz trafil na mine
        
        #przypadek konca gry
        if czy_trafil_na_mine:
            print("\nTo byla mina :(\nPrzegrales/as, koniec gry.")
            wypisz(plansza, pola)
            print("Koniec")
            return
        
        k += 1
    
    #gracz odkryl wszystkie pola
    wypisz(plansza, pola)
    print("Zwyciestwo! :D")
    return

gra()

