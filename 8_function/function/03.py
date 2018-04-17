def multiply_list(list1):
    multiply  = 1
    for item in list1:
        multiply = multiply * item
    return multiply 

if __name__ =="__main__":
    list1= (8, 2, 3, -1, 7)
    print(multiply_list(list1))