import os.path
def check_file():
    open('abc.txt','w')
    return os.path.isfile('abc.txt')

if __name__ =="__main__":
    print(check_file())