import math

def histogram(t, k, count=5):
    """
    t-lista danych
    k-ilosc przedzialow rownej dlugosci
    """
    w = [None] * (k+1) #w tej tablicy przechowuje granice przedzialow

    w[0] = min(t)
    w[k] = max(t) * 1.001 #stala podana w zadaniu nie odpowiada przykladowy

    for i in range(1, k):                   #dla kazdej wartosci miedzy najwiekrza, a najmniejsza
        w[i] = w[0] + i * ((w[k] - w[0])/k) #wpisz jej wartosc z ciagu arytmetycznego
    
    ile_wartosci = [0] * k      #w tej tablicy przechowuje ilosc wartosci z taliczy t wystepujacych w odpowiadajacym przedziale
    for i in range(k):                          #dla kazdego przedzialu
        for j in range(len(t)):                 #dla kazdej liczby w tablicy
            if t[j] >= w[i] and t[j] < w[i+1]:  #jesli wartosc liczby z tablicy jest w przedziale
                ile_wartosci[i] += 1            #zwieksz licznik jej wystapien
    
    najwiecej = max(ile_wartosci)   #ilosc liczb w najpopularniejszym przedziale

    krok = najwiecej//count    #co tyle wartosci bede zaznaczal na wykresie
    dlugosc = 50//(count+1)     #tyle bedzie zajnowac jedna przedzialka, zeby tablela sie zmiescila
    koniec_dla_rysunku = 0

    print(" "*20 + "0", end="")
    for i in range(krok, najwiecej, krok):                   #drukuje najpierw spacje, dlategu musze zaczac od drugiego
        print(" "*(dlugosc+1-len(str(i))) + f"{i}", end ="") #wyrownuje w zaleznosci od dlugosci liczby i
    print("\n" + " "*20 + "|", end="")
    for i in range(krok, najwiecej, krok):
        print("-"*dlugosc + "|", end ="")
        koniec_dla_rysunku += (dlugosc+1)       #jak daleko moze siegac pasek reprezentujacy ilosc plikow

    print("")
    
    for i in range(k):
        print("[ ", end = "")
        if w[i] < 0: print(str.format("{0:.03f}", w[i]), end="") #dla ujemnej liczby potrzebuje o jedna spacje mniej niz dla dodatniej liczby
        else: print(str.format(" {0:.3f}", w[i]), end="")       
        print(", ", end = "")
        if w[i+1] < 0: print(str.format("{0:.03f}", w[i+1]), end="")
        else: print(str.format(" {0:.03f}", w[i+1]), end="")
        print(" ) :", end = "")


        for j in range((ile_wartosci[i]*koniec_dla_rysunku)//najwiecej):  #stosunek wartosci w ktorej aktualnie jestesmy do najwiekrzej, pomnozony przez dostepne miejsce
            print("|", end = "")

        print("")




inp = open("dane.txt", "r")
n = int(inp.readline())

t = [None] * n     #w tej tablicy bede pszechowywal dane z tablicy
for i in range(n):
    t[i] = float(inp.readline())    #wpasani danych do funkcji

histogram(t, 13, 4)    #wywolanie funkcji na danuch z tablicy



