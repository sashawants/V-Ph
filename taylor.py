import math
import cmath

B,C=0.0,0.0

if (b!=0)and(c!=0):
    M=-4*C/(B**2)

def bol(a):
    p=1
    a=math.fabs(a)
    while a>10:
        a=a/10
        p=p+1
    return p
R=math.fabs(bol(B)-bol(C))

def row(x,n,m):
    ch=1
    f=1
    i=1
    s=0
    while i<=n:
        ch=ch*(m-i+1)*x
        #print 'ch(',i,')=',ch
        f=f*i
        #print 'f(',i,')=',f
        s=s+(ch/f)
        i=i+1
        #print 's(',i,')=',s
    return s

def rsh(b,c):
    
    if (b==0)and(c==0):
        root=0,0
    else:

        D=b**2-4*c
        #print ('D = ',D)

        if D>=0:
            if math.fabs(R)<=8:
                x1,x2 = (-b+math.sqrt(D))/2.0 , (-b-math.sqrt(D))/2.0
            else: 
                print ('CHECK B')
                S=row(M,R/2,0.5)       
                x1=(B*S)/2.0
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

print (rsh(B,C))

#print bol(B,C)
#print 'row=',row(M,R,0.5)
#print 'xd=',(C/B+(C**2)/(B**3))/B
