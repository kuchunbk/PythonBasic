def cut_string(filename):
    f_extns = filename.split(".")
    return "The extension of the file is : " + repr(f_extns[-1])
# h�m repr Chuy?n �?i �?i t�?ng x th�nh m?t chu?i bi?u th?c
# c?t chu?i khi xu?t hi?n d?u .

if __name__ == "__main__":
    filename = input("Input the Filename: ")
    print(cut_string(filename))