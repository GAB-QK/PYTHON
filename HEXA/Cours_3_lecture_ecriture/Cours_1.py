'''lecture et ecriture dans  dans fichier '''
#ouverture d'un fichier en ecriture
#ecrsament des données deja presente
with open("donnes.txt", "w") as fichier: #w pour write
    fichier.write("salam rouya")
#ouvertured'un fichier en eciture a la suite
#si il y a deja  du texte dnas le fichier
with open("donnes.txt", "a") as fichier: #a pour append
    fichier.write(" ça va ou quoi?")
    fichier.write("\nyo le sang de la veine")

with open("ecriture.txt", "w") as fichier:
    fichier.write("1\n2")
    fichier.close()

with open("ecriture.txt", "r") as fichier:
    contenu=fichier.read()
print(contenu)

Lignes =contenu.splitlines()
print(Lignes)
numero=[int(n) for n  in Lignes]
print(numero)
''' permet de stocker dans la liste en convrtissanrt en int/ permet de additioner etc et faire du traitement
de donné sur les valeurs/ renvoie une erreuer si il y a une strg non converetible exemple "hello" '''






