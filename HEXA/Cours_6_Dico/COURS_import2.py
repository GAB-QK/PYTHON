
import COURS_import as CI #permet de raccourcir avec le as

print(CI.cube(2))
print(CI.carre(2))

''' si on veut encore raccourcir on peeut specifier quelle fonction importer'''

from COURS_import import positif
print(positif(-4))

#raccourcis ultime
from COURS_import import * # importe toutes les fonctions
print(carre(5))

