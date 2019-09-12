import argparse
import re

def main():
    parser = argparse.ArgumentParser(description="""Search a file for patterns and return
        matches"""
    )

    parser.add_argument("file", help="the file to be searched", type=str)
    parser.add_argument("-p", "--pattern", help="the pattern to match", type=str)

    args = parser.parse_args()

    with open(args.file) as open_file:
        for line in open_file:
            if args.pattern in line:
                print(line)

if __name__ == "__main__":
    main()