#!/usr/bin/python3

"""Change the name of video series from the long format to the short format 
(example : The.Big.Bang.Theory.S01E20.Xvid.anything.avi becomes S01E20).

This script recieves in parameter the path to the directory containing the videos series files.

"""

import os
import sys
import re


def normalise_path(path: str):
    """Add the '/' if it is absent in the end of the path."""
    if path[-1] != '/':
        path += '/'
    return path


def rename_files(path: str):
    """Rename the files in the path from the long format to the short format (see the description of the program up there)."""
    old_content = [f for f in os.listdir(path)]
    new_content = [re.sub(r".*[sS](\d\d)[eE](\d\d).*\.(.+)$", r"S\1E\2.\3", f) for f in old_content]
    print("Here is the changment that will be applied : ")
    for (old, new) in zip(old_content, new_content):
        print(old, "   ===>   ", new)
    choice = input("Continue ?(y/n) : ")

    if choice.lower() == 'y':
        for (old, new) in zip(old_content, new_content):
            os.rename(path + old, path + new)
    else:
        exit(0)


def main():
    """This is the main fonction."""
    if len(sys.argv) < 2:
        print("Usage : {} <path>".format(sys.argv[0]))
        sys.exit(-1)

    path = normalise_path(sys.argv[1])
    rename_files(path)

    print("The changments were applied with success.")

if __name__ == "__main__":
    main()
