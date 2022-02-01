'''Exercice
en utilisant une boucle while
demander de rentrer exactement 6 mots
afficher le mot "terminer" une fois que c'est fait
'''

continuer = True
count = 0

while continuer == True and count<6:
    reponse = (input("Mots ?"))
    try:
        int(reponse)
    except :
        continuer = False
        continue
    count= count+1

print("terminer")