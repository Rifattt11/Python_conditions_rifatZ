import math

a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))
x = float(input('Введите значение x: '))
print()

if a*b < 2*x:
    result_y = (b * (math.e**(-3*x))) + math.sin(a)**2
else:
    result_y = (x**3/a) - (x/b)

print('y =',result_y)