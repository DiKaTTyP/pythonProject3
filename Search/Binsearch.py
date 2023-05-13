def Binsearch(a,b):
    mid = len(a)//2
    low = 0
    high = len(a)-1
    while a[mid] != b and low <= high:
        if b > a[mid]:
            low = mid+1
        else:
            high = mid-1
        mid = (low+high)//2

    if low > high:
        print('В данном списке нет такого числа')
    else:
        print(f' Индекс искомого числа равен: {mid}')
