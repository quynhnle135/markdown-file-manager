import datetime
import os


# Validate entered path/directory
def path_exists(path):
    try:
        return os.path.exists(path)
    except OSError as e:
        print(f"An error occurred: {e}")
        return False


# Validate if enter path/file is a valid Markdown
def is_md_file(file_path):
    return file_path.endswith(".md")


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
            print(f"There are {count} Markdown files in {directory} directory.")
            return count
    else:
        print(f"{directory} path does not exist.")
        return None


def generate_md_file(directory, args):
    if args.days:
        amount = args.days
    else:
        amount = 7
    if args.coding:
        template = "/Users/quinnle/PycharmProjects/md-file-manager/templates/coding_journal_template.md"
    elif args.practice:
        template = "/Users/quinnle/PycharmProjects/md-file-manager/templates/daily_practice_template.md"
    else:
        template = ""
    if path_exists(directory):
        today = datetime.date.today()
        for i in range(1, amount + 1):
            file_date = today + datetime.timedelta(days=i)
            file_name = f"{file_date.strftime('%Y%m%d')}.md"
            file_path = f"{directory}/{file_name}"
            with open(file_path, "w") as f:
                if args.coding:
                    coding_journal_template = open("/Users/quinnle/PycharmProjects/md-file-manager/templates/coding_journal_template.md", "r")
                    lines = coding_journal_template.read()
                    f.write(lines)
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


def update_content(file, new_content):
    if is_md_file(file):
        with open(file, "w") as f:
            f.write(new_content)
        print(f"New content has been updated in {file}")
    else:
        print(f"{file} file does not exist.")


def add_new_content(file, new_content):
    if is_md_file(file):
        with open(file, "a") as f:
            f.write(new_content)
        print(f"New content is added to {file}")
        f.close()
    else:
        print("Invalid path or file.")
