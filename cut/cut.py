import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Select file, extract text and print to standard output")

    parser.add_argument("source_file", help="The source file to be read")
    parser.add_argument("-f", "--fields", help="Specifiy the fields to return after separating by delimiter",
        type=int, nargs='+'
    )
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-d", "--delim", help="Specify the delimiter to separate the text by",
        type=str
    )
    group.add_argument("-c", "--char", help="Specify the character range to be cut.",
        type=int, nargs='+'
    )

    args = parser.parse_args()

    if args.delim:
        readFile(args.source_file, sortArgs(args.delim), args.fields)
    elif args.char:
        readFile(args.source_file, sortArgs(args.char))
    else:
        sys.exit("You must enter either a character range, or delimiter and field range to cut")

#Make sure that a vailid integar pair has been entered for character and fields arguments.
def sortArgs(args_to_sort):
    try:
        if len(args_to_sort) > 2:
            print("You may only enter a maximum of two numbers for the character or fields range")
        else:
            return args_to_sort
    except TypeError:
            sys.exit("You must enter a valid integer pair for the field and character arguments.")


def readFile(source_file, cutter, fields=0):    
    with open(source_file, 'r') as f:
        lines = f.read()
        if fields != 0:
            delimSplitter(lines, cutter, fields)    
        else:
            characterSplitter(lines, cutter)

#Splits strings up by delimiter supplied in args.delim
def delimSplitter(file_to_parse, delimiter, fields):
    current_field  = ""
    all_fields = []
    for character in file_to_parse:
        if not character == delimiter:
            current_field += character
        else:
            all_fields.append(current_field)
            current_field = ""
    print(all_fields[fields[0]:fields[1]])

#Splits strings up by character and interprets ranges supplied in args.char
def characterSplitter(file_to_parse, character_range):
    print(file_to_parse[character_range[0]:character_range[1]])
    
if __name__ == "__main__":
    main()