def chan_le(input_number):
    if input_number % 2 == 0:
        return 'so chan'
    else :
        return 'so le'

if __name__ == "__main__":
    input_number = int(input('xin moi nhap so'))
    print(chan_le(input_number))