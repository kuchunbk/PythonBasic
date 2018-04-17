import random
def random_line(file_name):
    lines = open(file_name).read().splitlines()
    return random.choice(lines)

if __name__ =="__main__":
    file_name= 'E:\\T? H?c\\python\\test.txt'
    print(random_line(file_name))