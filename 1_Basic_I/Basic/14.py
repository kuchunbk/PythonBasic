from datetime import date

def count_day(f_date,l_date):
    delta= f_date - l_date
    return delta

if __name__ == "__main__":
    f_date = date(2014, 7, 2)
    l_date = date(2014, 7, 11)
    print(count_day(f_date,l_date))