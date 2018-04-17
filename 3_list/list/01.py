def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers

if __name__ == "__main__":
    items = [1,3,4,5,6]
    print(sum_list(items))