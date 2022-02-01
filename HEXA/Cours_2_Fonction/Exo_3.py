
def premier(n):
    BOO = False
    for i in range(1, n+1):
        if  i==n :
            continue
        if i==1:
            continue
        elif n%i != 0:
            BOO=True
        else:
            BOO=False
            break
    return BOO

def L_premier(n):
    result=[]
    for i in range(n+1):
        if premier(i):
            result.append(i)
    return result
print (L_premier(100))