import time
class Iteration():
    def __init__(self, n, k):
        self.n = n
        self.k = k

    def __iter__(self):
        self.num = self.n
        return self

    def __next__(self):
        if self.k > self.num:
            value = self.num
            if value % 2 == 0:
                self.num += 2
                return value

            else:
                self.num+=1
                value = self.num
                return value
        else:
            raise StopIteration


for num in Iteration(0, 100000):
    print(num)
