import sys
from parser import Parser


def main():
    if len(sys.argv) != 2:
        raise ValueError("The program can accept just 2 args")
    parser = Parser(sys.argv[1])
    terms = parser.start()
    print(f"TERMS: {terms}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}")
