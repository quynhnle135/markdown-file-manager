import datetime
import os


def path_exists(path):
    try:
        return os.path.exists(path)
    except OSError as e:
        print(f"An error occurred: {e}")
        return False


def is_md_file(file_path):
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
            with open(file_path, "w") as file:
                file.write("# 1. What I Learned Today\n\n\n")
                file.write("# 2. Questions I Have\n\n\n")
                file.write("# 3. What I Found Challenging\n\n\n")
                file.write("# 4. Code I Wrote Today\n\n\n")
    else:
        print(f"{directory} path does not exist.")


def customized_md_file_generate(directory, days=7):
    if days == 7:
        md_file_generate(directory)
    else:
        if path_exists(directory):
            today = datetime.date.today()
            for i in range(1, days + 1):
                file_date = today + datetime.timedelta(days=i)
                file_name = f"{file_date.strftime('%Y%m%d')}.md"
                file_path = os.path.join(directory, file_name)
                with open(file_path, "w") as file:
                    file.write("# 1. What I Learned Today\n\n\n")
                    file.write("# 2. Questions I Have\n\n\n")
                    file.write("# 3. What I Found Challenging\n\n\n")
                    file.write("# 4. Code I Wrote Today\n\n\n")
        else:
            print(f"{directory} path does not exist.")
            return None


def update_md_file_content(file, new_content):
    if is_md_file(file):
        with open(file, "w") as f:
            f.write(new_content)
        print(f"New content has been updated in {file}")
    else:
        print(f"{file} file does not exist.")


def update_all_md_files_content_in_dir(directory, new_content):
    if path_exists(directory):
        files = os.listdir(directory)
        for f in files:
            if is_md_file(f):
                file_path = os.path.join(directory, f)
                with open(file_path, "w") as file:
                    file.write(new_content)
                print(f"New content has been updated in {file_path}")
        print("Finish updating content")
    else:
        print("Invalid path.")