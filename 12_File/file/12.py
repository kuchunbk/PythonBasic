def write_list(colors):
    with open('abc.txt','w') as my_file:
        for color in colors:
            my_file.write("%s\n" %color)
    content = open('abc.txt')
    return content.read()

if __name__ =="__main__":
    colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    print(write_list(colors))