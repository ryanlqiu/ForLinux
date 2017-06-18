class Fibs:
    def __init__(self):
        self.a=0
        self.b=1
    def __next__(self):
        self.a,self.b = self.b, self.a + self.b
        return self.b
    def __iter__(self):
        return self


counter = 0
fib=Fibs()
for f in fib:
    counter+=1
    print(f)
    if counter >49:
        break
