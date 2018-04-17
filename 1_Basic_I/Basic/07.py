def cut_string(filename):
    f_extns = filename.split(".")
    return "The extension of the file is : " + repr(f_extns[-1])
# hàm repr Chuy?n ð?i ð?i tý?ng x thành m?t chu?i bi?u th?c
# c?t chu?i khi xu?t hi?n d?u .

if __name__ == "__main__":
    filename = input("Input the Filename: ")
    print(cut_string(filename))