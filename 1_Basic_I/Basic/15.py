import math

def calculate_volume(r):
    volume = 4/ 3 * math.pi * r ** 3
    return volume

if __name__ == "__main__":
    r = 6
    print(calculate_volume(r))