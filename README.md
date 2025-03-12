Класс LongNum

Класс LongNum представляет собой структуру для работы с длинными числами. Он содержит атрибуты deg (размер числа), mas (список цифр числа) и sign (знак числа). Конструктор позволяет инициализировать объект с заданными параметрами. Метод __str__ преобразует объект в строку, включая знак и цифры числа. Метод simplify() удаляет ведущие нули в числе, упрощая его представление.

Класс Polinoms

Класс Polinoms предназначен для работы с многочленами. Атрибут dim хранит степень многочлена, а mas — список коэффициентов. Реализован метод __add__, который выполняет сложение двух многочленов, а также метод __str__, позволяющий вывести многочлен в удобочитаемом виде, где коэффициенты представлены с соответствующими степенями переменной x.

Класс Rational

Класс Rational реализует структуру для работы с рациональными числами. Он хранит числитель (m) и знаменатель (n). Если знаменатель равен 1, объект представляется в виде целого числа, в противном случае — в виде дроби m/n. Метод __str__ формирует строковое представление объекта.

Класс Vector

Класс Vector предназначен для представления и работы с векторами. Он содержит атрибут dim (размерность вектора) и mas (список значений координат вектора). Реализованы операции сложения векторов и скалярного произведения (__add__, __mul__). Метод __str__ позволяет вывести вектор в виде списка его координат.

Класс Matrix

Класс Matrix предназначен для работы с матрицами и содержит множество методов для различных операций. Он реализует суммирование матриц, транспонирование, умножение, вычисление определителя, получение миноров, нахождение ранга матрицы, а также методы решения систем линейных уравнений (методом Гаусса и обратной матрицы). Методы sum_matrix и sum_matrix_with_check выполняют сложение двух матриц, transpos транспонирует матрицу, mul_matrix умножает две матрицы, а det_lapl и laplass вычисляют определитель с использованием разложения Лапласа.

Методы gauss_up, gauss и gauss_down реализуют прямой и обратный ход метода Гаусса, а gauss_modified_up, gauss_modificator и gauss_modified_down улучшают его, выбирая максимальный элемент для приведения к ступенчатому виду. inverse_matrix находит обратную матрицу, а slau и sole решают систему линейных уравнений разными методами. matrix_det вычисляет определитель матрицы методом Гаусса, а matrix_rg находит ее ранг.

--

The `LongNum` class represents large numbers with a customizable number of digits and sign. It includes methods for initialization, string representation, and simplification. The `simplify` method removes leading zeros to ensure a compact representation.

The `Polinoms` class represents polynomials, allowing for operations such as addition. The polynomial's coefficients are stored in a list, and the `__str__` method formats the polynomial in a human-readable form. The `__add__` method enables polynomial addition by summing corresponding coefficients.

The `Rational` class models rational numbers as fractions. It consists of a numerator (`m`) and a denominator (`n`), with an appropriate string representation to display fractions correctly.

The `Vector` class represents mathematical vectors, supporting addition and dot product operations. The `__add__` method performs element-wise vector addition, while `__mul__` calculates the dot product. The string representation outputs the vector's list format.

The `Matrix` class provides functionality for matrix operations, including addition, transposition, multiplication, determinant calculation, and solving systems of linear equations. Methods like `sum_matrix` and `sum_matrix_with_check` allow matrix addition, while `mul_matrix` handles matrix multiplication. The `transpos` method computes the transpose of a matrix. Determinant calculations are performed using the Laplace expansion (`det_lapl`) and Gaussian elimination (`matrix_det`). The class also includes implementations for the Gauss method to transform matrices into triangular forms (`gauss_up`, `gauss_down`) and solve systems of linear equations (`sole`). Additionally, `inverse_matrix` computes the inverse of a square matrix, and `slau` is used to solve linear equation systems.

