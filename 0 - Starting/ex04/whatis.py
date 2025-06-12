import sys

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)
    elif len(sys.argv) == 2:
        try:
            val = int(sys.argv[1])
            if isinstance(val, int):
                if val % 2:
                    print("I'm Odd.")
                else:
                    print("I'm Even.")
        except ValueError:
            print("AssertionError: argument is not an integer")
            sys.exit(1)
    sys.exit(0)