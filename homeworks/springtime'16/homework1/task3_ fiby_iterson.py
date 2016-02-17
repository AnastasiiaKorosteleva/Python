__author__ = 'anastasiiakorosteleva'


class fibonacci_sequence:
    def __init__(self, n):
        self.n = n
        self.cnt = 0

    def __iter__(self):
        self.fibs = [1, 1]
        for f in range(2, self.n):
            self.fibs.append(self.fibs[-1] + self.fibs[-2])

    def __next__(self):
        if self.cnt >= self.n:
            raise StopIteration()
        else:
            a = self.fibs[self.cnt]
            self.cnt += 1
            return a


it = fibonacci_sequence(5)
it.__iter__()

print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

#print(it.__iter__())
# for x in it:
#     print(x)



