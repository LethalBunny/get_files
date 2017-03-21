# This Python 3 script gathers names of all the files from the specified directory and all the directories nested inside.

## Usage:
#### 1. In terminal (solely for printing the file names)

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


#### 2. As module

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
