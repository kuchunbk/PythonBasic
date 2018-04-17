def not_poor(str1):
    snot = str1.find('not')
    sbad = str1.find('poor')
    if sbad > snot:
        str1 = str1.replace(str1[snot:(sbad+4)], 'good')
    return str1

if __name__ =="__main__":
    str1= ' The lyrics is not that poor!'
    print(not_poor(str1))