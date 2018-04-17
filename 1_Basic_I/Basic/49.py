from os import listdir
from os.path import isfile, join

def print_file(input_data):
    list1 =[]
    for file in listdir(input_data):
        if isfile(join(input_data, file)):
            list1.append(file)
    return list1
        
if __name__=="__main__":
    input_data = "E:\\Tu hocj\\"
    print(print_file(input_data))