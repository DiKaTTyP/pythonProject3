def Fibonacci(a,b):
    s=len(a)
    start = -1
    f0=0
    f1=1
    f2=1
    while(f2 < s):
        f0= f1
        f1=f2
        f2=f1+f0

    while(f2>1):
        i = min(start+f0,s - 1)
        if a[i] < b:
            f2 = f1
            f1=f0
            f0=f2-f1
            start = i
        elif a[i]> b:
            f2=f0
            f1=f1-f0
            f0=f2-f1
        else:
            return(i+1)
    if (f1) and (a[s-1] == b):
        return(s-1)

    return (None)

a = [12,34,57,89]
print(Fibonacci(a,57))