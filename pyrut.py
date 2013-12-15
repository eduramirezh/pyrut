from itertools import cycle

def verifier(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    result = (-s) % 11
    return result if result != 10 else 'k'

class RutIterator:
    def __init__(self, start=1, end=40000000):
        self.start = start
        self.end = end
        self.isPositive = (self.start < self.end)
        self.current = start

    def __iter__(self):
        return self

    def next(self):
        if (self.current <= self.end):
            prev = self.current
            self.current += 1
            return dict(n=prev, v=verifier(prev))
        else:
            raise StopIteration

def ruts(start = 1, end = 40000000):
    return RutIterator(start, end)

def isValid(rut, verifier_digit):
    return verifier_digit == verifier(rut)
