import datetime
import os
from typing import List, Optional


# Determine if the specified path is a valid path
def path_exists(path: str) -> bool:
    try:
        return os.path.exists(path)
    except OSError as e:
        print(f"An error occurred: {e}")
        return False


# Determine if the specified path/file is a valid Markdown file
def is_md_file(file_path: str) -> bool:
    return file_path.endswith(".md")


# Read content of given Markdown
def read_file(file: str) -> Optional[List[str]]:
    # Determine if the specified path/file is a valid Markdown file
    if is_md_file(file):
        with open(file, "r") as f:
            lines = f.readlines()
            for l in lines:
                print(l)
            return lines
    else:
        print("File's format is not correct or file doesn't exist.")
        return None


# Count the number of Markdowns in the given directory
def count_md_files(directory: str) -> Optional[int]:
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
            print(f"There are {count} Markdown files in {directory} directory.")
            return count
    else:
        print(f"{directory} path does not exist.")
        return None


# Create multiple Markdown files using a specified template if necessary
def generate_md_file(directory: str, args) -> None:
    # Verify if the user has specified a desired number of Markdown files
    if args.days:
        amount = args.days
    else:
        amount = 7
    # Determine if the specified path is a valid path
    if path_exists(directory):
        today = datetime.date.today()
        for i in range(0, amount + 1):
            file_date = today + datetime.timedelta(days=i)
            file_name = f"{file_date.strftime('%Y%m%d')}.md"
            file_path = f"{directory}/{file_name}"
            with open(file_path, "w") as f:
                # Generate Markdown using the Coding Journal template if args.coding is specified
                if args.coding:
                    coding_journal_template = open("/Users/quinnle/PycharmProjects/md-file-manager/templates/coding_journal_template.md", "r")
                    lines = coding_journal_template.read()
                    f.write(lines)
                # Generate Markdown using the Daily Practice template if args.practice is specified
                elif args.practice:
                    daily_practice_template = open("/Users/quinnle/PycharmProjects/md-file-manager/templates/daily_practice_template.md", "r")
                    lines = daily_practice_template.read()
                    f.write(lines)
                else:
                    f.write(f"{file_date.strftime('%Y%m%d')}")
            f.close()
            print(f"New file {file_name} is created.")
        print(f"Finish creating {amount} file(s).")
    else:
        print(f"{directory} does not exist.")
        return


# Replace existing content in the specified Markdown file with new content
def update_content(file: str, new_content: str) -> None:
    # Determine if the specified path/file is a valid Markdown file
    if is_md_file(file):
        with open(file, "w") as f:
            f.write(new_content)
        print(f"New content has been updated in {file}")
    else:
        print(f"{file} file does not exist.")


# Add new content to the end of the specified Markdown file
def add_new_content(file: str, new_content: str) -> None:
    # Determine if the specified path/file is a valid Markdown file
    if is_md_file(file):
        with open(file, "a") as f:
            f.write(new_content)
        print(f"New content is added to {file}")
        f.close()
    else:
        print("Invalid path or file.")
