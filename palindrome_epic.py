import re


def is_palindrome(pal, list_of_pals):
    while pal:
        for pal in list_of_pals:
            pal = re.sub('\W+', '', pal)
            pal = pal.lower()
            while pal != 0:
                if len(pal) >= 1:
                    if pal == '':
                        return True
                    if pal[0] == pal[-1]:
                        return True
                    else:
                        return False


def main():
    with open('palindrome.txt') as f:
        list_of_pals = f.readlines()
    list_of_pals = [pal.strip() for pal in list_of_pals]
    pal = 'tot'
    print(is_palindrome(pal, list_of_pals))


if __name__ == '__main__':
    main()
