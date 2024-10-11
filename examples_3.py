def int_to_roman(num):
    # Определяем массивы для числовых значений и их римских эквивалентов
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman_numeral = ""
    i = 0

    # Используем цикл while для преобразования числа в римское представление
    while num > 0:
        # Определяем, сколько раз текущее значение из массива может быть вычтено из числа
        for _ in range(num // values[i]):
            roman_numeral += symbols[i]
            num -= values[i]
        i += 1

    return roman_numeral

# Запрашиваем у пользователя целое число
number = int(input("Введите целое число: "))

# Преобразуем число в римское представление
roman_representation = int_to_roman(number)

# Выводим результат
print(f"Римское представление числа {number}: {roman_representation}")
