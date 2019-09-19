import argparse
import re

def main():
    parser = argparse.ArgumentParser(description="""Search a file for patterns and return
        matches"""
    )

    parser.add_argument("file", help="the file to be searched", type=str)
    parser.add_argument("-p", "--pattern", help="the pattern to match", type=str)

    args = parser.parse_args()
    pattern = re.compile(args.pattern)

    with open(args.file, r) as open_file:
        search_text = open_file.read()
        matches = pattern.finditer(search_text)

        for match in matches:
            print(match)

if __name__ == "__main__":
    main()