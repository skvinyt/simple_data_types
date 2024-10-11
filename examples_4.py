from fractions import Fraction

def parse_fraction(fraction_str):
    numerator, denominator = map(int, fraction_str.split('/'))
    return Fraction(numerator, denominator)

def main():
    # Запрашиваем у пользователя две дроби
    fraction1_str = input("Введите первую дробь (в формате a/b): ")
    fraction2_str = input("Введите вторую дробь (в формате a/b): ")

    # Преобразуем строки в объекты Fraction
    fraction1 = parse_fraction(fraction1_str)
    fraction2 = parse_fraction(fraction2_str)

    # Находим сумму и произведение дробей
    sum_fraction = fraction1 + fraction2
    product_fraction = fraction1 * fraction2

    # Выводим результаты
    print(f"Сумма дробей: {sum_fraction}")
    print(f"Произведение дробей: {product_fraction}")

# Запускаем программу
if __name__ == "__main__":
    main()
