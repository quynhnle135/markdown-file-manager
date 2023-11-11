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
        file_date = datetime.date.today()
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
            return lines
    else:
        print("File's format is not correct or file doesn't exist.")
        return None


def count_md_files(directory):
    if path_exists(directory):
        files = os.listdir(directory)
        count = sum(1 for file in files if is_md_file(file))
        if count <= 0:
            print(f"No available Markdown file in {directory} directory.")
            return count
        elif count == 1:
            print(f"There's 1 Markdown file in {directory} directory.")
            return count
        else:
            print(f"There're {count} Markdown files in {directory} directory.")
            return count
    else:
        print(f"{directory} path does not exist.")
        return None


def md_file_generate(directory):
    if path_exists(directory):
        today = datetime.date.today()
        for i in range(1, 8):
            file_date = today + datetime.timedelta(days=i)
            file_name = f"{file_date.strftime('%Y%m%d')}.md"
            file_path = os.path.join(directory, file_name)
            with open(file_path, "w") as f:
                f.write(f"{file_date} Markdonw file is created in {directory}.")
    else:
        print(f"{directory} path does not exist.")