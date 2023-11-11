from md_file_manager import validate_file, validate_path, create_file, read_file, md_file_generate, count_md_files
import argparse


def main():
    parser = argparse.ArgumentParser(description="Welcome to MD File Manager program.")
    parser.add_argument("-vp", "--validatepath", type=str, help="Validate path")
    parser.add_argument("-vf", "--validatefile", type=str, help="Validate .md file")
    parser.add_argument("-c", "--create", type=str, help="Create simple MD file in the given directory. Enter . to create file in the current directory")
    parser.add_argument("-r", "--read", type=str, help="Read file.")
    parser.add_argument("-g", "--generate", type=str, help="Generate 7 .md files.")
    parser.add_argument("-cf", "--count", type=str, help="Count available .md files in given directory.")
    args = parser.parse_args()
    if args.create:
        create_file(args.create)
    elif args.read:
        read_file(args.read)
    elif args.generate:
        md_file_generate(args.generate)
    elif args.count:
        count_md_files(args.count)
    elif args.validatepath:
        validate_path(args.validatepath)
    elif args.validatefile:
        validate_file(args.validatefile)


if __name__ == "__main__":
    main()
