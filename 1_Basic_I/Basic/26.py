def histogram(items):
    for n in items:
        output = ''
        times = n
    while( times > 0 ):
        output += '*'
        times = times - 1
        print(output)

if __name__ == "__main__":
    items= [2, 3, 6, 5]
    print(histogram(items))