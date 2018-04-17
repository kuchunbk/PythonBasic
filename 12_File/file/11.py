def getSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size

file = open('E:\\Tu hocj\\abc.txt', 'rb')
print (getSize(file))
          