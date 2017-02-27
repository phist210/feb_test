import re


def is_palindrome(sentence):
    sentence = re.sub('\W+', '', sentence.lower())
    if not sentence:
        return True
    first = sentence[0]
    last = sentence[-1]
    rest = sentence[1:-1]
    if first == last:
        return is_palindrome(rest)
    else:
        return False


def main():
    sentence = input("\nEnter some text to determine if it is a palindrome: ")
    print(is_palindrome(sentence))


if __name__ == '__main__':
    main()
