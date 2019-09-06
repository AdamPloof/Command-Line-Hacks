import argparse
import os
import glob

def find_all(dir_name):
    if args.print:
        print(os.listdir(dir_name))

def find_some(dir_name):
    if args.print:
        print(glob.glob(in_dir))

parser = argparse.ArgumentParser(description="""find files in specified directory, if no directory
    exists, search current working directory"""
)

parser.add_argument("find", help="the directory to search", type=str)
parser.add_argument("-n", "--name", help="the name or pattern of the file to find", type=str)
parser.add_argument("-p", "--print", help="print the files and directories found", action="store_true")
parser.add_argument("-d", "--dir", help="only return directory names", action="store_true")
parser.add_argument("-f", "--file", help="only return file names", action="store_true")

args = parser.parse_args()

if args.find == "." and not args.name:
    in_dir = os.getcwd()
    find_all(in_dir)
else:
    in_dir = (args.find, args.name)
    in_dir = "/".join(in_dir)
    find_some(in_dir)