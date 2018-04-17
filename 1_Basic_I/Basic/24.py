def is_vowel(char):

    all_vowels = 'aeiou'

    return char in all_vowels

if __name__ == "__main__":
    char = input('xin moi nhap chuoi')
    print(is_vowel(char))