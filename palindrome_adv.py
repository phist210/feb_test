import re


def is_palindrome(sentence):
    sentence = re.sub('\W+', '', sentence.lower())
    while sentence:
        if sentence[0] != sentence[-1]:
            return False
        sentence = sentence[1:-1]
    return True


def main():
    sentence = input("\nEnter some text to determine if it is a palindrome: ")
    print(is_palindrome(sentence))


if __name__ == '__main__':
    main()
