# Anti-Duplicator

This script allows to find files duplicates (files with same both filename and size) in given path (including subdirectories).

# Quickstart

For script launch need to install Python 3.5.

Usage:

```bash

$ python3 duplicates.py -h
usage: duplicates.py [-h] path

positional arguments:
  path        a path for search duplicates of files (including subdirectories)

optional arguments:
  -h, --help  show this help message and exit

```

Example of script launch on Linux:

```bash

$ python3 duplicates.py ~/some_dir

Found duplicates of file1.txt with size 1234 bytes in:
/home/user/some_dir/file1.txt
/home/user/some_dir/dir1/file1.txt

Found duplicates of file2.txt with size 4321 bytes in:
/home/user/some_dir/dir1/file2.txt
/home/user/some_dir/dir1/dir2/file2.txt
/home/user/some_dir/dir1/dir2/dir3/file2.txt

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
