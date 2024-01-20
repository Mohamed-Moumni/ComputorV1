import sys


def main():
    if len(sys.argv) != 2:
        raise ValueError("The program can accept just 2 args")


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}")
