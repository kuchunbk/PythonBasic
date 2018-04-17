import calendar

def print_month(year,month):
    return calendar.month(year, month)

if __name__ == "__main__":
    year = int(input("Input the year : "))
    month = int(input("Input the month : "))
    print(print_month(year,month))