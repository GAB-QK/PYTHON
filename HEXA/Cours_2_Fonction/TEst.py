def premier(n):
    verif = False
    for i in range(2,n+1):
        if i == n:
            continue
        elif n%i != 0:
            verif = True
        else:
            verif = False
            break
    return verif

print(premier(7))