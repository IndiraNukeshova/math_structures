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

class Matrix:
    def __init__(self, matrix=None):
        self.matrix = matrix if matrix else []
        

    def sum_matrix(self, a, b, m, n):
        c = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                c[i][j] = a[i][j] + b[i][j]
        return c
    
    def sum_matrix_with_check(self, a, b):
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            print("Error size!")
            return None
        c = [[a[j][i] + b[j][i] for i in range(len(a[0]))] for j in range(len(a))]
        return c
    
    def transpos(self, matrix):
        tmp = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                tmp[j][i] = matrix[i][j]
        return tmp
    
    def mul_matrix(self, a, b, m, n, l):
        c = [[0 for j in range(l)] for i in range(m)]
        for i in range(m):
            for j in range(l):
                for k in range(n):
                    c[i][j] += a[i][k] * b[k][j]
        return c
    
    def add_line(self, a, x):
        a.append(x)
        return a
    
    def add_col(self, a, x):
        for i in range(len(a)):
            a[i].append(x[i])
        return a
    
    def give_minor(self, a, n, k, l):    
        B = [[0 for i in range(n-1)] for j in range(n-1)]
        for i in range(k):
            for j in range(l):
                B[i][j] = a[i][j]
            for j in range(l+1, n):
                B[i][j-1] = a[i][j]
        for i in range(k+1, n):
            for j in range(l):
                B[i-1][j] = a[i][j]
            for j in range(l+1, n):
                B[i-1][j-1] = a[i][j]
        return B
    
    def det_lapl(self, a, n):
        if n == 1:
            return a[0][0]
        det = 0
        for j in range(n):
            det += (-1) ** j * self.det_lapl(self.give_minor(a, n, 0, j), n-1) * a[0][j]
        return det
    
    def laplass(self, A, n):
        if n == 1:
            return A[0][0]
        det = 0
        for j in range(n):
            det += (-1)**j * self.laplass(self.give_minor(A, n, 0, j), n-1) * A[0][j]
        return det
    
    def swap_line(self, a, n, i, j):
        for k in range(n):
            a[i][k], a[j][k] = a[j][k], a[i][k]
        return a
    
    def gauss_up(self, a, m, n):  # верхняя трапец
        size1 = m-1 if m <= n else n
        for i in range(size1):  # num of work, diag el
            for j in range(i+1, m):  # under el
                if a[i][i] != 0:  # Prevent division by zero
                    q = a[j][i] / a[i][i]
                    for k in range(i, n):  # sub line
                        a[j][k] -= q * a[i][k]
        return a
    
    def gauss(self, a, m, n):
        size1 = m - 1 if m <= n else n
        for i in range(size1):  # diag
            for j in range(i+1, m):  # underdiag
                if a[i][i] != 0:  # Prevent division by zero
                    q = a[j][i] / a[i][i]
                    for k in range(i, n):  # j - iq
                        a[j][k] -= a[i][k] * q
        return a
    
    def gauss_down(self, a, m, n):  # нижняя трапец
        size1 = m-1 if m <= n else n
        for i in range(size1, 0, -1):  # num of work, diag el
            for j in range(i):  # under el
                if a[i][i] != 0:  # Prevent division by zero
                    q = a[j][i] / a[i][i]
                    for k in range(i+1):  # sub line
                        a[j][k] -= q * a[i][k]
        return a
    
    def gauss_modified_up(self, a, m, n):
        size1 = m-1 if m <= n else n
        for i in range(size1):  # num of work, diag el
            mx = [0, 0]
            for j in range(i, m):  # Fixed from n to m for row selection
                if abs(a[j][i]) > mx[0]:
                    mx = [abs(a[j][i]), j]
     
            self.swap_line(a, n, i, mx[1])
            for j in range(i+1, m):  # under el
                if a[i][i] != 0:  # Added check to prevent division by zero
                    q = a[j][i] / a[i][i]
                    for k in range(i, n):  # sub line
                        a[j][k] -= q * a[i][k]
        return a
    
    def gauss_modificator(self, a, m, n):
        size1 = m-1 if m <= n else n
        for i in range(size1):
            mx = [0, 0]
            for j in range(i, m):  # Changed from n to m for row selection
                if abs(a[j][i]) > mx[0]:
                    mx = [abs(a[j][i]), j]
            a = self.swap_line(a, n, i, mx[1])
            for j in range(i+1, m):  # underdiag
                if a[i][i] != 0:  # Prevent division by zero
                    q = a[j][i] / a[i][i]
                    for k in range(i, n):  # j - iq
                        a[j][k] -= a[i][k] * q
        return a
    
    def gauss_modified_down(self, a, m, n):
        size1 = m-1 if m <= n else n
        for i in range(size1, 0, -1):  # num of work, diag el
            mx = [0, 0]
            for j in range(i+1):
                if abs(a[j][i]) > mx[0]:
                    mx = [abs(a[j][i]), j]
     
            self.swap_line(a, n, i, mx[1])
            for j in range(i):  # under el
                if a[i][i] != 0:  # Added check to prevent division by zero
                    q = a[j][i] / a[i][i]
                    for k in range(i+1):  # sub line
                        a[j][k] -= q * a[i][k]
        return a
    
    def matrix_rg(self, a, m, n):
        a = self.gauss_modified_up(a, m, n)
        rg = 0
        for i in range(min(m, n)):
            if a[i][i] != 0: 
                rg += 1 
        return rg
    
    def inverse_matrix(self, a, n):
        b = [[a[i][j] for j in range(n)] for i in range(n)]
        I = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        for i in range(n):
            self.add_col(b, I[i])
        self.gauss_down(b, n, 2*n)  
        self.gauss_up(b, n, 2*n)
        for i in range(n):
            if b[i][i] != 0:  # Added check to prevent division by zero
                t = b[i][i]
                for j in range(n, 2*n):
                    b[i][j] /= t
                b[i][i] = 1
        return [[b[i][j] for j in range(n, 2*n)] for i in range(n)]
    
    def slau(self, a, x, n):
        b = [[a[i][j] for j in range(n)] for i in range(n)]
        self.add_col(b, x)
        self.gauss_down(b, n, n+1)  
        self.gauss_up(b, n, n+1)
        for i in range(n):
            if b[i][i] != 0:  # Added check to prevent division by zero
                t = b[i][i]
                b[i][n] /= t
        return [b[i][n] for i in range(n)]
    
    def matrix_det(self, a, n):
        a_copy = [[a[i][j] for j in range(n)] for i in range(n)]  # Create a copy to avoid modifying original
        self.gauss_up(a_copy, n, n)
        det = 1
        for i in range(n):
            det *= a_copy[i][i]
        return det
    
    def sole(self, a, b, n):  # слау
        a_copy = [[a[i][j] for j in range(n)] for i in range(n)]  # Create a copy
        b_copy = [b[i] for i in range(n)]  # Create a copy of b
        self.add_col(a_copy, b_copy)
        self.gauss_up(a_copy, n, n+1)  # Fixed from gauss to gauss_up
        x = [0] * n
        for i in range(n-1, -1, -1):
            sum_ax = 0
            for j in range(i+1, n):
                sum_ax += a_copy[i][j] * x[j]
            if a_copy[i][i] != 0:  # Added check to prevent division by zero
                x[i] = (a_copy[i][n] - sum_ax) / a_copy[i][i]
        return x
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


    # Проверка Vector
    v1 = Vector(3)
    v1.mas = [1, 2, 3]
    v2 = Vector(3)
    v2.mas = [4, 5, 6]
    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("Vector 1 * Vector 2:", v1 * v2)

    mtx = Matrix()
    
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    
    print("Matrix A:")
    for row in A:
        print(row)
    
    print("\nMatrix B:")
    for row in B:
        print(row)
    
    print("\nSum of A and B:")
    sum_result = mtx.sum_matrix_with_check(A, B)
    if sum_result:
        for row in sum_result:
            print(row)
    
    print("\nTranspose of A:")
    transposed_A = mtx.transpos(A)
    for row in transposed_A:
        print(row)
    
    print("\nMultiplication of A and B:")
    mult_result = mtx.mul_matrix(A, B, 3, 3, 3)
    for row in mult_result:
        print(row)
    
    print("\nDeterminant of A:")
    det_A = mtx.matrix_det(A, 3)
    print(det_A)
    
    print("\nInverse of B (if exists):")
    try:
        inv_B = mtx.inverse_matrix(B, 3)
        for row in inv_B:
            print(row)
    except Exception as e:
        print(f"Cannot invert matrix B: {e}")
    
    print("\nSolving Ax = b with b = [1, 2, 3]:")
    b = [1, 2, 3]
    x = mtx.sole(A, b, 3)
    print(x)

if __name__ == "__main__":
    main()
