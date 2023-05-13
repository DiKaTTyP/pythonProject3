def Partition(a,st,ed):
    spi = st
    for i in range(st+1,ed+1):
        if  a[i] <= a[st]:
            spi +=1
            a[i],a[spi] = a[spi], a[i]
    a[spi], a[st] = a[st],a[spi]
    return spi

def Fastsortrec(a,st,ed):
    if st >= ed:
        return
    spi = Partition(a,st,ed)
    Fastsortrec(a,st,spi - 1)
    Fastsortrec(a,spi +1,ed)

def Fastsort(a,st=0,ed = None):
    if ed is None:
        ed = len(a) - 1

    return Fastsortrec(a,st,ed)

import random
