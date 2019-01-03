import math

def mediana(x):
    if len(x)%2 == 1:
        return x[(len(x)-1)//2]
    else:
        return (x[len(x)//2]+x[len(x)//2-1])/2

def boxplot(x, nazwa):
    x.sort()

    med = mediana(x)

    x_first = [None] * ((len(x)+1)//2)
    x_last = [None] * ((len(x)+1)//2)

    for i in range(len(x_first)):
        x_first[i] = x[i]
    for i in range(len(x_last)):
        x_last[i] = x[(len(x))//2 + i]

    q1 = mediana(x_first)
    q3 = mediana(x_last)
    
    #Ściągawka – rysowanie:
    # inicjowanie rysunku:
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches

    fig = plt.figure()
    ax = fig.add_subplot(111)
    # ustal zakresy na osiach:
    ax.set_xlim([0.0, 3.0]) # zakres wartości na osi OX
    ax.set_ylim([x[0]-(math.fabs(x[0])*0.01), x[len(x)-1]]) # zakres wartości na osi OY
    # przykładowy jasnoszary prostokąt:

    ax.add_patch(patches.Rectangle((1, q1), 1, q3-q1, fill = False))

    y = [1.5] * len(x) 
    plt.plot(y, x, "-k")

    plt.plot([1, 2], [med, med])


    # ax.add_patch(patches.Rectangle(....)) można będziemy wywoływać wielokrotnie
    # plt.plot(x, y, "ko") # dodaj punkty (x[0], y[0]), (x[1], y[1]), ...
    # plt.plot(x, y, "-k") # narysuj łamaną łączącą (x[0], y[0]), (x[1], y[1]), ...
    # k - czarny, r - czerwony, b - niebieski, g - zielony, itp.

    # zapis do PNG po zakończeniu rysowania
    fig.savefig(nazwa, dpi=90)
    

    
boxplot([5,3,6,-34,63,46,36,23], "5.png")