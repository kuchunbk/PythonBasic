def result_value(my_dict):
    result = 1
    for key in my_dict:
        result = result * my_dict[key]
    return result

if __name__ == "__main__":
    my_dict = {'data1':100,'data2':-54,'data3':247}
    print(result_value(my_dict))
