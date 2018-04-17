def word_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())
print("Number of words in the file :",word_count("E:\\Tu hocj\\abc.txt"))