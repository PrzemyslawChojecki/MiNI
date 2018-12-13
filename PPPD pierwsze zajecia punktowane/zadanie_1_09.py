"""
pizza-19.99
cola-6.99
zestaw-25.99
dostawa-5
"""

print("Zawsze jest dobra pora na pice! :D")
p = int(input("Ile picy chcecie?\np = "))
c = int(input("Ile coli chcecie?\nc = "))

if p<0 or c < 0 or (p==0 and c == 0):
    print("Nieprawidlowe dane kurde blaszka!")
    exit()

if p == 0 or c ==0:
    print(f"Nie uzbiera sie z tego zestaw :( Nalezy zaplacic {5+19.99*p+6.99*c} PLN")
else:
    print(f"Uzbiera sie {min(p, c)} zestawow i zaplacicie {min(p, c)*25.99+(p-min(p, c))*19.99+(c-min(p, c))*6.99} PLN")