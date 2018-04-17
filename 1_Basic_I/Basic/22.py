def list_count_4(number):
    count = 0  
    for num in number:
        if num == 4:
            count = count + 1
    return count

if __name__ == "__main__":
    number = [1,2,3,4,5,6,7,4,3,4]
    print(list_count_4(number))