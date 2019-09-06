import argparse

parser = argparse.ArgumentParser(description="Do some stuff to some stuff")
group = parser.add_mutually_exclusive_group()
group.add_argument("-b", "--bold", action="store_true", help="make the text bold")
group.add_argument("-i", "--italic", action="store_true", help="make the text italic")
group.add_argument("-u", "--underline", action="store_true", help="underline the text")

parser.add_argument("recall", help="return the string", type=str)
parser.add_argument("--foo", help="foo")
parser.add_argument("--bar", help="bar")
parser.add_argument("--baz", help="baz")

args = parser.parse_args()

print(args.recall)
