'''
Dictionnaires
collection  de valeurs identifiées par des clés
'''

contact={"Nom":"Lepage","prénom":"thibaut","Age":120,"Département":75}

print(contact)
print(contact["Nom"])

'''on peut ajouter ou modifier des elements '''

contact["Age"]=80
print(contact["Age"])
contact["Numero"]="0626183190"
print(contact)

'''Iteration'''
for i in contact:
    print(i)
print("")

for key,value in contact.items():      # permet d'iterer sur les paires de valeurs
    print("clé:",key,",valeur :",value)




