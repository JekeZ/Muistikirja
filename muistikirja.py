import time
aika = time.strftime("%X %x")
while True:
    print ("(1) Lue muistikirjaa \n(2) Lisää merkintä \n(3) Tyhjennä muistikirja \n(4) Lopeta")
    syote = int(input("Mitä haluat tehdä?: "))
    if(syote == 1):
        f = open("muistikirja.txt", "r")
        print(f.read())
        f.close
        continue

    elif(syote == 2):
        merkinta = input("Kirjoita uusi merkintä : ")
        f = open("muistikirja.txt", "a")
        f.write(merkinta + ":::" + aika + "\n")
        f.close
        continue

    elif(syote == 3):
        f = open("muistikirja.txt", "w").close()
        print("Muistio tyhjennetty.")
        continue

    elif(syote == 4):
        print("Lopetetaan.")
        break
    else:
        print("Tuntematon valinta.")
        break