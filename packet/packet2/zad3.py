def Spisok(s):
    sum=0
    sum4=0
    for i in s:
        sum+=i
        if i%2 ==0:
            sum4+=i
    m = max(s)
    mi = min(s)
    sr = m - mi
    print(f"Список: {s} Сумма: {sum} Сумма четных: {sum4} Максимальное: {m}  Минимальное:{mi} Разница между маскимальным и минимальным: {sr}")
    return(s,sum,sum4,m,mi,sr)
