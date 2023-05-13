import time
from GenerationSimple import GenerationSimple
def Dekorator(F):
    def wrapper(*args,**kwargs,):
        c = time.time() * 1000
        print(f"Вызов функции {F.__name__} с аргументами {args} ")
        result = F(*args,**kwargs)
        t = ((time.time() * 1000) - c)
        print(f"Функция {F.__name__} вернула значение {result} за {t} милисекунд")
        return result
    return wrapper

"""@Dekorator
def add(a,b):
    result = GenerationSimple(a,b)

    return result"""

def DekoratorTime(F):
    def wrapper(*args,**kwargs,):
        c = time.time() * 1000
        print(f"Вызов функции {F.__name__} с аргументами {args} ")
        result = F(*args,**kwargs)
        t = ((time.time() * 1000) - c)
        print(f"Функция {F.__name__} вернула значение {result} за {t} милисекунд")
        return result
    return wrapper

@DekoratorTime
def GenerationS(a,b):
    for num in GenerationSimple(a,b):
        result = num

    return result

result = GenerationS(1,10000)
