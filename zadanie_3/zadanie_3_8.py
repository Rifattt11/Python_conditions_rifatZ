x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
print()

if x**2 + y**2 <= 1:
    if x + y <= -1:
        result = True
    else:
        result = False
else:
    result = False

print(result)