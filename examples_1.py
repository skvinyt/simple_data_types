def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Запрашиваем у пользователя два целых числа
num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))

# Находим НОД
result = gcd(num1, num2)

# Выводим результат
print(f"Наибольший общий делитель чисел {num1} и {num2} равен {result}.")
