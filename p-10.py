# Xavier Beatrice P10
import sys, os
from os.path import split


def main(args):
    if len(args) < 1:
        print("Usage: p-10.py <search>")
        sys.exit(1)
    splitter = ";"
    if len(args) > 1 and args[1] == "1":
        splitter = ":"
    PATHVars = []
    value = os.getenv('PATH')
    directories = value.split(splitter)
    for value in directories:
        os.listdir(value)

main(sys.argv[1:])