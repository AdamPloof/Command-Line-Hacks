import argparse

def main():
    parser = argparse.ArgumentParser(description="Sort each line of supplied input")

    parser.add_argument("file_name", help="the name of the file to sort", type=str)
    parser.add_argument("-c", "--case", help="ignores the case of each line", action="store_true")
    parser.add_argument("-d", "--desc", help="output of sort is in reverse (descending) order",
        action="store_true"
    )

    args = parser.parse_args()

    with open(args.file_name, "r") as f:
        sort_file = f.readlines()

        if args.case and args.desc:
            sorted_file = sorted(sort_file, key=str.lower, reverse=True)
        elif args.case:
            sorted_file = sorted(sort_file, key=str.lower)
        elif args.desc:
            sorted_file = sorted(sort_file, reverse=True)
        else:
            sorted_file = sorted(sort_file)

        for item in sorted_file:
            print(item)

if __name__ == "__main__":
    main()