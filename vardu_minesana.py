import random

#funkcija, kas izvēlas vārdu no vārdu saraksta
def izvēlēties_vārdu():
   vārdi = ['grāmata', 'saule', 'programmēšana', 'dators', 'zirgs', 'nakts', 'tiesnesis', 'maize', 'dzīvoklis', 'bibliotēka']
    return random.choice(vārdi)

#funkcija, kas attēlo vardu, kurā minētie burti ir atklati, bet visi parejie ir aizvietoti ar '_'
def parādīt_vārdu(vārds, minētie_burti):
    parādījums = ''
    for burts in vārds:
        if burts in minētie_burti:
            parādījums += burts
        else:
            parādījums += '_'
    return parādījums

#funkcija, kas realizē vārda minēšanas spēli
def minesana():
    turpināt_spēli = True

    while turpināt_spēli:
        vārds = izvēlēties_vārdu()
        minētie_burti = []
        mēģinājumi = 6

        print("Laipni lūdzam vārdu minēšanas spēlē!")
        print("Mēģiniet uzminēt vārdu.")
        print(parādīt_vārdu(vārds, minētie_burti))

        while True:
            minējums = input("Miniet burtu: ").lower()

            if minējums in minētie_burti:
                print("Jūs jau minējāt šo burtu!")
            elif minējums in vārds:
                minētie_burti.append(minējums)
                print("Jūs uzminējāt!")
                print(parādīt_vārdu(vārds, minētie_burti))
            else:
                mēģinājumi -= 1
                print("Nepareizi! Jums palika {} mēģinājumi.".format(mēģinājumi))
                print(parādīt_vārdu(vārds, minētie_burti))
                if mēģinājumi == 0:
                    print("Atvainojiet, jums beidzās mēģinājumi. Vārds bija '{}'.".format(vārds))
                    break

            if all(burts in minētie_burti for burts in vārds):
                print("Apsveicam, jūs uzminējāt vārdu '{}'!".format(vārds))
                break

        atbilde = input("Vai vēlaties turpināt spēli? (jā/nē): ").lower()
        if atbilde != 'jā':
            turpināt_spēli = False

    print("Paldies par spēli!")

if __name__ == "__main__":
    minesana()
