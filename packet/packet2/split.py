def Split(s):
    l=0
    k=0
    for i in s:
        if i == ' ' or i== "," or i=='.':
            if l == 0:
                k+=1
            else:
                l += 1
        else:
            l = 0
        for n in i:
            if n == ' ' or n == "," or n == '.' or n == '':
                if l == 0:
                    k += 1
                else:
                    l += 1
            else:
                l = 0
    print(k)