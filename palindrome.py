import re


def is_palindrome(sentence):
    sentence = sentence.lower()
    if len(sentence) >= 1:
        if sentence == '':
            return True
        if sentence[0] == sentence[-1]:
            return True
        else:
            return False
    return is_palindrome(sentence[1:-1])


def main():
    sentence = input("\nEnter some text to determine if it is a palindrome: ")
    sentence = re.sub('\W+', '', sentence)
    print(is_palindrome(sentence))


if __name__ == '__main__':
    main()
