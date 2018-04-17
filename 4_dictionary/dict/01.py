import operator

def Sort_value_reduction(dict1):
    return sorted(d.items(), key=operator.itemgetter(0))

def Sort_value_increase(dict1):
    return  sorted(d.items(), key=operator.itemgetter(0),reverse=True)

if __name__ == "__main__":
    dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    print(Sort_value_reduction(dict1))
    print(Sort_value_increase(dict1))