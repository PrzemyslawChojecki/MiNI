"""
ile talii jest potrzeba, zeby pograc
w dana ilosc osob w makao
"""

print("Slyszalem, ze chcecie pograc sobie w makao.")
print("Pozwolcie, ze pomoge wam wybrac ile kalii tart potrzebujecie:")

G = int(input("Ile jest graczy: "))
T = int(input("Ile macie talii: "))

kart = 1 + G * 5

print(f"Potrzbujecie {(kart//52)+1} talii")

if T*52 < kart:
    print("\nNie macie wystarczajaco duzo karteczek, zeby pograc :(")
    exit()

print(f"Moze sie do was dolaczyc jeszcze {int((T*52 - kart)/5)} graczy :)")