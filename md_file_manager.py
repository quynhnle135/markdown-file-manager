import os
import datetime


def path_exists(path):
    """Check if given path exists."""
    try:
        return os.path.exists(path)
    except OSError as e:
        print(f"An error occurred: {e}")
        return False


def is_md_file(file_path):
    """Check if a given file path is for a Markdown file."""
    return file_path.endswith(".md")


def create_file(directory):
    pass


def read_file(file):
    pass


def count_md_files(directory):
    pass


def read_all_md_file(directory):
    pass


def md_file_generate(directory):
    pass