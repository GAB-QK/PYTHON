
import random
tentative= 0
nombrehasard=random.randint(1,10)
game = True
reponse=0
while reponse != nombrehasard:
    reponse= int(input("Devinez le nombre ?"))
    tentative += 1
    if reponse == nombrehasard :
        print("Trouvé !")
        print("nombre de tentative: ",tentative)
    elif reponse > nombrehasard :
            print("trop grand")
    else :
            print("trop petit")


