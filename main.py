import math

class LongNum:
    def __init__(self, n, mas=[], sign='+'):
        self.deg = n
        self.mas = mas if mas else [0 for _ in range(n)]
        self.sign = sign

    def __str__(self):
        s = '' if self.sign == '+' else '-'
        return s + ''.join(map(str, self.mas))

    def simplify(self):
        while self.mas and self.mas[0] == 0 and self.deg > 1:
            self.mas.pop(0)
            self.deg -= 1
        return self

class Polinoms:
    def __init__(self, n, mas=[]):
        self.dim = n
        self.mas = mas if mas else [0] * (self.dim + 1)

    def __add__(self, other):
        mx = max(self.dim, other.dim)
        c = Polinoms(mx)
        for i in range(mx):
            c.mas[i] = self.mas[i] + other.mas[i]
        return c
    
    def __str__(self):
        return ' + '.join(f'{coef}x^{i}' for i, coef in enumerate(self.mas) if coef)

class Rational:
    def __init__(self, m, n=1):
        self.m = m
        self.n = n

    def __str__(self):
        return f'{self.m}/{self.n}' if self.n != 1 else str(self.m)

class Matrix:
    def __init__(self, m, n, mas=[]):
        self.m = m
        self.n = n
        self.mas = mas if mas else [[0 for _ in range(n)] for _ in range(m)]

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.mas)

class Vector:
    def __init__(self, n):
        self.dim = n
        self.mas = [0] * n

    def __add__(self, other):
        return Vector(self.dim, [self.mas[i] + other.mas[i] for i in range(self.dim)])
    
    def __mul__(self, other):
        return sum(self.mas[i] * other.mas[i] for i in range(self.dim))

    def __str__(self):
        return str(self.mas)


def main():
    # Проверка LongNum
    arr = [0, 0, 0, 1, 2]
    num = LongNum(len(arr), arr, '+')
    print("LongNum:", num.simplify())

    # Проверка Polinoms
    x = Polinoms(3, [2, 2, 3, 5])
    y = Polinoms(3, [4, 5, 6, 8])
    print("Polinom X:", x)
    print("Polinom Y:", y)
    print("X + Y:", x + y)

    # Проверка Rational
    frac = Rational(3, 4)
    print("Rational:", frac)

    # Проверка Matrix
    A = Matrix(2, 2, [[1, 2], [3, 4]])
    print("Matrix A:")
    print(A)

    # Проверка Vector
    v1 = Vector(3)
    v1.mas = [1, 2, 3]
    v2 = Vector(3)
    v2.mas = [4, 5, 6]
    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("Vector 1 * Vector 2:", v1 * v2)

if __name__ == "__main__":
    main()
