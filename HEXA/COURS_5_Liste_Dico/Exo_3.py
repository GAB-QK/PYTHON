'''
afficher des reluts des test de perf des algo de tri avec matplotlib

'''
tailles = [100, 200, 500, 1000, 2000, 5000, 10000, 20000]
# copier coller de la sortie du script de perf de tri
sort=[2.9087066650390625e-05, 4.1961669921875e-05, 0.00011491775512695312, 0.0002429485321044922, 0.00047016143798828125, 0.0014488697052001953, 0.0032460689544677734, 0.005702018737792969]
selection=[0.00022912025451660156, 0.0011909008026123047, 0.003596067428588867, 0.013032913208007812, 0.04882502555847168, 0.35045504570007324, 1.184964895248413, 4.624263048171997]
insertion=[0.0006818771362304688, 0.0025789737701416016, 0.017480134963989258, 0.06457924842834473, 0.2878439426422119, 1.8347787857055664, 7.091181993484497, 28.594368934631348]

'''
afficher des reluts des test de perf des algo de tri avec matplotlib

'''



plt.plot(tailles,insertion,"r--",
         label="insertion",
         linewidth=5)
plt.plot(tailles,selection,"bx-",
         label="Selection",
         linewidth=5)
plt.plot(tailles,sort,"ko-",
         label="Sort",
         linewidth=5)


plt.xlabel("taille de la liste")
plt.ylabel("temps (s)")
plt.legend()

plt.show()


