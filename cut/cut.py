import argparse

def main():
    parser = argparse.ArgumentParser(description="Select file, extract text and print to standard output")

    parser.add_argument("source_file", help="The source file to be read")
    parser.add_argument("-d", "--delim", help="Specify the delimiter to separate the text by",
        type=str
    )
    parser.add_argument("-c", "--char", help="Specify the character range to be cut."
        type=str
    )

    args = parser.parse_args()

def readFile(sourceFile):
    with open(sourceFile, r) as f:
        lines = f.read()

#Splits strings up by character and interprets ranges supplied in args.char
def characterSplitter(char):
    pass

#Splits strings up by delimiter supplied in args.delim
def delimSplitter(delim):
    pass
    


if __name__ == "__main__":
    main()