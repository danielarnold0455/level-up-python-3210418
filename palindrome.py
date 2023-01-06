import string


class Palindrome:

    _word = str()
    def __init__(self, word:str):
        self._word = word

    def check_palindrome(self):
        f = filter(str.isalpha, self._word.casefold())
        word = list(f)
        return word == list(reversed(word))

    def __str__(self):
        return f'Is {self._word!r} a palindrom?: {self.check_palindrome()}'


if __name__ == '__main__':
    palindrome = Palindrome("Go hang a salami - I'm a lasagna hog!")
    print(palindrome)
    print(Palindrome('dog'))