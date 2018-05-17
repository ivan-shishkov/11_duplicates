import argparse
import sys
import os
from collections import defaultdict


def get_files_duplicates_info(path):
    files_locations = defaultdict(list)

    for root, _, file_names in os.walk(path):
        for file_name in file_names:
            full_file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(full_file_path)

            files_locations[(file_name, file_size)].append(full_file_path)

    return {
        file_info: file_paths
        for file_info, file_paths in files_locations.items()
        if len(file_paths) > 1
    }


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

    for (file_name, file_size), file_paths in files_duplicates_info.items():
        print()
        print('Found duplicates of {} with size {} bytes in:'.format(
            file_name,
            file_size,
        ))
        print('\n'.join(file_paths))
    print()


def main():
    command_line_arguments = parse_command_line_arguments()

    path = command_line_arguments.path

    if not os.path.isdir(path):
        sys.exit('This path is not a directory or not exists')

    print_files_duplicates_info(
        files_duplicates_info=get_files_duplicates_info(path),
    )


if __name__ == '__main__':
    main()
