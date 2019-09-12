import argparse
import os
import glob

# if "." or cwd is provided as a search path
def find_all(dir_name):
    found_files = os.listdir(dir_name)
    if args.print:
        if args.dir:
            file_path_array = [os.path.dirname(file_path) for file_path in found_files]
        elif args.file:
            file_path_array = [os.path.basename(file_path) for file_path in found_files]
        else:
            file_path_array = found_files
    
    # check if the exec argument was given
    if args.exec:
        exec(file_path_array)
    else:
        print(file_path_array)

# for any other search path
def find_some(dir_name):
    found_files = glob.glob(in_dir)
    if args.print:
        if args.dir:
            file_path_array = [os.path.dirname(file_path) for file_path in found_files]
        elif args.file:
            file_path_array = [os.path.basename(file_path) for file_path in found_files]
        else:
            file_path_array = found_files

    # check if the exec argument was given
    if args.exec:
        exec(file_path_array)
    else:
        print(file_path_array)

# if --exec is included as an argument. Obviously just a placeholder and not really executing any commands
def exec(found_files):
    if args.exec == "rm":
        print(["The following file has been removed: " + i for i in found_files])
    elif args.exec == "dup":
        print(["The following file has been duplicated: " + i for i in found_files])
    elif args.exec == "mv":
        print(["The following file has been moved: " + i for i in found_files])
    else:
        pass


parser = argparse.ArgumentParser(description="""find files in specified directory, if no directory
    exists, search current working directory"""
)

parser.add_argument("find", help="the directory to search", type=str)
parser.add_argument("-n", "--name", help="the name or pattern of the file to find", type=str)
parser.add_argument("-p", "--print", help="print the files and directories found", action="store_true")
parser.add_argument("-e", "--exec", help="execute a command on the found files and/or directories",
    type=str, choices=["rm", "dup", "mv"]
)

group = parser.add_mutually_exclusive_group()
group.add_argument("-d", "--dir", help="only return directory names", action="store_true")
group.add_argument("-f", "--file", help="only return file names", action="store_true")

args = parser.parse_args()

if args.find == "." and not args.name:
    in_dir = os.getcwd()
    find_all(in_dir)
else:
    in_dir = (args.find, args.name)
    in_dir = "/".join(in_dir)
    find_some(in_dir)