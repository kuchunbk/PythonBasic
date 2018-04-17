def get_lowest_common_multiple(number1, number2):
    min_number = min(number1, number2)
    max_number = max(number1, number2)
    if max_number % min_number:
        count = 1
        while count <= min_number:
            if max_number * count % min_number == 0:
                return max_number * count
            count += 1
    else:
        return max_number


if __name__ == "__main__":
    input_number1 = int(input('number1'))
    input_number2 = int(input('number2'))
    print("Lowest common multiple of two number: ",
          input_number1, input_number2)
    print(get_lowest_common_multiple(input_number1, input_number2))
