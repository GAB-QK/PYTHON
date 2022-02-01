'''Afficher la longueur
du mot
Initialiser les points à 10
Demander au joueur de rentrer une lettre
si la lettre a déjà été demandée ou si elle n'est pas dans le mot à deviner, on perd un point
Sinon, on indique où se trouve cette lettre dans le mot
Tant que le joueur a des points, redemander une lettre'''
import random as r

points = 10
mot_blanc = ""
Bonne_L = ""          #création d'une liste pour stocker  les lettres déjà trouvé
                # construction du mot blanc avec la fonction for.. in, va permettre d'inserer le nombre de lettre du mot à deviner



with open("liste_francais.txt", "r") as fichier:
    contenu=fichier.read().splitlines()
    #print(contenu)
    Mot=contenu

    tirage = Mot[r.randint(0, len(Mot) - 1)]
    solution =tirage
    #print(solution)
#import de mot random dans fichier txt

    for a in solution:
        mot_blanc += "_ "  #création et init du mot blanc

    while points > 0 :
        #print(len(solution))
        print("tu dois deviner ce mot :", mot_blanc)    #affichage du  mot blanc au joueur
        Test = input("donne une lettre ma petite gueule ?!")     #variable test qui demande les lettre
        if Test in solution:              # test de la réponse dans variable solution avec for .. in
            Bonne_L = Bonne_L + Test           #  ajouts à la liste les lettres trouvées
            print("Trouvé !")
        else :
            points -= 1       # perte de points si réponse mauvaise
            print("non c'est pas ça chakal!\n","il te reste",points,"tentatives")

        mot_blanc = ""  #  remet à  0 la vraiable pour mettre à jour
        for lettre in solution:     #pour chaque lettre de la solution
            if lettre in Bonne_L:     #   on verifie si elle est dans lettres trouvées
                mot_blanc += lettre + " "     # du coup on l'ajoute à l'affichage mot_blanc
            else:
                mot_blanc += "_ "        # sinon rajouter BLANC
        if "_ " not in mot_blanc :
            print("tu as gagné mon loulou")
            print("c'est super ça")
            break

if "_ " in mot_blanc :
    print("t'es nul c'etait: ", solution)











