while True:
    try:
        s = input("Введите строку текста: ")
        s = s.swapcase()
        print(s)
        m = s.split()
        longest = max(s.split(), key = len)
        print(longest)
        sum_ = 0
        for element in s:
            if element.isdigit():
                sum_ += int(element)
        print(sum_)
        break
    except ValueError as e:
        print(f"Ошибка: {e}. Попробуйте еще раз.")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}.")