import random
import time
from Sort import Linesort
from Sort import Bubblesort
from Sort import *
from Search import Binsearch
from Search import LineSearch
from Search import Fibonacci

a = [random.randint(1,10) for i in range (10)]
b = [random.randint(1,100) for i in range (100)]
c = [random.randint(1,1000) for i in range (1000)]
d = [random.randint(1,10000) for i in range (10000)]
k=a[:]
"""b=int(input())
t1=time.time()*1000
print( time.time()*1000 - t1)
Binsearch(a,b)
t2=time.time()*1000
LineSearch(a,b)
print( time.time()*1000- t2)
print(Fibonacci(a,b))"""

Fastsort(d,0,9999)
print(d)