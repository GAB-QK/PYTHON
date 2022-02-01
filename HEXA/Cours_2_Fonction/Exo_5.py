'''

def TOP50 (L):
    L.pop()
    L.pop(0)
    return L

print(TOP50([1,2,3,4]))
'''

def TOP40 (A):
    return A[1:-1]

print(TOP40([1,2,3,4]))

