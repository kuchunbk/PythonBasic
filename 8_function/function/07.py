def string_test(str1):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for item in str1:
        if item.isupper():
            d["UPPER_CASE"]+=1
        elif item.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    return (d)

if __name__=="__main__":
    str1 = 'The quick Brow Fox'
    print(string_test(str1))