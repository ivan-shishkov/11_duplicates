import argparse
import sys
import os
from collections import defaultdict


def find_files_duplicates(path):
    files_locations = defaultdict(list)

    for root, __, files in os.walk(path):
        for filename in files:
            full_file_path = os.path.join(root, filename)
            file_size = os.path.getsize(full_file_path)

            files_locations[(filename, file_size)].append(full_file_path)

    return [item for item in files_locations.items() if len(item[1]) > 1]


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'path',
        help='a path for search duplicates of files '
             '(including subdirectories)',
        type=str,
    )

    command_line_arguments = parser.parse_args()

    return command_line_arguments


def print_files_duplicates_info(files_duplicates_info):
    if not files_duplicates_info:
        print('Files duplicates not found')
        return

    for file_duplicates in files_duplicates_info:
        filename = file_duplicates[0][0]
        file_size = file_duplicates[0][1]

        print()
        print('Found duplicates of {} with size {} bytes in:'.format(
            filename,
            file_size,
        ))
        for path in file_duplicates[1]:
            print(path)
    print()


def main():
    command_line_arguments = parse_command_line_arguments()

    path = command_line_arguments.path

    if not os.path.isdir(path):
        sys.exit('This path is not a directory or not exists')

    print_files_duplicates_info(
        files_duplicates_info=find_files_duplicates(path),
    )


if __name__ == '__main__':
    main()
