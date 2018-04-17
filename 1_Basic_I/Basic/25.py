def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
        return False

if __name__ == "__main__":
    group_data = [1, 5, 8, 3]
    n = 3
    print(is_group_member(group_data, n))