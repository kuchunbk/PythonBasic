def calculate_total_money(principal, rate, year):
    mount = principal * (1 + rate) ** year
    return mount


if __name__ == "__main__":
    rate = float(input('xin moi nhap lai suat'))
    principal = float(input('von goc'))
    year= int(input('so nam'))
    print(calculate_total_money(principal, rate, year))
