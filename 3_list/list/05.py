def match_words(words):
    ctr = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr

if __name__ == "__main__":
    words = ['abc', 'xyz', 'aba', '1221']
print(match_words(words))