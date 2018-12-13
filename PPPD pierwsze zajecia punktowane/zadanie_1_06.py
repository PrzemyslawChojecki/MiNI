"""
winda jest 8-osobowa
na dole stoi n ludzi
na gorze m ludzi

ile kursow musi zrobic winda?
"""

n = int(input("To ile ludzi stoi na dole?\nn: "))
m = int(input("A na gorze?\nm: "))
x = 0

if n<0 or m<0:
    print("Bledne n albo m. :(")
    exit()

if (n//8 <= m//8) and m!=0:
    x+=1

    x+=(((m//8)+int(bool(m%8)))*2)-1
elif n!=0:
    x=((n//8)+int(bool(n%8)))*2-1
else:
    x=0

print(x)