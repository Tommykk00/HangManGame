import random
import time
import json

jatkaPelia = 'U'
pelaaPelia = True
kategoria = ""
kayttajaArvauslista = []
kayttajaArvaukset = []

#Alustetaan hedelma ja marja
def hedelma():
    with open("hedelmat.txt") as hedelma_tiedosto:
        hedelmat = hedelma_tiedosto.readline().split()
    random_hedelma = random.choice(hedelmat)
    return random_hedelma
def marja():
    with open("marjat.txt") as marja_tiedosto:
        marjat = marja_tiedosto.readline().split()
    random_marja = random.choice(marjat)
    return random_marja

#Kerrotaan pelaajalle säännöt ja kysytään sana kategoriaa
nimi = input("Syötä nimesi: ")
print("Moi " + nimi.capitalize() + ", pelataan hirsipuuta!")
time.sleep(1)
print("Tehtäväsi on arvata oikea tietokoneen valitsema sana. \nSinulla on rajattu määrä arvauksia. Jos arvaat sanan oikein ennenkuin arvauksesi loppuvat, voitat. \nJos et, häviät.") 
time.sleep(1)
print("Voit arvata vain yhden kirjaimen kerralla, älä unohda painaa ENTER näppäintä valittuasi kirjaimen.")
time.sleep(2)
print("Peli alkakoon!!")
time.sleep(1)

dataa = {
            "pelaaja": {
                        "nimi": nimi
           }
}

file = open("dataa.json", "w")
json.dump(dataa, file, indent = 6)
file.close()

while True:
    #Valitaan sana
    while True:
        if kategoria.upper() == 'H':
            salainenSana = hedelma()
            break
        elif kategoria.upper() == 'M':
            salainenSana = marja()
            break
        else:
            kategoria = input("Valitse haluamasi kategoria: H: Hedelmät / M: Marjat. Paina x ja ENTER poistuaksesi. ")

        if kategoria.upper() == 'X':
            print("Nähdään pian!")
            pelaaPelia = False
            break
    #pelaajalle yrityksiä sanan pituuden verran + 2
    if pelaaPelia:
        salainenSanalista = list(salainenSana)
        yrityksia = (len(salainenSana) + 2)

        #printataan arvattu kirjain
        def printtaaArvattuKirjain():
            print("Sinun salainen sanasi on: " + ''.join(kayttajaArvauslista))

        for n in salainenSanalista:
            kayttajaArvauslista.append('_')
        printtaaArvattuKirjain()

        print("Sallittujen arvausten määrä on: ", yrityksia)

        #Aloitetaan peli
        while True:
            print("Arvaa kirjain: ")
            kirjain = input()

            if kirjain in kayttajaArvaukset:
                print("Sinä arvasit jo tätä kirjainta, koita jotain muuta.")
            else:
                yrityksia -= 1
                kayttajaArvaukset.append(kirjain)
                if kirjain in salainenSanalista:
                    print("Hyvä arvaus!")
                    if yrityksia > 0:
                        print("Sinulla on ", yrityksia, "arvausta jäljellä!")
                    for i in range(len(salainenSanalista)):
                        if kirjain == salainenSanalista[i]:
                            kirjainIndeksi = i
                            kayttajaArvauslista[kirjainIndeksi] = kirjain.upper()
                    printtaaArvattuKirjain()
                else:
                    print("Hups! Yritä uudelleen.")
                    if yrityksia > 0:
                        print("Sinulla on ", yrityksia, "arvausta jäljellä!")
                    printtaaArvattuKirjain()

             #Voitto/häviö logiikka
            joinedLista = ''.join(kayttajaArvauslista)
            if joinedLista.upper() == salainenSana.upper():
                print("Jee! Sinä voitit.")
                break
            elif yrityksia == 0:
                print("Liian monta arvausta. Parempi onni ensi kerralla.")
                print("Salainen sana oli: " + salainenSana.upper())
                break

        #Pelaa uudestaan
        jatkaPelia = input("Haluatko pelata uudestaan? Paina U pelataksesi uudelleen, paina mitä tahansa muuta lopettaaksesi: ")
        if jatkaPelia.upper() == 'U':
            kategoria = input("Valitse haluamasi kategoria: H: Hedelmät / M: Marjat. ")
            kayttajaArvauslista = []
            kayttajaArvaukset = []
            pelaaPelia = True
        else:
            print("Kiitos pelaamisesta, nähdään ensi kerralla!")
            break
    else:
        break
                
                        




















    
