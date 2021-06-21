import math
print("кооф А")
a = int(input())
print("кооф Б")
b = int(input())
print("кооф С")
c = int(input())

discr = b ** 2 - 4 * a * c


if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(x1)
    print(x2)
if discr == 0:
    x = -b / (2 * a)
    print(x)
if discr < 0:
    print("Корней нет")