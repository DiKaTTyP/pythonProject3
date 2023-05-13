def Qad(n):
    a= 1
    b=0
    for _ in range(n):
        b=str(b)
        if int(b[len(str(b))-1]) == 4 and int(b) % 6 == 0:
            yield b
        b=a*a
        a+=1

for num in Qad(100):
    print(num)