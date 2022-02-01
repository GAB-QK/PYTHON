# module Time
import time as T
print(T.time())

# la fonction sleep permet de mettre en pause
#le programme pendant un certain nombre de secondes
print("1")
T.sleep(3)
print("2")

# la fonction time permet de faire une diff de temps de calcul
T1=T.time()
print("blablabla")
T.sleep(4)
T2=T.time()
print("temps de calcul",T2-T1,"seconde")


