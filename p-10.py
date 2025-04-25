# Xavier Beatrice P10
import sys, os
from os.path import split


def main(args):
    if len(args) < 1 or (len(args) > 1 and args[1] != "1") or (len(args) > 2):
        print("Incorrect number of arguments: ", len(args))
        print("Usage: p-10.py <search>")
        print("Usage (for linux): p-10.py <search> 1")
        sys.exit(1)
    splitter = ";"
    if len(args) > 1 and args[1] == "1":
        splitter = ":"
    value = os.getenv('PATH')
    directories = value.split(splitter)
    for value in directories:
        try:
            for i in os.listdir(value):
                if args[0] in i:
                    print(os.path.join(value, i))
        except FileNotFoundError:
            print("Could not find directory '%s' in path" % value)

main(sys.argv[1:])