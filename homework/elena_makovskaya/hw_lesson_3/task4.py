#Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь
from math import sqrt

leg_1 = 10
leg_2 = 13

hypotenuse = sqrt(leg_1**2 + leg_2**2)
area = 0.5 * leg_1 * leg_2

print(hypotenuse)
print(area)