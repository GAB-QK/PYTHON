a=[]
b={"a":a}
c=2

for i in range(4):
    if i%2==0:
        a.append(i)
    b[i]=str(i)
    if i>c:
        b[i]=0
print(b)
