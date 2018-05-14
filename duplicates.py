import argparse


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


if __name__ == '__main__':
    main()
