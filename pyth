import sys
import math
from sympy import Symbol, Eq, solve

# Клас, що представляє точку на еліптичній кривій
class ECPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Операція додавання двох точок на еліптичній кривій
def add_points(p, q, a, b, p_value):
    if p == None:
        return q
    if q == None:
        return p

    # Обчислення спільного додаткового коефіцієнту
    if p != q:
        m = (q.y - p.y) * mod_inverse(q.x - p.x, p_value)
    else:
        m = (3 * p.x**2 + a) * mod_inverse(2 * p.y, p_value)

    # Обчислення координат x і y для нової точки
    x = (m**2 - p.x - q.x) % p_value
    y = (m * (p.x - x) - p.y) % p_value

    return ECPoint(x, y)

# Операція подвоєння точки на еліптичній кривій
def double_point(p, a, b, p_value):
    if p == None:
        return None

    # Обчислення спільного додаткового коефіцієнту
    m = (3 * p.x**2 + a) * mod_inverse(2 * p.y, p_value)

    # Обчислення координат x і y для нової точки
    x = (m**2 - 2 * p.x) % p_value
    y = (m * (p.x - x) - p.y) % p_value

    return ECPoint(x, y)

# Операція множення точки на скаляр
def scalar_multiply(k, p, a, b, p_value):
    binary = bin(k)[2:]  # Переведення скаляра в двійкову форму
    result = None

    # Проходження по двійковому представленню скаляра
    for bit in binary:
        result = double_point(result, a, b, p_value)

        if bit == '1':
            result = add_points(result, p, a, b, p_value)

    return result

# Обчислення оберненого за модулем числа
def mod_inverse(a, m):
    if math.gcd(a, m) != 1:
        return None

    # Використання розширеного алгоритму Евкліда
    x, y, g = extended_gcd(a, m)

    return x % m

# Розширений алгоритм Евкліда
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_gcd(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y

# Перевірка належності точки до еліптичної кривої
def is_on_curve(point, a, b, p_value):
    return (point.y**2 - (point.x**3 + a * point.x + b)) % p_value == 0

# Приклад використання функцій для еліптичних кривих
def main():
    # Параметри еліптичної кривої
    a = 2
    b = 7
    p_value = 17  # Розмір полія GF(p)

    # Базова точка G
    G = ECPoint(5, 1)

    # Перевірка базової точки G належності до кривої
    if not is_on_curve(G, a, b, p_value):
        print("Базова точка G не належить до кривої")
        return

    # Приклад обчислення подвоєної точки
    double_G = double_point(G, a, b, p_value)
    print("Подвоєна точка G:", double_G)

    # Приклад обчислення додавання двох точок
    H = ECPoint(12, 6)
    sum_points = add_points(G, H, a, b, p_value)
    print("Сума точок G і H:", sum_points)

    # Приклад скалярного множення точки G на скаляр k
    k = 9
    scalar_mult = scalar_multiply(k, G, a, b, p_value)
    print("Скалярне множення точки G на скаляр k:", scalar_mult)

if __name__ == "__main__":
    main()
