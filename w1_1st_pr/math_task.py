import sys


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

def formula(a,b,c):
    x1 = (-b+(b**2 - 4*a*c)**0.5)/2*a
    x2 = (-b-(b**2 - 4*a*c)**0.5)/2*a
    return int(x1), int(x2)

print((formula(a,b,c)),sep=" ")
