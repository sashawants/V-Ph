#'MDCXCIVI','MCMXLIX','MCMXC','LXXVII'  1695,1949,1990,77
r='LXXVII'
    
ra = {'I':1 ,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

a = 0
i=0

while i<(len(r)-1):
    #print(ra[r[i]],ra[r[i+1]])
    if ra[r[i]] >= ra[r[i+1]]:
        a += ra[r[i]]
        i += 1
    else:
        a += ra[r[i+1]] - ra[r[i]]
        i += 2
    #print (a)
if i<len(r):
    a += ra[r[len(r)-1]]
        
print (a)
