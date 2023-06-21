from elliptic_curves import Point, EllipticCurve

# Створення еліптичної кривої y^2 = x^3 + ax + b (mod p)
a = 2
b = 3
p = 17
curve = EllipticCurve(a, b, p)

# Створення точок на еліптичній криві
point1 = Point(5, 1)
point2 = Point(6, 3)

# Додавання точок
point_sum = curve.add_points(point1, point2)
print(f"Сума точок {point1} та {point2}: {point_sum}")

# Подвоєння точки
point_double = curve.double_point(point1)
print(f"Подвоєна точка {point1}: {point_double}")

# Множення точки на скаляр
scalar = 5
point_mult = curve.multiply_point(point1, scalar)
print(f"Множення точки {point1} на скаляр {scalar}: {point_mult}")
