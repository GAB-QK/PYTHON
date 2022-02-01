
'''Exo
ecrire une fonction qui prend en parametre
deux longueurs A et B

et qui renvoi la longueur de l'hypotenuse
du triangle rectangle A et B '''
import math
import math as M
def hypotanus (a,b):
    return M.sqrt(a**2+b**2)

print(hypotanus(3,4))
print(M.hypot(3,4))

