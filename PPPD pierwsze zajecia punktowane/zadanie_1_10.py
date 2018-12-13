"""
c = 8zl/l
s = 8l/100km
p = 30zl
"""

c = float(input("Podaj cene 1 litra paliwa na twojej stacji: "))
s = float(input("Spalanie twojego samochodzika na 100km: "))
p = int(input("Ila masz hajsu: "))
k = int(input("Ile km chcesz nim przejechac: "))

if c<0 or s>50 or s<3 or p<0 or k<0:
    print("Bledne dane :(")
    exit()


mozeszJechac = p*(1/c)*(1/s)*100
koszt1Km = c*s/100

print(f"Mozesz w takim razie przejechac {mozeszJechac} km")
print(f"Przejechanie 1 km kosztuje cie {koszt1Km} PLN")

if mozeszJechac >= k:
    print("Mozesz jechac!")
else:
    print(f"Niestety brakuje ci {(k-mozeszJechac)*koszt1Km} PLN.")