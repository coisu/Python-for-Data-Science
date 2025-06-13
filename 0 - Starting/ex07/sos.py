import sys



NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}


def print_morse(s: str):
    res = ""
    for c in s:
        res += NESTED_MORSE.get(c, "")
    print(res)


def validate_arg(s: str):
    for c in s:
        if c.isalpha() is False and c.isdigit() is False and c != ' ':
            return False
    return True


def main():
    '''
    program entry
    check input string and call the function with the given string from STDIN
    '''
    try:
        if len(sys.argv) != 2:
            raise IndexError

        s = sys.argv[1]
        if validate_arg(s):
            print_morse(s.upper())
        else:
            raise AssertionError()
    except (IndexError, ValueError, AssertionError):
        print("AssertionError: the arguments are bad")
    except Exception as e:
        print(f"Unexpected error occured: {e}")


if __name__ == "__main__":
    '''
    main() is called only when the py script is excuted directly
    '''
    main()