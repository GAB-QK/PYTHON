
'''on definti des focntions qui vont être appeleés depuis un autre module'''

def carre(x):
    return x**2
def cube(x):
    return x**3
def positif (x):
    return x>=0

# cette condition est utilisé pour n'executer des instructions en general des tests que si le module est
# executé directement et pas import par un autre module

if __name__ == "__main__":
    print(carre(7))
    print(__name__)
    print(positif(4))


