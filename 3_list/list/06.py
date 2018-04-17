from operator import itemgetter , attrgetter
def Sort(data):
    return sorted(data, key=itemgetter(1))

if __name__ == "__main__":
    data = [(2, 3), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(Sort(data))