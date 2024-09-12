#натуральноее число сумма четных цифр этого числа или 0 если четных цифр в записи нет
while True:
    try:
        # Вводим число
        a = int(input("Введите натуральное число: "))
        if a <= 0:
            raise ValueError("Число должно быть натуральным (положительным).")
        sum_ = 0
        for element in str(a):
            if int(element) % 2 == 0:
                sum_ += int(element)
        print("Сумма четных цифр натурального числа равна: " + str(sum_))
        break

    except ValueError as e:
        print(f"Ошибка: {e}. Попробуйте еще раз.")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}.")
