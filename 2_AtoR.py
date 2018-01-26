#'MDCXCIVI':1695(MDCXCV),'MCMXLIX':1949,'MCMXC':1990,'LXXVII':77, 'XM':990(CMXC)  
a = 1695

from math import fabs

ar = {0:'',1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',}

r=''

d1 = 1
d2 = 5
while a>0:
    x = a % 10
    i = x % 5
    j = x // 5
    if i==4:
        r = ar[d1] + ar[10*j*d1] + ar[fabs(j-1)*d2] + r
    else:
        r = ar[j*d2] + i * ar[d1] + r
    d1 *= 10
    d2 *= 10
    a //= 10

print (r)
