def last_name(input_lastname):
    return (input_lastname)

def first_name(input_firstname):
    return (input_firstname)

if __name__ == "__main__":
    input_lastname = input('xin moi nhap ho')
    input_firstname = input('xin moi nhap ten')
    print('ho ten nguoi dung la',first_name(input_firstname),last_name(input_lastname))