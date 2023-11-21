from md_file_manager import *
import argparse


def main():
    parser = argparse.ArgumentParser(description="MD File Manager")
    parser.add_argument("-p", "--path", help="Check if the specified path exists in the system")
    parser.add_argument("-f", "--file", help="Verify the specified file is a Markdown (.md) file")
    parser.add_argument("-r", "--read", help="Read and display the contents of a specified file.")
    parser.add_argument("-co", "--count", help="Count the number of Markdown (.md) files in the specified "
                        "directory. Use '.' to count files in the current directory.")
    parser.add_argument("-g", "--generate", help="Generate multiple Markdown files. "
                        "If specified is not entered, default amount of files will be created is 7.")
    parser.add_argument("-a", "--add", help="Add new content to existing files.")
    parser.add_argument("-u", "--update", help="Updated contents of Markdown files in the specified directory.")
    parser.add_argument("-d", "--days", type=int, help="Number of days to generate files for (default: 7).")
    parser.add_argument("-ct", "--content", type=str, help="New content for updating.")
    parser.add_argument("-cj", "--coding", action="store_true", help="Generate file with Coding Journal template")
    parser.add_argument("-dp", "--practice", action="store_true", help="Generate file with Daily Practice template")

    args = parser.parse_args()

    if args.path:
        if path_exists(args.path):
            print(f"The path {args.path} exists.")
        else:
            print(f"The path {args.path} does not exist.")

    if args.file:
        if is_md_file(args.validatemd):
            print(f"{args.validatemd} is a valid Markdown file.")
        else:
            print(f"{args.validatemd} is not a valid Markdown file.")

    if args.read:
        print("Start reading file...")
        read_file(args.read)
        print("-Finish reading file-")

    if args.count:
        count_md_files(args.count)

    if args.generate:
        generate_md_file(args.generate, args)
        print("Multiple Markdown files are created.")

    if args.add:
        add_new_content(args.add, args.content)

    if args.update:
        update_content(args.update, args.content)
        print("New content is updated.")


if __name__ == "__main__":
    main()
