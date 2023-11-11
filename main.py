from md_file_manager import path_exists, is_md_file, read_file, generate_single_md_file
import argparse


def main():
    parser = argparse.ArgumentParser(description="Welcome to MD File Manager program.")
    parser.add_argument("-p", "--path", type=str, help="Check if the specified path exists in the system")
    parser.add_argument("-m", "--validatemd", type=str, help="Verify the specified file is a Markdown (.md) file")
    parser.add_argument("-cr", "--createmd", type=str, help="Create a new Markdown (.md) file in the specified directory. Use '.' to indicate the current directory.")
    parser.add_argument('-rd', "--readmd", type=str, help="Read and display the contents of a specified file.")

    args = parser.parse_args()

    if args.path:
        if path_exists(args.path):
            print(f"The path {args.path} exists.")
        else:
            print(f"The path {args.path} does not exist.")
    elif args.validatemd:
        if is_md_file(args.validatemd):
            print(f"{args.validatemd} is a valid Markdonw file")
        else:
            print(f"{args.validatemd} is not a valid Markdown file.")
    elif args.createmd:
        generate_single_md_file(args.createmd)
        print(f"Markdown is created in {args.createmd} directory.")
    elif args.readf:
        read_file(args.readf)


if __name__ == "__main__":
    main()
