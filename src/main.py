import sys
from parsing import parser


def main():
    if len(sys.argv) != 2:
        raise Exception("The program can accept just 2 args")
    polynomial = parser(sys.argv[1])


if __name__ == "__main__":
    main()
