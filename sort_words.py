def sort_words(words):
    sorted_words = words.split()
    sorted_words.sort(key=str.casefold)
    return ' '.join(sorted_words)


if __name__ == '__main__':
    print(sort_words('Orange banana Apple apple'))