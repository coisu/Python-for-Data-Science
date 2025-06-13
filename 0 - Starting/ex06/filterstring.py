import sys
from ft_filter import ft_filter


def filter_string(s: str, n: int) -> list:
    '''
    '''
    words = s.split(' ')
    find_longer = lambda word: len(word) > n
    longer = ft_filter(find_longer, words)
    return longer


def main():
    '''
    program entry
    check input string and call the function with the given string from STDIN
    '''
    try:
        if len(sys.argv) != 3:
            raise IndexError

        s = sys.argv[1]
        n = int(sys.argv[2])
        print(filter_string(s, n))
    except (IndexError, ValueError):
        print("AssertionError: the arguments are bad")
    except Exception as e:
        print(f"Unexpected error occured: {e}")


if __name__ == "__main__":
    '''
    main() is called only when the py script is excuted directly
    '''
    main()
