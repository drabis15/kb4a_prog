import random


def herni_smycka(ucet):
    sazka = int(input("Kolik chceš vsadit? "))
    if sazka>ucet:
        print("Tolik nemáš")
    return




def hra(sazka,vysledek,zustatek):
    vysledek = ["orel" ,"panna"]
    random.choice(vysledek)
    if random.choice == vyber:
        zustatek+=(sazka*2)
    else:
        zustatek-=sazka
        return zustatek


       
    
        



ucet=int(input("Kolik chceš dát na účet? "))

vyber = str(input("Vyber [panna] nebo [orel]?"))
znovu = int(input("chceš pokračovat? 1/2: "))
if znovu ==2:
    print("Konec hry")
hra(sazka,vyber,ucet)

