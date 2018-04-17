def get_max_divisor_of_two_number(number1, number2):
    min_number = min(number1, number2)
    max_number = max(number1, number2)
    if max_number % min_number:
        for number in range(min_number // 2 + 1, 0, -1):
            if min_number % number == 0 and max_number % number == 0:
                return number
    else:
        return min_number


if __name__ == "__main__":
    input_number1 = int(input('number1'))
    input_number2 = int(input('number2'))
    print("max divisor of two number: ", input_number1, input_number2)
    print(get_max_divisor_of_two_number(input_number1, input_number2))