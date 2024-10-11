def to_hex(num):
    if num == 0:
        return '0'

    is_negative = num < 0
    num = abs(num)

    hex_digits = "0123456789ABCDEF"
    hex_str = ""

    while num > 0:
        remainder = num % 16
        hex_str = hex_digits[remainder] + hex_str
        num //= 16

    if is_negative:
        hex_str = '-' + hex_str

    return hex_str

# Запрашиваем у пользователя целое число
number = int(input("Введите целое число: "))

# Преобразуем число в шестнадцатеричное представление
hex_representation = to_hex(number)

# Выводим результат
print(f"Шестнадцатеричное представление числа {number}: {hex_representation}")

# Проверка с использованием встроенной функции hex
print(f"Проверка с использованием встроенной функции hex: {hex(number)}")
