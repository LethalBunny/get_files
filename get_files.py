#!/usr/bin/env python3

"""
This script gathers names of all the files from the specified
directory and all the directories nested inside.

Usage:
    In terminal (solely for printing the file names)

    dir_name : obligatory positional argument, directory must either be in the
               current working directory or it's full path must be provided
    -t       : optional space - separated file extensions (all files are
               printed by default)
    e.g.
    .../python get_files.py my_dir
    .../python get_files.py my_dir -t jpg
    .../python get_files.py my_dir -t exe txt pdf

    Note that if the dir_name is invalid, nothing will be printed, but if
    the specified file types couldn't be found then appropriate message
    will be shown.


    As module

    Use the function get_files to get a mapping of all found files.
    e.g.
    import get_files
    files = get_files.get_files(my_dir)
    txt_files = files['txt']
    pdf_files = files['pdf']
    for ext in files:
        print(ext, files[ext])

    Note that in case of an invalid directory name an empty
    defaultdict(list) (dictionary-like object) will be returned.
"""


import os
from collections import defaultdict


def get_files(dir_name):
    """Gets names of all the files inside the specified directory

    Gets names of all the files inside the specified directory, stores them
    in a defaultdict object using the following data structure:
    files["ext_1"] = ["file_1.ext_1", file_2.ext_1", ...]
    """
    files = defaultdict(list)
    for _, _, file_names in os.walk(dir_name):
        for fn in file_names:
            ext = os.path.splitext(fn)[1].lstrip('.')
            files[ext].append(fn)
    return files


def print_files(mapping, extensions=None):
    """Prints files of specified extensions (or all by default).

    Prints the files of specified extensions (or all by default) based on
    the mapping received from the get_files function, results are
    seperated by type.
    """
    extensions = extensions or iter(mapping)
    for ext in extensions:
        files = mapping[ext]
        if files:
            print("{} files:\n".format(ext))
            print("\n".join("- {}".format(f) for f in files))
            print("\n")
        else:
            print("no files of type {} found\n".format(ext))


def main():
    import argparse
    parser = argparse.ArgumentParser(description="get files from a directory")
    parser.add_argument('dir_name', help="name of a directory (or full path)")
    parser.add_argument('-t', help="file type(s) to output", nargs='+',
                        dest='extensions', metavar='ext')
    args = parser.parse_args()
    mapping = get_files(args.dir_name)
    print('\n')
    print_files(mapping, args.extensions)

if __name__ == '__main__':
    main()