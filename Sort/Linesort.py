def Linesort(a):
    for i in range(len(a)):
        min = i
        for k in  range(i+1,len(a)):

            if  a[k] < a[min]:
                min = k
        a[min], a[i] = a[i], a[min]
    return a