class Iteration():
    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        value = self.num
        self.num +=1
        return value



for num in Iteration():
    print(num)