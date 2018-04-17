import math
def calculate_distance(input_xa, input_ya, input_xb, input_yb):
    distance = math.sqrt((input_xa - input_xb) ** 2
                         + (input_ya - input_yb) ** 2)
    return distance


if __name__ == "__main__":
    input_xa = float(input('xa'))
    input_ya = float(input('ya'))
    input_xb = float(input('xb'))
    input_yb = float(input('yb'))
    print(calculate_distance(input_xa, input_ya, input_xb, input_yb))
