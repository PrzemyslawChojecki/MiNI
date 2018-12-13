"""
W wieżowcu o 21 piętrach (piętra liczymy od 0 do 20) popsuła się winda. Wszyscy zostali zmuszeni do
korzystania ze schodów.
• Pomiędzy każdymi dwoma piętrami jest dokładnie 15 schodków.
• Łazienki znajdują się tylko na piętrach o parzystych numerach.
"""

schd = int(input("Podaj liczbe schodow, ktore pokonales\n"))

if schd < 0 or schd > 300:
    print("Bledne dane")
elif schd%15 == 0:
    print("Jestes na ",int(schd/15) , " pietrze")
else :
    print("Jestes miedzy ",int(schd/15), ", a ",int(schd/15) + 1, " pietrem.")

if schd%30 == 15:
    print("Musisz pokonac 15 schodkow w gore albo w dol do najblizszej toalety.")    
elif schd%30 < 15:
    print("Musisz pokonac ",(schd-int(schd/30)*30), " schodkow w dol do najblizszej toalety.")
else :
    print("Musisz pokonac ",30-(schd-int(schd/30)*30), "schodkow w gore do najblizszej toalety.")