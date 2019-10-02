import argparse
import re

def main():
    parser = argparse.ArgumentParser(description="Locates and replace patterns within a file")

    parser.add_argument("file_name", help="The file to be searched", type=str)
    parser.add_argument("-p", "--pattern", help="The pattern to search for", type=str)
    parser.add_argument("-s","--sub", help="The pattern to substitute", type=str)

    args = parser.parse_args()

    # make sure a pattern to search a substitution are provided
    if args.pattern and args.sub:
        pattern = re.compile(args.pattern)
        substitute(args.file_name, pattern, args.sub)
    elif args.pattern or args.sub:
        print("Patterns must be paired with a corresponding substitution")
    else:
        with open(args.file_name, "r") as f:
            for line in f:
                print(line)

# substitute the string provided by the sub argument for the pattern provided
def substitute(file_name, pattern_to_find, sub_pattern):
    with open(file_name, "r") as f:
        subText = f.read()
        matches = pattern_to_find.findall(subText)

        if len(matches) > 1:
            for current_match in matches:
                subText = subText.replace(current_match, sub_pattern)
        else:
            subText = subText.replace(matches, sub_pattern)
        
        print(subText)

if __name__ == "__main__":
    main()
