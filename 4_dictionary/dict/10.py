def sum_value_dict(my_dict):
    return sum(my_dict.values())

if __name__=="__main__":
    my_dict = {'data1':100,'data2':-54,'data3':247}
    print(sum_value_dict(my_dict))