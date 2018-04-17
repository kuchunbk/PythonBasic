from collections import Counter
def count_words(str1):
    words = str1.split()
    wordCount = Counter(words)
    return wordCount

if __name__ == "__main__":
    str1 = 'tran van luan'
    print(count_words(str1))