import sys


def count_text(text: str):
    '''
    for this exercise String library is not allowed,
    so it will go throgh a loop and check character by character
    the first if condition is for the protection of input by ctrl + D
    '''
    upper = 0
    lower = 0
    mark = 0
    space = 0
    digit = 0
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    if text is None:
        text = ""
    for c in text:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c in punctuation_chars:
            mark += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digit += 1
    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{mark} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    '''
    program entry
    check input string and call the function with the given string from STDIN
    '''
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print("What is the text to count?")
            text = sys.stdin.readline()
        count_text(text)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Unexpected error occured: {e}")


if __name__ == "__main__":
    '''
    main() is called only when the py script is excuted directly
    '''
    main()
