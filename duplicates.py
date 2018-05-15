import argparse
import sys
import os
from collections import defaultdict


def get_files_duplicates(path):
    files_locations = defaultdict(list)

    for root, __, files in os.walk(path):
        for filename in files:
            full_file_path = os.path.join(root, filename)
            file_size = os.path.getsize(full_file_path)

            files_locations[(filename, file_size)].append(full_file_path)

    return filter(lambda item: len(item[1]) > 1, files_locations.items())


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'path',
        help='a path for search duplicates of files (including subdirectories)',
        type=str,
    )

    command_line_arguments = parser.parse_args()

    return command_line_arguments


def main():
    command_line_arguments = parse_command_line_arguments()

    path = command_line_arguments.path

    if not os.path.isdir(path):
        sys.exit('This path is not a directory or not exists')


if __name__ == '__main__':
    main()
