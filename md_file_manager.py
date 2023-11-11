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


def generate_single_md_file(path):
    if path_exists(path):
        file_date = datetime.datetime.now()
        file_name = f"{file_date.strftime('%y%m%d')}.md"
        file_path = os.path.join(path, file_name)
        with open(file_path, "w") as f:
            f.write(f"This file is created at {file_date} in {file_path} directory.")
    else:
        print("The given path does not exist.")


def read_file(file):
    if is_md_file(file):
        with open(file, "r") as f:
            lines = f.readlines()
            for l in lines:
                print(l)
    else:
        print("File's format is not correct or file doesn't exist.")


def count_md_files(directory):
    pass


def read_all_md_file(directory):
    pass


def md_file_generate(directory):
    pass