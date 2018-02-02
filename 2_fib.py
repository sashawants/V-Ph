N=4*(10**6)
f1=1
f2=2
f=0
s=2
i=2


lst=[1,2]
while i<=N:
    f = f1 + f2
    lst += [f]
    if f%2 == 0:
        s += f
    f1=f2
    f2=f
    i=i+1


s1 = sum([x for x in lst if x%2==0])
ch = sum([x**3 for x in s1])
zn = sum([x**2 for x in s1])
o = ch / (1.0 * zn)

#print (ch)
#print (zn)

print (o)
