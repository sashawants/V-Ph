import math
import cmath

B,C=-(10)**(20),4.0

def rsh(b,c):

    D=b**2-4*c
    #print ('D = ',D)

    if D>=0:
        if b>=0:
            x1=(-b-math.sqrt(D))/2.0
        else:
            x1=(-b+math.sqrt(D))/2.0
        x2=c/x1

    if x1==x2:
        root=x1
    else:
        root=x1,x2

    if D<0:
        x1,x2=(-b+cmath.sqrt(D))/2.0 , (-b-cmath.sqrt(D))/2.0
        #x1 = complex (round (x1.real , 2) , round (x1.imag , 2))
        #x2 = complex (round (x2.real , 2) , round (x2.imag , 2))
        root = x1,x2

    return (root)

print rsh(B,C)
