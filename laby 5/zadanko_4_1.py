import numpy
from PIL import Image
import copy

def print_m(t, d = None, f = None):
    """
    Funkcja dostaje macierz t
    Funkcja wydrukuje macierz na terminal, lub do pliku
        podanego jako 3 argument funkcji
    Jesli podamy funkcji liczbe jako 2 argument,
         wydrukuje maksymalnie taka ilosc znakow w kazdej komurce
    Funkcja dostosowuje dlugosci wartosci w macierzy
    """
    if d != None:
        for i in range(len(t)):
            for j in range(len(t[0])):
                t[i][j] = (int(t[i][j] * 10**d)/10**d)
    if type(t) != type([ [0, 0], [0, 0] ]):
        print("It's not a matrix!\nIt is:")
        print(t)
        return

    length = [0] * len(t[0])
    for j in range(len(t[0])):
        for i in range(len(t)):
            if len(str(t[i][j])) > length[j]: length[j] = len(str(t[i][j]))

    if f == None:
        for i in range(len(t)):
            for j in range(len(t[0])):
                print(t[i][j], end=" ")
                print(" " * (length[j] - len(str(t[i][j]))), end = "")
            print("")

    else:
        with open(f, "a") as out:
            for i in range(len(t)):
                for j in range(len(t[0])):
                    print(" " * (length[j] - len(str(t[i][i]))), end = "")
                    print(t[i][j], end=" ", file = out)
                print("", file = out)


def make_m(m, n = None, w = None):
    """
    Funkcja zwraca macierz o m kolumnach i n wierszach.
    Jesli pominiemy 2 wspolrzedna, tworzy macierz kwadratowa.
    Macierz jest Wypelniona 3. argumentem, domyslnie None
    """
    if n == None: n = m

    return [ [w] * n for i in range(m) ]

def sub_m(A, B):
    """
    Returns a matrix C that for every i, j: C[i][j] = A[i][j] - B[i][j]
    If matrixes are unsubstractable, returns None
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None
    C = make_m(len(A), len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] - B[i][j]
    return C


def png_read(filepath):
    img = Image.open(filepath)
    assert len(img.size)==2 # skala szarosci, nie RGB
    return (numpy.array(img)/255).reshape(img.size[1], img.size[0]).tolist()

def png_write(img, filepath):
    img = Image.fromarray((numpy.array(img)*255).astype(numpy.int8), 'L')
    img.save(filepath)

def png_brighter(B, b = 0.5):
    A = copy.deepcopy(B)
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] += b
            if A[i][j] >= 1: A[i][j] = 1
    png_write(A, f"brighter_{b}.png")

def png_negative(B):
    A = copy.deepcopy(B)
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = 1-A[i][j]
    png_write(A, "negative.png")

def png_convolution(Ao, B, k, n):
    A = copy.deepcopy(Ao)
    
    C = [ [0] * len(A[0]) for i in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A[0])):
            for u in range(-k, k):
                for v in range(-k, k):
                    if i+u >= len(A) or j+v >= len(A[0]) or u+k+1 >= len(B) or v+k+1 >= len(B[0]): C[i][j] += 0
                    elif i+u < 0 or j+v < 0 or u+k+1 < 0 or v+k+1 < 0: C[i][j] += 0
                    else: C[i][j] += A[i+u][j+v] * B[u+k+1][v+k+1]


    png_write(C, f"convoulted{n}.png")
    return C

A = png_read("skimage_astronaut.png")



png_brighter(A, 0.4)

png_negative(A)

k = 1

B = [ [-1] * (2*k + 1) for i in range(2*k + 1)]

B[0][0] = 0
B[2][0] = 0
B[2][2] = 0
B[0][2] = 0
B[1][1] = 5
print_m(B)
C = png_convolution(A, B, 1, 0)

Diff = sub_m(A, C)

png_write(Diff, "output.png")

"""
B = [ [1/9] * (2*k + 1) for i in range(2*k + 1)]
print_m(B)
png_convolution(A, B, 1, 1)
"""


