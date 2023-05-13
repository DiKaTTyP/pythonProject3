def Fib(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in Fib(20):
    print(num)
