
class personne :
    def __init__(self,nom,date_naissance):
        self.nom=nom
        self.date_naissance = date_naissance
        self.argent=0

    def presente_toi(self):
        print("je m'apelle",self.nom,"je suis née le",self.date_naissance)

    def majorite(self):
        annee=int(self.date_naissance[-4:])
        maj=annee+18
        return self.date_naissance[:-4]+str(maj)

    def thune (self):
        print("jai",self.argent,"€")







personne1 = personne("gabriel","05-12-1999")
personne2 = personne("BOB le bricoleur","14/07/1886")

personne1.argent+=10000

print(personne1.presente_toi())
print(personne1.majorite())
print(personne1.thune())


class Assure (personne) :
    def __init__(self,nom,date_naissance,numero_secu):
        self.nom=nom
        self.date_naissance=date_naissance
        self.numereo_secu=numero_secu
        self.argent=0
    def rembourse(self,montant):
        self.argent+= montant

personne3= Assure("TOto","42/13/2000","100137512010130")
personne3.presente_toi()
print(personne3.numereo_secu)
personne3.rembourse(5000)
personne3.thune()

'''
"crée deux instance de la  classe personne " \
"en utilisant le nom de la  classe comme  fonction" \
"c'estle constructur qui est réellement applé" \
"avec la nouvelle instance comme parametre  self "
'''







