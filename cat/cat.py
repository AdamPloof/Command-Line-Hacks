import argparse

def main():
    parser = argparse.ArgumentParser(description="Reads the supplied files and concatenates into a new file")
    parser.add_argument("selected_file", nargs='+', help="supply file name to be read", type=str)
    parser.add_argument("-c", "--cat", help="concatenate the files supplied into the following file", 
        type=str
    )

    args = parser.parse_args()

    # process arguments like so: file1 file2 --cat file3 (write file1 and file2 to file3)
    if args.cat:
        new_file = args.cat + ".txt"
        for selected_file in args.selected_file:
            with open(selected_file) as openFile:
                for line in openFile:
                    with open(new_file, "a") as writeFile:
                        writeFile.write(line)
                        print(line)
                
    else:
        for selected_file in args.selected_file:
            with open(selected_file) as openFile:
                for line in openFile:
                    print(line)

if __name__ == "__main__":
    main()